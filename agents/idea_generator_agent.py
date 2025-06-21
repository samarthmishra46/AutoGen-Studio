from agents.base_agent import BaseAgent

class IdeaGeneratorAgent(BaseAgent):
    def run(self, topic: str) -> dict:
        return {"title": f"Exploring {topic}", "formats": ["blog", "image", "caption", "seo"]}
