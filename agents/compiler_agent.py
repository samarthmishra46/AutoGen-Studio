from agents.base_agent import BaseAgent
import os, json, shutil

class CompilerAgent(BaseAgent):
    def run(self, content: dict) -> str:
        out = "outputs/generated_package"
        os.makedirs(out, exist_ok=True)

        # Write blog content
        with open(os.path.join(out, "blog.md"), "w") as f:
            f.write(content["blog"])

        # Write SEO JSON
        with open(os.path.join(out, "seo.json"), "w") as f:
            json.dump(content["seo"], f, indent=2)

        # Write caption
        with open(os.path.join(out, "caption.txt"), "w") as f:
            f.write(content["seo"]["caption"])

        # ✅ Fix image_url writing
        with open(os.path.join(out, "image_url.txt"), "w") as f:
            f.write(str(content["image_url"]))  # Or .url if available

        # Create zip
        shutil.make_archive(out, 'zip', out)
        return f"{out}.zip"
