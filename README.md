# 📚 Book Recommendation System

A real-world Machine Learning–based Book Recommendation System that uses item-based collaborative filtering with cosine similarity to recommend books users are most likely to enjoy, based on collective user behavior.

Inspired by recommendation engines used by platforms like Amazon and Goodreads.

---

## 🚀 Live Demo


🔗 **App Link:**  
👉 https://datashoaib-book-recommender-system-appapp-adexhh.streamlit.app/

---

## 📸 UI Preview

<p align="center">
  <img src="assets/IMG_20250712_150636.jpg" width="90%" alt="Book Recommendation UI">
  <br><br>
  <img src="assets/IMG_20250712_150725.jpg" width="90%" alt="Popular Books Section">
</p>

---

## 🎯 Problem Statement (Real-World ML)

Online book platforms host thousands of books, making it difficult for users to discover content that aligns with their interests. This often results in poor personalization and reduced user engagement.

**This project addresses the question:**

> *How can we recommend relevant books to users by learning from historical user–book interactions while ensuring scalability and fast response time?*

---

## 🧠 Key Features

- 📖 Item-based Collaborative Filtering  
- 🔍 Book recommendations using cosine similarity  
- ⭐ Displays Top 30 most popular books  
- ⚡ Fast & interactive UI built with Streamlit  
- 🧱 Clean and minimal user interface  
- 🌐 Fully deployed and publicly accessible  

---

## ⚙️ How the Recommendation System Works

- User–book interaction data is converted into a pivot table  
- Cosine similarity is calculated between books  
- A precomputed similarity matrix is stored for fast inference  
- When a user selects a book:  
  - The system recommends Top 5 similar books  
- Popularity-based recommendations handle cold-start users  

---

## 🛠️ Tech Stack

**Language**
- Python  

**Libraries**
- Pandas  
- NumPy  
- Scikit-learn  

**ML Concepts**
- Recommender Systems  
- Collaborative Filtering  
- Cosine Similarity  

**Deployment**
- Streamlit  

**Model Storage**
- Pickle  

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/DataShoaib/book-recommender-system.git
cd book-recommender-system

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/app.py
