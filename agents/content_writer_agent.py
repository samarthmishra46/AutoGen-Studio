from agents.base_agent import BaseAgent
import os
import google.generativeai as genai

# ✅ Correct configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class ContentWriterAgent(BaseAgent):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")  # You can also use "gemini-1.5-pro"
        self.chat = self.model.start_chat()

    def run(self, topic: str) -> str:
        prompt = f"Write a detailed 600-word blog article about: {topic}"
        response = self.chat.send_message(prompt)
        return response.text
