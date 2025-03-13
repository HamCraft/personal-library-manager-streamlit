import streamlit as st
import json
import os

# JSON file path
FILE_PATH = "library.json"

# Load books from JSON file
def load_books():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

# Save books to JSON file
def save_books(books):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book(title, author, year):
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)

# Remove a book
def remove_book(title):
    books = load_books()
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)

# Streamlit UI
st.title("📚 Personal Library Manager")

# Display books
st.subheader("Your Library")
books = load_books()
search_query = st.text_input("Search by title or author", "")
filtered_books = [book for book in books if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]

if filtered_books:
    for book in filtered_books:
        st.write(f"**{book['title']}** by {book['author']} ({book['year']})")
        if st.button(f"Remove {book['title']}", key=book['title']):
            remove_book(book['title'])
            st.experimental_rerun()
else:
    st.write("No books found.")

# Add a book
st.subheader("Add a New Book")
title = st.text_input("Title")
author = st.text_input("Author")
year = st.text_input("Year")

if st.button("Add Book"):
    if title and author and year.isdigit():
        add_book(title, author, int(year))
        st.success(f"Added {title} to your library!")
        st.rerun()
    else:
        st.error("Please enter valid details.")
