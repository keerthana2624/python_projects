
import json
import os
def add_book(books):
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    year=input("Enter the year of publication: ")
    genre=input("Enter the genre of the book: ")
    book={"title":title, "author":author,"year":year,"genre":genre}
    books.append(book)
    print("book added successfully")
# books=[]
# add_book(books)

def view_collection(books):
    if not books:
        print("No books in the collection.")
    else:
        for book in books:
            print("Title:", book['title'])
            print("Author:", book['author'])
            print("Year:", book['year'])
            print("Genre:", book['genre'])
            print()
# books=[]
# books=add_book(books)
# view_collection(books)


def save_to_json(books, filename="books.json"):
    try:
        with open(filename, "w") as file:
            json.dump(books, file)
        print(filename)
    except IOError as e:
        print(e)
# books = [
#     {"title": "Book One", "author": "Author One", "year": 2001, "genre": "Fiction"},
#     {"title": "Book Two", "author": "Author Two", "year": 2002, "genre": "Non-fiction"}
# ]
# save_to_json(books)


def load_from_json(filename="books.json"):
    try:
        if not os.path.exists(filename):
            print(filename)
            return []
        with open(filename, "r") as file:
            return json.load(file)
    
    except (IOError, json.JSONDecodeError) as e:
        print(e)
        return []
# books = load_from_json()
# print(books)

def main():
    books = load_from_json()
    while True:
        print("\n===== Personal Book Collection Management =====")
        print("1. Add Book")
        print("2. View Collection")
        print("3. Save to JSON")
        print("4. Load from JSON")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(books) 
        elif choice == '2':
            view_collection(books)
        elif choice == '3':
            save_to_json(books)
        elif choice == '4':
            books = load_from_json()
        elif choice == '5':
            save_to_json(books)
            print("Exiting program.")
            break 
        else:
            print("Invalid choice. Please try again.")
main()