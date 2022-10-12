from db import DbConnection
from users import Users
from books import Books
from librarian import Librarian
from utils import Entity


DbConnection.createDbConnection()

def menu():
    ops = input("Select operation type(add, update, delete, read, rent):")
    if ops == 'add':
        entity = input('Select type of entity to add(users,librarian,books):')
        if entity == Entity.USER.value:
            user = Users.get_input()
            user.create()
        elif entity == Entity.LIBRARIAN.value:
            lib = Librarian.get_input()
            lib.create()
        elif entity == Entity.BOOK.value:
            books = Books.get_input()
            books.create()
    if ops == 'update':
        entity = input('Select type of entity to update(users,books):')
        if entity == Entity.USER.value:
            user_id = input('Enter user id: ')
            name = input('Enter user name')
            Users.update(name, user_id)
        elif entity == Entity.BOOK.value:
            book_id = input('Enter book id: ')
            name = input('Enter user name')
            Books.update(name, book_id)

    if ops == 'delete':
        entity = input('Select type of entity to add(users,librarian,books):')
        if entity == Entity.USER.value:
            user_id = input('Enter user id: ')
            Users.delete(user_id)
        elif entity == Entity.BOOK.value:
            book_id = input('Enter book id: ')
            Books.delete(book_id)

    if ops == 'read':
        print()
        print("Available books are:")
        for book in Books.getall():
            print(book[0], book[1], book[2], book[3])

    if ops == 'rent':
        user_id = input('Enter userId: ')
        book_id = input('Enter bookId: ')
        Books.rent_to_user(user_id, book_id)
    menu()

menu()

# a) add user, add librarian, add books.
# b) update user details, update books details
# c) delete user, delete books
# d) read the books details and list of books available
# e) perform rental operations
