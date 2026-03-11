# 🐰 Talking Rabbitt MVP

A conversational analytics prototype that allows users to upload a CSV dataset and ask questions about the data using natural language. The system returns **AI-generated insights and automatic visualizations**, demonstrating the "Magic Moment" of conversational data analysis.

---

## 🚀 Features

- Upload CSV sales dataset
- Ask questions in natural language
- AI-generated business insights
- Automatic chart generation
- Chat-style conversation interface
- Interactive visualizations using Plotly

---

## 🧠 Example Questions

Try asking:

- Which region generated the highest revenue?
- Show revenue trend over time
- Show revenue distribution by region
- Compare revenue by region

---

## 🏗 Architecture

User uploads CSV  
↓  
Streamlit frontend  
↓  
FastAPI backend  
↓  
Groq LLM processes question  
↓  
AI generates insight  
↓  
Chart generated automatically  

---

## 🛠 Tech Stack

Frontend:
- Streamlit
- Plotly

Backend:
- FastAPI
- Pandas

AI:
- Groq API (Llama 3.1 model)

---

## 📂 Project Structure

```
talking-rabbitt-mvp
│
├── backend
│   └── main.py
│
├── frontend
│   └── app.py
│
├── sales_data.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/talking-rabbitt-mvp.git
cd talking-rabbitt-mvp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start backend:

```bash
cd backend
uvicorn main:app --reload
```

Start frontend:

```bash
cd frontend
streamlit run app.py
```

---

## 🔐 Environment Variables

Create an environment variable for your Groq API key:

```bash
setx GROQ_API_KEY "your_api_key_here"
```

---

## ✨ Magic Moment

Instead of manually filtering Excel data, users can simply ask:

> "Which region generated the highest revenue?"

and instantly receive:

- a clear AI insight
- a visual chart

Turning **minutes of manual analysis into a 5-second conversation.**

---

## 📌 Future Improvements

- AI-driven chart selection
- advanced conversational analytics
- dataset auto-insights
- downloadable reports

---

## 👨‍💻 Author

Built as a prototype for the **Talking Rabbitt AI Product Manager assessment**.