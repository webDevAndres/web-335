/* 
Title: ministry_of_mongodb-whatabook.js
Author: Andres Macias
Date: 9/25/22
Description: MongoDB queries for Assignment 7.2 - WhatABook Design
 */


// query list of all books
db.books.find( {} )

// query list books by genre
db.books.find( { "genre": user_genre } )

// query list books by author 
db.books.find( { "author": user_author } )

// query book by bookId
db.books.find_one( { "bookId": user_book_id } )

// query to list customer's wishlist
db.customers.find_one( { "customerId": user_input_id } )

// query to add a book to customer's wishlist
db.customers.update_one(
    { 'customerId': user_input_id },
    { '$push': {'wishlist': book_to_add } }
)

// query to remove a book from a customer's wishlist
db.customers.update_one(
    { 'customerId': user_input_id },
    { '$pull': {'wishlist': { "bookId": input_id }} }
)