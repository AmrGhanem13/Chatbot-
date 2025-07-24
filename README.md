# 🧠 AI Chat Assistant with LLaMA 3, FastAPI, and Streamlit

This project integrates a powerful AI assistant using the **LLaMA 3-70B** model (via [Together.ai](https://www.together.ai)), deployed through a FastAPI backend and an interactive Streamlit frontend. It includes:

- ✅ Chat history (last 15 messages)
- ✅ Dynamic Streamlit UI
- ✅ Ngrok tunneling for public access

---

## 🚀 Features

- 💬 Chat with Meta’s **LLaMA 3-70B** via Together API  
- 🔁 Persistent chat memory (up to last 15 exchanges)  
- ⚡ FastAPI backend at `/llm/` endpoint  
- 🖥️ Streamlit frontend with user-friendly interface  
- 🌍 Ngrok support for global access  
- 🔒 Environment variables using `.env`  

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
pip install streamlit fastapi uvicorn python-dotenv together
```
## 📁 Project Structure
- project/
- ├── app.py              # Streamlit frontend UI
- ├── fast.py             # FastAPI backend API
- ├── .env                # API key config
- ├── .gitignore          # Ignored files
- ├── requirements.txt    # Dependencies
- └── README.md           # Documentation

## 🛠️ Run the App

- Start the FastAPI backend using Uvicorn:

```bash
uvicorn fast:app --reload
```

- Then in a new terminal, run the Streamlit frontend:

```bash
streamlit run app.py
```

## 👨‍💻 Author
Amr Ghanem
- |Software Engineer | Data Scientist & AI Developer
- 📫 Open to collaborations and contributions
