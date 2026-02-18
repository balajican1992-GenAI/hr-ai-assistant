
import gradio as gr
import requests

API_URL = "http://localhost:8000/chat"

def chat_fn(message, history):
    try:
        response = requests.post(API_URL, json={"message": message})
        if response.status_code == 200:
            data = response.json()
            return data.get("response", str(data))
        else:
            return f"API Error: {response.status_code} {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def launch_ui():

    demo = gr.ChatInterface(
        fn=chat_fn,
        title="HR AI Assistant",
        description="Ask HR-related questions from the knowledge base.",
        examples=[
            "Rewards Program",
            "Nestle Policy?"
        ],
    )
    demo.launch()



# Run the UI if this script is executed directly
if __name__ == "__main__":
    launch_ui()

