
# 🤖 Shiyas - AITwin

A small Streamlit app that lets you "chat" with Shiyas' AI Twin using the OpenAI-compatible client routed through Hugging Face's inference router. This README contains everything you need to run, secure, and develop the project.

---

🎯 Quick summary
- Tech: Python, Streamlit, OpenAI Python client (used with Hugging Face router)
- Main file: `app.py`
- Run: `streamlit run app.py`
- Secrets: HF token read from `.env` (variable: `HF_TOKEN`)

---

Demo Preview
- Open a terminal and run:
  - `streamlit run app.py`
- Visit the local Streamlit URL printed in the terminal (usually http://localhost:8501).

---

Requirements ✅
- Python 3.8+
- The project currently depends on:
  - streamlit
  - python-dotenv
  - openai
- The repository contains `requirement.txt` (note the filename). You can use it as-is or create a pinned `requirements.txt` for reproducible installs.

We recommend pinning versions for production. Example:
```
streamlit==1.25.0
python-dotenv==1.0.0
openai==1.0.0
```

---

Setup — Local (fastest)
1. Clone the repo:
   - git clone https://github.com/shiyyaas/shiyas-AITwin.git
   - cd shiyas-AITwin

2. Create & activate a virtual environment:
   - python -m venv .venv
   - macOS / Linux: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`

3. Install dependencies:
   - pip install -r requirement.txt
   (or rename `requirement.txt` → `requirements.txt` and run `pip install -r requirements.txt`)

4. Create environment variables:
   - Copy the example (below) into `.env` at repo root (do NOT commit `.env`):
     ```
     HF_TOKEN=your_huggingface_token_here
     ```
   - Alternatively export env var:
     - macOS / Linux: `export HF_TOKEN="your_token"`
     - Windows (cmd): `set HF_TOKEN=your_token`

5. Start the app:
   - streamlit run app.py

---

.env.example
```
# Copy to .env (DO NOT commit .env)
HF_TOKEN=
```

Important: Do NOT commit your real tokens to the repository. If you have already pushed a token, see the Security section below.

---

What app.py does (short)
- Loads environment variables via python-dotenv.
- Configures Streamlit page.
- Instantiates OpenAI client:
  - base_url is set to Hugging Face router: `https://router.huggingface.co/v1`
  - API key is read from `HF_TOKEN`
- Presents a simple chat UI using Streamlit's chat helpers and streams model responses.
- Uses `client.chat.completions.create(..., stream=True)` and `st.write_stream(stream)` to show streaming responses.

---

Files in repo
- app.py
- LICENSE (MIT)
- .gitignore
- requirement.txt

---

Development & Contribution 🤝
- Fork the repo, create a feature branch (`feat/xxx`), and open a PR.
- Keep PRs small and focused.
- Add tests for new logic if applicable.
- Follow simple style rules (black/isort) for Python formatting.

---

License
- This project is licensed under the MIT License. See `LICENSE` for details.

---

Contact & Credits
- Author: shiyas ps (as declared in LICENSE)
- If you want help hardening the app (removing secrets from history, adding CI or Docker, or improving the chat UX), Contact me we can disscuss.

---

Thank you! 🚀 Made with love
