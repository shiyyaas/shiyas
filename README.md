# 🤖 Shiyas - AITwin

A small Streamlit app that lets you "chat" with Shiyas' AI Twin using the OpenAI-compatible client routed through Hugging Face's inference router.

---

## 🎯 Quick Summary

* **Tech:** Python, Streamlit, OpenAI Python client (Hugging Face router)
* **Main file:** `app.py`
* **Run:** `streamlit run app.py`
* **Secret:** HF token in `.env` file

---

## 🚀 Setup

1. **Clone the repo:**
```bash
   git clone https://github.com/shiyyaas/shiyas-AITwin.git
   cd shiyas-AITwin
```

2. **Create virtual environment:**
```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\Activate.ps1  # Windows
```

3. **Install dependencies:**
```bash
   pip install -r requirement.txt
```

4. **Add your Hugging Face token:**
   * Create a `.env` file in the repo root:
```
     HF_TOKEN=your_huggingface_token_here
```
   * **Important:** Never commit `.env` to GitHub!

5. **Run the app:**
```bash
   streamlit run app.py
```
   Visit `http://localhost:8501` in your browser.

---

## 🎭 About This AI Twin

This is an AI clone of me (Shiyas PS). Everyone has different perspectives about who I am, and all viewpoints are valuable.

**Current personality:**
> Your name is Shiyas PS. You're a self-confident person, you are kind. You're a BCA student. You are very serious person, You're not being silly.

### Help Shape My Personality 🤝

Know me personally? Think something's missing or inaccurate? Your contributions are welcome!

**How to contribute:**

1. **Open an issue** - Describe what should change about the personality and why
2. **Submit a PR** - Update the system prompt in `app.py` with improved personality traits
3. **Provide examples** - Show how I actually communicate or respond to situations

**Guidelines:**

* Don't remove existing traits without opening an issue first - let's discuss it
* Explain your reasoning clearly
* Real examples are helpful for context

Your contributions help make this AI twin more accurate. Thank you! 🎯

---

## 🛠️ Development & Contribution

Contributions to improve the project are welcome.

* Fork the repo, create a feature branch, and open a PR
* Keep PRs focused and small
* Follow Python best practices (black/isort formatting)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 📞 Contact

**Author:** Shiyas PS  
**Live Demo:** [shiyasaitwin.streamlit.app](https://shiyasaitwin.streamlit.app)

Questions or suggestions? Feel free to reach out!

---

Made with ❤️
