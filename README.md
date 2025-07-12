# 📚 Book Recommendation System

A content-based book recommender system built using Python and Streamlit, which helps users discover similar books based on their preferences. Just select a book and get top 5 personalized recommendations instantly!

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live--Demo-red)](https://book-recommender-system-shoaib.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Live Demo

🔗 **App Link:** [book-recommender-system-shoaib.streamlit.app](https://book-recommender-system-shoaib.streamlit.app)

<p align="center">
  <img src="assets/screenshot-1.jpg" width="100%" alt="UI Screenshot 1">
  <br><br>
  <img src="assets/screenshot-2.jpg" width="100%" alt="UI Screenshot 2">
</p>

---

## 🧠 Features

- 🔍 Recommend similar books using content-based filtering
- 📖 Top 30 most popular books displayed
- ⚡ Fast & interactive user experience with Streamlit
- 🧱 Clean and minimal UI design
- ✅ Deployed and accessible online

---

## 📦 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Pickle (for model serialization)

---

## 🛠️ Installation

```bash
git clone https://github.com/DataShoaib/book-recommender-system.git
cd book-recommender-system
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 How It Works

- The system uses **cosine similarity** on book feature vectors to find similar titles.
- It recommends 5 books based on the selected book using a precomputed similarity matrix.
- The dataset includes book metadata and popularity scores.

---

## 📸 Screenshots

| Recommendation Page | Popular Books Section |
|---------------------|------------------------|
| ![](assets/screenshot-1.jpg) | ![](assets/screenshot-2.jpg) |

---

## 📂 Project Structure

```
book-recommender-system/
│
├── app.py                # Main Streamlit app
├── books.csv             # Dataset file
├── similarity.pkl        # Precomputed similarity matrix
├── requirements.txt      # Required Python packages
├── assets/               # Screenshots folder
└── README.md             # You’re here!
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

## 🧑‍💻 Author

- **Shoaib Akhtar**  
  🔗 [GitHub - @DataShoaib](https://github.com/DataShoaib)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
