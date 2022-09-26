""" 
Title: ministry_of_mongodb-console.py
Author: William Watlington
Date: 25 September 2022
Description: Console application for whatabook project
"""

# import MongoDB client
from pymongo import MongoClient


# string from MongoDB for to connect to the whatabook database
client = MongoClient(
    "mongodb+srv://whatabookuser:s3cret@cluster0.ug54bka.mongodb.net/whatabookretryWrites=true&w=majority")

# variable for accessing the whatabook database
db = client['whatabook']

# display available commands to the user
print('Welcome to Whatabook. To view all books, type "list".\n To search by genre, type "genre".\n To display a list of books by author, type "author".\n To display a book by bookID, type "ID".\n To view a customer wishlist, type "wishlist".\n')

# get user input
user_command = input().lower()

# function to list all books


def list_books():
    for book in db.books.find({}):
        print('Title: ' + book['title'].title())
        print('Author: ' + book['author'].title())
        print('Genre: ' + book['genre'].title())
        print('Book ID: ' + book['bookId'] + '\n')

# function to allow users to list all books by genre


def genre_search():
    print('To list all books of the genre, type the corresponding number.\n Genres:')

    # find all distinct genres in books collection
    genres = sorted(db.books.distinct("genre"))
    for genre in genres:
        print("  " + genre.capitalize())

    user_genre = input().lower()
    # check if user input genre it exists and if so display all books of that genre
    if user_genre in genres:
        print("Available " + user_genre.capitalize() + " books:")
        genre_books = db.books.find({"genre": user_genre})
        for book in genre_books:
            print(' Title: ' + book['title'].title())
            print(' Author: ' + book['author'].title())
            print(' Genre: ' + book['genre'].title())
            print(' Book ID: ' + book['bookId'] + '\n')
    else:
        print("invalid input")

# function to allow users to list all books by a certain author


def author_search():
    print("Type the full name of the author you would like to see books by:")
    user_author = input().lower()
    all_authors = db.books.distinct("author")
    if user_author in all_authors:
        print("All available books by " + user_author.capitalize() + ":")
        author_books = db.books.find({"author": user_author})
        for book in author_books:
            print(' Title: ' + book['title'].title())
            print(' Author: ' + book['author'].title())
            print(' Genre: ' + book['genre'].title())
            print(' Book ID: ' + book['bookId'] + '\n')
    else:
        print("author not found")

# function to allow users to search by bookId (ISBN)


def id_search():
    print("Type the full ID (ISBN) of the book you would like to search for:")
    user_book_id = input().lower()
    try:
        id_book = db.books.find_one({"bookId": user_book_id})
        print('Book found:')
        print(' Title: ' + id_book['title'].title())
        print(' Author: ' + id_book['author'].title())
        print(' Genre: ' + id_book['genre'].title())
        print(' Book ID: ' + id_book['bookId'] + '\n')
    except:
        print("No book with that ID found")

# function to hold all wishlist options


def wishlist():
    print("To search for a wishlist, type the customerId.")
    user_input_id = input().lower()
    # check if user exists, notify user if no user with that ID is found
    try:
        # find user document from user input ID and print current wishlist
        wishlist_user = db.customers.find_one({"customerId": user_input_id})
        print("User found:")
        print("Name: " + wishlist_user['firstName'] +
              " " + wishlist_user['lastName'])
        print("Current Wishlist: ")
        if wishlist_user['wishlist']:
            for book in wishlist_user['wishlist']:
                print(' Title: ' + book['title'].title())
                print(' Author: ' + book['author'].title())
                print(' Genre: ' + book['genre'].title())
                print(' Book ID: ' + book['bookId'] + '\n')
        # prompt user to choose to add or remove book from wishlist
        print("To add a book to this user's wishlist, type 'add'.\nTo remove a book from this user's wishlist, type 'remove'")
        user_choice = input().lower()
        # if user chooses to add a book to the wishlist, prompt for the book ID, attempt to add it if it exists and print the updated database
        if user_choice == "add":
            print("Type the ID (ISBN) of the book you would like to add to the wishlist")
            input_id = input().lower()
            try:
                book_to_add = db.books.find_one({"bookId": input_id})
                db.customers.update_one(
                    {'customerId': user_input_id},
                    {'$push': {'wishlist': book_to_add}}
                )
                wishlist_user = db.customers.find_one(
                    {"customerId": user_input_id})
                print("Updated wishlist:")
                for book in wishlist_user['wishlist']:
                    print("Title: " + book['title'].title() +
                          "\nAuthor: " + book['author'].title())

            except:
                print("Book not found")
        # if user chooses to remove a book to the wishlist, prompt for the book ID, attempt to remove it if it exists and print the updated database
        elif user_choice == "remove":
            print(
                "Type the ID (ISBN) of the book you would like to remove from the wishlist")
            input_id = input().lower()
            try:
                db.customers.update_one(
                    {'customerId': user_input_id},
                    {'$pull': {'wishlist': {"bookId": input_id}}}
                )
                wishlist_user = db.customers.find_one(
                    {"customerId": user_input_id})
                print("Book removed.\nUpdated wishlist:")
                for book in wishlist_user['wishlist']:
                    print("Title: " + book['title'].title() +
                          "\nAuthor: " + book['author'].title())

            except:
                print("Book ID not found in this users's wishlist")
        else:
            print("Invalid input")
    except Exception as e:
        print(e)
        print("No user with that ID found")


# check if user input is valid and if so call corresponding function
if user_command == 'list':
    list_books()
elif user_command == 'genre':
    genre_search()
elif user_command == 'id':
    id_search()
elif user_command == 'author':
    author_search()
elif user_command == 'wishlist':
    wishlist()
else:
    print("invalid input")
