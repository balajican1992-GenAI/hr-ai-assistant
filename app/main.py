
from fastapi import FastAPI
from app.api.router import router

app = FastAPI()
app.include_router(router)

# Optional: allow running Gradio UI for local testing
def run_gradio():
    from app.ui.gradio_ui import launch_ui
    launch_ui()

if __name__ == "__main__":
    run_gradio()