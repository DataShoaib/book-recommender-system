📚 Book Recommendation System

A real-world Machine Learning–based Book Recommendation System that uses item-based collaborative filtering with cosine similarity to recommend books users are most likely to enjoy, based on collective user behavior.

Inspired by recommendation engines used in platforms like Amazon and Goodreads.






🚀 Live Demo

🔗 Deployed App:
👉 https://book-recommender-system-shoaib.streamlit.app/

📸 UI Preview
<p align="center"> <img src="assets/IMG_20250712_150636.jpg" width="90%" alt="Book Recommendation UI"> <br><br> <img src="assets/IMG_20250712_150725.jpg" width="90%" alt="Popular Books Section"> </p>
🎯 Problem Statement (Real-World ML)

With thousands of books available online, users often struggle to discover books that match their interests.

This project solves the problem of:

How can we recommend relevant books to users by learning from historical user–book interactions while ensuring scalability and fast response time?

🧠 Key Features

📖 Item-Based Collaborative Filtering

🔍 Book recommendations using cosine similarity

⭐ Top 30 most popular books displayed

⚡ Fast & interactive UI using Streamlit

🧱 Clean and minimal interface

🌐 Fully deployed and publicly accessible

⚙️ How the Recommendation System Works

User–book interaction data is transformed into a pivot table

Cosine similarity is calculated between books

A precomputed similarity matrix is stored for fast inference

When a user selects a book:

The system recommends Top 5 similar books

Popularity-based recommendations handle cold-start users

🛠️ Tech Stack

Language: Python

Libraries:

Pandas

NumPy

Scikit-learn

ML Concepts:

Recommender Systems

Collaborative Filtering

Cosine Similarity

Deployment: Streamlit

Model Storage: Pickle

📦 Installation & Setup
# Clone the repository
git clone https://github.com/DataShoaib/book-recommender-system.git
cd book-recommender-system

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/app.py

📂 Project Structure
book-recommender-system/
│
├── app/
│   └── app.py                  # Main Streamlit application
│
├── Artifacts/
│   └── models/
│       ├── book_pkl
│       ├── pt.pkl
│       ├── similarities.pkl
│       └── top_30_popular_book.pkl
│
├── assets/
│   ├── demo.txt
│   ├── IMG_20250712_150636.jpg
│   └── IMG_20250712_150725.jpg
│
├── data_raw/
│   ├── Books.csv.zip
│   ├── Ratings.csv.zip
│   └── Users.csv.zip
│
├── notebooks/
│   └── book_recommender_systen.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt

📊 Dataset Overview

Books Dataset: ISBN, title, author, publisher

Users Dataset: User IDs

Ratings Dataset: User–book ratings

These datasets simulate real-world recommendation system challenges such as sparsity and popularity bias.

📈 Key Learnings

Designing recommendation systems used in production

Working with sparse user–item matrices

Similarity-based ML modeling

Model serialization using Pickle

Deploying ML apps with Streamlit

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

🧑‍💻 Author

Shoaib Akhtar
🔗 GitHub: https://github.com/DataShoaib

📄 License

This project is licensed under the MIT License.
See the LICENSE
 file for details.

⭐ If you found this project helpful, consider starring the repository!