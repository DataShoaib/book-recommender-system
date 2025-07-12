import streamlit as st
import gzip
import pandas as pd
import numpy as np
import pickle


with gzip.open("book_with_rating.pkl.gz", "rb") as f:
    book_with_rating = pickle.load(f)

with open("similarities.pkl","rb")  as f:
    similarities=pickle.load(f)

with open("top_30_popular_book.pkl","rb") as f:
    top_30_popular_book=pickle.load(f)

with open("pt.pkl","rb") as f:
    pt=pickle.load(f)

with open("top_30_popular_book.pkl","rb") as f:
    top_30_books=pickle.load(f)

def recommender(book_name):
    idx = np.where(pt.index == book_name)[0][0]
    similar_books = sorted(list(enumerate(similarities[idx])), key=lambda x: x[1], reverse=True)[1:6]

    st.sidebar.title("📬 Contact Info")
    st.sidebar.markdown("**👨‍💻 Created by Shoaib**")
    st.sidebar.markdown("📧 Email: [mdshoaiba478@gmail.com]")
    st.sidebar.markdown("🐙 GitHub: [https://github.com/DataShoaib]")

    data = []

    for i in similar_books:
        item = []
        book_idx = i[0]
        book_title = pt.index[book_idx]

        temp_df = book_with_rating[book_with_rating["Book-Title"] == book_title]

        if not temp_df.empty:
            first_row = temp_df[["Book-Author", "Image-URL-M"]].drop_duplicates().iloc[0]
            item.append(book_title)
            item.append(first_row["Book-Author"])
            item.append(first_row["Image-URL-M"])
            data.append(item)
    return data


st.set_page_config(page_title="📚 Book Recommender", layout="wide")
st.title("📚 Book Recommendation System")

# 📍 Select book from dropdown or text input
book_list = pt.index.values
selected_book = st.selectbox("Choose a book to get recommendations:", book_list)

# 🔘 Recommend button
if st.button("Recommend"):
    recommendations = recommender(selected_book)

    st.subheader("📖 Top 5 Recommended Books")

    # Display in 5 columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"**{recommendations[idx][0]}**")
            st.markdown(f"*by {recommendations[idx][1]}*")
            st.image(recommendations[idx][2], width=150)

print(" ")

st.set_page_config(page_title="📚 Top 30 Books", layout="wide")
st.title("📚 Most Popular 30 Books")

st.subheader("🔥 Top 30 Books Based on Popularity")

# 🖼️ Show 30 books in grid (5 per row)
for i in range(0, 30, 5):
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if i + idx < len(top_30_books):
            row = top_30_books.iloc[i + idx]
            with col:
                st.markdown(f"**{row['Book-Title']}**", unsafe_allow_html=True)
                st.markdown(f"*by {row['Book-Author']}*")
                st.image(row["Image-URL-M"], width=140)
