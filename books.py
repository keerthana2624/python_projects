def add_book(books):
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    year=input("Enter the year of publication: ")
    genre=input("Enter the genre of the book: ")
    book={"title":title, "author":author,"year":year,"genre":genre}
    books.append(book)
    print("book added successfully")
books=[]
add_book(books)

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
books=[]
books=add_book(books)
view_collection(books)

 