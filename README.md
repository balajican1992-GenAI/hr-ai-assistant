# HR AI Assistant

## Project Overview
The HR AI Assistant is a Python-based application designed to assist HR professionals by leveraging AI capabilities. It provides functionalities such as document embedding, retrieval, and a user-friendly interface for interacting with the system.

## About the Project
The HR AI Assistant is designed to streamline HR processes by leveraging advanced AI technologies. It enables efficient document processing, information retrieval, and provides an intuitive interface for users. The modular architecture ensures scalability and ease of maintenance, making it a robust solution for HR professionals.

## Features
- **Document Embedding and Retrieval**: Efficiently process and retrieve information from documents using FAISS.
- **Gradio UI**: A user-friendly interface for interacting with the assistant.
- **API Endpoints**: Expose functionalities via RESTful APIs.
- **Modular Design**: Organized codebase with clear separation of concerns.

## Project Structure
```
requirements.txt
SESSION_HANDLING_GUIDE.md
app/
    config.py
    main.py
    api/
        endpoints.py
        router.py
    services/
        document_loader.py
        embedding.py
        message_service.py
        rag_service.py
        retriever.py
        text_splitter.py
        vector_store.py
    ui/
        gradio_ui.py
data/
    faiss_index/
        index.faiss
tests/
    test_ragservice.py
    test_vector.py
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/hr-ai-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hr-ai-assistant
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the Application
1. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```
2. Access the Gradio UI:
   Open your browser and navigate to the URL provided by the server.

### Running Tests
Run the test suite to ensure everything is working correctly:
```bash
pytest tests/
```

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search.
- [Gradio](https://gradio.app/) for the user interface.

---

Feel free to reach out for any questions or contributions!