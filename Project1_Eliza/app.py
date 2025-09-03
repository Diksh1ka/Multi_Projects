import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# Backend: Python
def echo(message, history):
    # LLM: OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful LLM teacher."},
            {
                "role": "user",
                "content": message
            }
        ]
    )
    
    return completion.choices[0].message.content

# Frontend: Gradio
demo = gr.ChatInterface(
    fn=echo, 
    type="messages", 
    examples=["I want to lear about LLMs", "What is NLP?", "What is RAG?"], 
    title="LLM Mentor",
    chatbot=gr.Chatbot(label="Eliza")
)
demo.launch()