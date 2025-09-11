library = [(100, "Ikigai", "Hector Garcia", 1970),
    (101, "Wabi Sabi", "Beth Kempton", 1990),
    (102, "The Art Of Simple Living", "Shunmyo Masuno", 1956)]

def display_books():
    print("Library Catalog:\n")
    for book in library:
        print(f"ID: {book[0]}, Title:'{book[1]}',Author:{book[2]},Year:{book[3]}\n")

def findbook_byid(book_id):
    for book in library:
        if book[0]==book_id:
            return book
    return None

display_books()
try:
    search_id=int(input("Enter Book ID to search:"))
    book=findbook_byid(search_id)

    if book:
        print(f"\nBook Found:ID:{book[0]},Title:'{book[1]}',Author:{book[2]},Year:{book[3]}")
    else:
        print("\nBook not found.")
except ValueError:
    print("\nInvalid input.Please enter a numeric Book ID.")
