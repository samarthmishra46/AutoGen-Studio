from agents.base_agent import BaseAgent
import google.generativeai as genai
import os

# Optional: Load .env if you haven't already loaded the API key
from dotenv import load_dotenv
load_dotenv()

class ReviewerAgent(BaseAgent):
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def run(self, blog: str) -> str:
        prompt = f"Review this blog for grammar and tone:\n\n{blog}"
        response = self.model.generate_content(prompt)
        return response.text if hasattr(response, "text") else str(response)
