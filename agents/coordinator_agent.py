# agents/coordinator_agent.py

from agents.base_agent import BaseAgent
from agents.idea_generator_agent import IdeaGeneratorAgent
from agents.content_writer_agent import ContentWriterAgent
from agents.image_designer_agent import ImageDesignerAgent
from agents.seo_agent import SEOAgent
from agents.reviewer_agent import ReviewerAgent
from agents.compiler_agent import CompilerAgent

class CoordinatorAgent(BaseAgent):
    def run(self, topic: str) -> dict:
        idea = IdeaGeneratorAgent().run(topic)
        blog = ContentWriterAgent().run(topic)
        image_path = ImageDesignerAgent().run(topic)
        seo = SEOAgent().run(topic)
        review = ReviewerAgent().run(blog)
        package_path = CompilerAgent().run({
            "blog": blog,
            "image_url": image_path,
            "seo": seo
        })

        return {
            "idea": idea,
            "blog": blog,
            "image": image_path,   # <- this fixes your error
            "seo": seo,
            "review": review,
            "package": package_path
        }
