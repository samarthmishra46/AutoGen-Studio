
# 🤖 AutoGen Studio

**AutoGen Studio** is an AI-powered multi-agent content creation system that generates blogs, SEO metadata, images, and captions—all from a single prompt. Built using **Google Cloud Vertex AI**, **Gemini**, and open-source tools, the platform showcases intelligent agent collaboration for autonomous content generation.

---

## 🚀 Features

- 🔁 Multi-Agent Architecture using modular AI agents
- ✍️ Blog writing via Gemini (Google Generative AI)
- 🎨 AI-generated images via Gemini or Hugging Face models
- 📈 SEO optimization (keywords, hashtags, caption)
- 🧠 Content review and tone correction
- 📦 Auto-compiled output into downloadable blog packages
- 🌐 Optional Streamlit frontend for user-friendly interaction

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **LLMs:** Google Gemini 1.5 Pro / Flash
- **Image Models:** Gemini image generation or HuggingFace stable diffusion
- **Agent System:** Modular Python classes
- **Deployment:** Google Cloud (Vertex AI + Gemini API)
- **Frontend:** [Optional] Streamlit for UI
- **Environment Management:** `venv` + `.env`

---

## 📂 Project Structure

```
autogen_studio/
├── main.py                         # Entry point for CLI or Streamlit
├── agents/
│   ├── base_agent.py              # Base class for agents
│   ├── coordinator_agent.py      # Orchestrates all sub-agents
│   ├── content_writer_agent.py   # Generates blog content
│   ├── seo_agent.py              # Generates SEO keywords + hashtags
│   ├── image_designer_agent.py   # Generates images from prompt
│   ├── reviewer_agent.py         # Reviews grammar + tone
│   ├── compiler_agent.py         # Compiles all output into files
│   └── idea_generator_agent.py   # Suggests a catchy blog title
├── outputs/
│   └── generated_package.zip     # Generated result bundle
├── .env                          # API keys and secrets
└── README.md
```

---

## 🧪 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/autogen-studio.git
cd autogen-studio
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file:
```env
GOOGLE_API_KEY=your_google_generative_ai_key
HUGGINGFACE_TOKEN=your_huggingface_api_key
REPLICATE_API_TOKEN=your_optional_replicate_api_key
```

---

## ⚙️ How to Run

### ▶️ CLI Version
```bash
python3 main.py
```

### 🌐 Streamlit Version
```bash
streamlit run main.py
```

---

## 🧠 Agents in Action

AutoGen Studio uses multiple agents working together:
| Agent | Role |
|-------|------|
| `IdeaGeneratorAgent` | Generates a catchy blog title |
| `ContentWriterAgent` | Creates the blog content |
| `ImageDesignerAgent` | Generates an image based on the topic |
| `SEOAgent` | Suggests keywords, hashtags, captions |
| `ReviewerAgent` | Reviews grammar and tone |
| `CompilerAgent` | Packages everything into files |

---

## 💡 Example Output

- 📝 Blog: `outputs/blog.md`
- 🎨 Image: `outputs/generated_image.png`
- 📈 SEO: `outputs/seo.json`
- 🧾 Caption: `outputs/caption.txt`
- 📦 Final Package: `outputs/generated_package.zip`

---

## 🌍 Deployment

To deploy using Google Cloud:
- Enable **Vertex AI API** and **Generative AI Studio** in your project
- Create a service account or use API key-based authentication
- Deploy using GCP Functions or App Engine (optional)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

We welcome contributions! Feel free to fork this repository and submit a PR.

---

## 📫 Contact

For support, questions, or collaborations, contact:

- [Samarth Mishra](mailto:samarthmishra46@gmail.com)
- [Project Discussions](https://github.com/yourusername/autogen-studio/discussions)
# AutoGen_Studio
# AutoGen_Studio
# AutoGen_Studio
# AutogenStudio
# AutoGen-Studio
