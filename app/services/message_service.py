import sqlite3
import uuid
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parents[2]
DB_DIR = BASE_DIR / "data"
DB_PATH = DB_DIR / "chat_history.db"


def _get_connection() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with _get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(session_id) REFERENCES sessions(session_id)
            )
            """
        )
        connection.commit()


def create_session(user_id: str) -> str:
    if not user_id or not user_id.strip():
        raise ValueError("user_id is required")

    session_id = str(uuid.uuid4())
    with _get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO sessions (session_id, user_id) VALUES (?, ?)",
            (session_id, user_id.strip()),
        )
        connection.commit()

    return session_id


def save_message(user_id: str, session_id: str, role: str, content: str) -> None:
    allowed_roles = {"user", "assistant", "system"}

    if not user_id or not user_id.strip():
        raise ValueError("user_id is required")
    if not session_id or not session_id.strip():
        raise ValueError("session_id is required")
    if role not in allowed_roles:
        raise ValueError("role must be one of: user, assistant, system")
    if not content or not content.strip():
        raise ValueError("content is required")

    with _get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1 FROM sessions WHERE session_id = ? AND user_id = ?",
            (session_id.strip(), user_id.strip()),
        )
        session_exists = cursor.fetchone()
        if not session_exists:
            raise ValueError("session_id not found for this user")

        cursor.execute(
            """
            INSERT INTO messages (user_id, session_id, role, content)
            VALUES (?, ?, ?, ?)
            """,
            (user_id.strip(), session_id.strip(), role, content.strip()),
        )
        connection.commit()


def get_chat_history(user_id: str, session_id: str, limit: int = 20) -> List[Dict[str, str]]:
    if not user_id or not user_id.strip():
        raise ValueError("user_id is required")
    if not session_id or not session_id.strip():
        raise ValueError("session_id is required")
    if limit <= 0:
        raise ValueError("limit must be greater than 0")

    with _get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1 FROM sessions WHERE session_id = ? AND user_id = ?",
            (session_id.strip(), user_id.strip()),
        )
        session_exists = cursor.fetchone()
        if not session_exists:
            raise ValueError("session_id not found for this user")

        cursor.execute(
            """
            SELECT role, content, created_at
            FROM messages
            WHERE user_id = ? AND session_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (user_id.strip(), session_id.strip(), limit),
        )
        rows = cursor.fetchall()

    history = [
        {
            "role": row["role"],
            "content": row["content"],
            "created_at": row["created_at"],
        }
        for row in reversed(rows)
    ]

    return history
