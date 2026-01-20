# 📚 Book Recommendation System

🔍 This project uses **item-based collaborative filtering** with cosine similarity on a user-book rating matrix to recommend similar books based on what other users have rated.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live--Demo-red)](https://book-recommender-system-shoaib.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Live Demo

🔗 **App Link:** [book-recommender-system-shoaib.streamlit.app](https://book-recommender-system-shoaib.streamlit.app)

## 📸 UI Screenshots

<p align="center">
  <img src="assets/IMG_20250712_150636.jpg" width="90%" alt="Book Recommender Screenshot 1">
  <br><br>
  <img src="assets/IMG_20250712_150725.jpg" width="90%" alt="Book Recommender Screenshot 2">
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
├── app/
│   └── app.py                  # Main Streamlit app
├── Artifacts/                  # Pretrained models and data artifacts
│   ├── book_with_rating.pkl.gz
│   ├── pt.pkl
│   ├── similarities.pkl
│   └── top_30_popular_book.pkl
├── assets/                     # Screenshots and demo files
│   ├── demo.txt
│   ├── IMG_20250712_150636.jpg
│   └── IMG_20250712_150725.jpg
├── data/
│   └── raw/                    # Raw dataset files
│       ├── Books.csv.zip
│       ├── Ratings.csv.zip
│       └── Users.csv.zip
├── notebooks/                  # Jupyter notebooks
├── .gitignore
├── README.md
└── requirements.txt

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
