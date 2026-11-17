BOOKS = [
    {"id": 1, "title": "Wings of Fire", "author": "A. P. J. Abdul Kalam", "genre": "Biography"},
    {"id": 2, "title": "The Guide", "author": "R. K. Narayan", "genre": "Fiction"},
    {"id": 3, "title": "Malgudi Days", "author": "R. K. Narayan", "genre": "Short Stories"},
    {"id": 4, "title": "Ponniyin Selvan", "author": "Kalki Krishnamurthy", "genre": "Historical"}
]

def view_books():
    print("\n--- Available Books ---")
    for book in BOOKS:
        print(f'ID: {book["id"]} | {book["title"]} | '
              f'Author: {book["author"]} | Genre: {book["genre"]}')
