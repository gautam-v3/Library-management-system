# Lib.py

def add_book(book_id, book_name):
    print("Book ID:", book_id)
    print("Book Name:", book_name)
    print("Book added successfully")

def login_user(username, password):
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid credentials")



def issue_book(book_id, student_id):
    print("Book", book_id, "issued to student", student_id)

def return_book(book_id, student_id):
    print("Book", book_id, "returned by student", student_id)
def view_books():
    print("Displaying all books")

