from agents.base_agent import BaseAgent
import google.generativeai as genai

class SEOAgent(BaseAgent):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-1.5-pro"
        self.chat = self.model.start_chat()

    def run(self, topic: str) -> dict:
        prompt = f"Generate 5 SEO keywords and 3 hashtags for the topic: {topic}"
        response = self.chat.send_message(prompt)
        
        lines = response.text.strip().split("\n")

        keywords = []
        hashtags = []

        for line in lines:
            line = line.strip()
            # Remove leading numbers or bullets
            if line and not line.startswith("#"):
                keyword = line.split(".")[-1].strip("-• ").strip()
                keywords.append(keyword)
            elif line.startswith("#"):
                hashtags.append(line.strip())

        # Safeguard in case model doesn't behave
        keywords = keywords[:5]
        hashtags = hashtags[:3]

        return {
            "keywords": keywords,
            "hashtags": hashtags,
            "caption": f"Discover insights on {topic}!"
        }
