# agents/image_designer_agent.py

from agents.base_agent import BaseAgent
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Gemini client
client = genai.Client()

class ImageDesignerAgent(BaseAgent):
    def run(self, prompt: str) -> str:
        print(f"🎨 Generating image for prompt: {prompt}")
        customer_prompt = f"Create a high-quality, blog-style illustration for a post titled: {prompt}. The image should be visually engaging and informative, ideally conveying the key concept of the topic. Use a clean, modern, and minimalistic style with soft shadows, smooth gradients, and a warm color palette. Avoid clutter. The design should suit a tech or educational blog layout."
        # Ensure the prompt is not empty
        # Request image generation with Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=customer_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"]
            )
        )

        # Create output directory
        os.makedirs("outputs", exist_ok=True)
        image_path = "outputs/generated_image.png"
        image_data_found = False

        # Parse the response
        for part in response.candidates[0].content.parts:
            if getattr(part, "inline_data", None):
                image_data = part.inline_data.data
                image = Image.open(BytesIO(image_data))
                image.save(image_path)
                image_data_found = True
                break

        if not image_data_found:
            raise Exception("❌ No image data returned by Gemini.")

        print(f"✅ Image saved to {image_path}")
        return image_path
