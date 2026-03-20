# 🧠 AI Mind Map Generator

An intelligent web application that converts unstructured documents into **structured, interactive mind maps** using AI.

---

## 🚀 Features

* 📄 Upload documents (PDF, DOCX, TXT)
* 🤖 AI-powered text summarization
* 🧠 Automatic concept extraction
* 🌳 Hierarchical mind map generation (3–4 levels)
* 🎯 Interactive visualization using D3.js
* 💬 Clickable nodes with explanations
* 🌌 Modern UI with animations and dark/light mode

---

## 🛠️ Tech Stack

### 🔹 Backend

* Python (Flask)
* Transformers (Hugging Face)
* PyTorch
* pdfplumber, python-docx

### 🔹 Frontend

* HTML, CSS, JavaScript
* D3.js (for visualization)
* Particles.js (for background effects)

---

## 📂 Project Structure

```
ai-mindmap-generator/
│
├── backend/
│   ├── app.py
│   ├── utils/
│   │   ├── parser.py
│   │   ├── nlp.py
│   │   ├── mindmap.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── style.css
│   │   ├── script.js
│   │   └── particles.js
│
├── uploads/
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/ai-mindmap-generator.git
cd ai-mindmap-generator
```

---

### 2️⃣ Create Virtual Environment

```
py -3.11 -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```
cd backend
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User uploads a document
2. Text is extracted (PDF/DOCX/TXT)
3. AI generates a summary using NLP
4. Keywords & topics are identified
5. AI generates explanations for each concept
6. Data is converted into a hierarchical graph
7. D3.js renders an interactive mind map

---

## 💡 Sample Output

```
Document
├── Business Objective
│   ├── Cost
│   │   ├── Reduces operational expenses
│   │   ├── Improves efficiency
│   ├── Revenue
│   │   ├── Increases income streams
│   │   ├── Enhances growth
```

---

## ⚠️ Notes

* First run may take time due to AI model download (~300–500MB)
* Use Python 3.11 for best compatibility
* Avoid uploading scanned PDFs (text extraction may fail)

---

## 🚀 Future Enhancements

* 🔐 User authentication & saved mind maps
* 🤖 Chat with mind map nodes
* 📱 Mobile responsive UI
* 📊 Export as image/PDF
* 🌍 Deploy on cloud

---

## 👨‍💻 Author

D.Drona Madhuri
B.Tech CSE (AI/ML)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
