/* 
Title: ministry_of_mongodb-whatabook.js
Author: Andres Macias
Group: William Watlington, Manel Phiseme
Date: 10/2/22
Description: MongoDB Shell Scripts for the book and customer collections. for Assignment 8 - WhatABook Database Modeling and Scripts
 */

// Delete the Book and Customer Collections
db.books.drop()
db.customers.drop()

// Create the book and customer collections
db.createCollection("houses", {
	validator: { $jsonSchema: {
		bsonType: "object",
		properties: {
			bookId: {
				bsonType: "string"
			},
			genre: {
				bsonType: "string"
			},
			author: {
				bsonType: "string"
			}
		}
	}}
})

db.createCollection("customer", {
	validator: { $jsonSchema: {
		bsonType: "object",
		properties: {
			customerId: {
				bsonType: "string"
			},
			firstName: {
				bsonType: "string"
			},
			lastName: {
				bsonType: "string"
			},
			wishlist: {
				bsonType: "array"
			}
		}
	}}
})

// Books
andyWeir = {
	"title": "project hail mary",
	"genre": "scifi",
	"author": "andy weir",
    "bookId": "9780593135204"
}

brandonSanderson = {
	"title": "the way of kings",
	"genre": "fantasy",
	"author": "brandon sanderson",
    "bookId": "9780765365279"
}

jrrTolken = {
	"title": "lord of teh rings",
	"genre": "fantasy",
	"author": "j.r.r tolkein",
    "bookId": "9780007203581"
}

colleenHoover = {
	"title": "verity",
	"genre": "thriller",
	"author": "collen hoover",
    "bookId": "9781408726600"
}



//Insert the documents.
db.houses.insertOne(andyWeir)
db.houses.insertOne(brandonSanderson)
db.houses.insertOne(jrrTolken)
db.houses.insertOne(colleenHoover)


// Customers
williamWatlington = {
	"firstName": "William",
	"lastName": "Watlington",
	"customerId": "c1005",
    "wishlist": []
}

manelPhiseme = {
	"firstName": "Manel",
	"lastName": "Phiseme",
	"customerId": "c1007",
    "wishlist": []
}

andresMacias = {
	"firstName": "Andres",
	"lastName": "Macias",
	"customerId": "c1006",
    "wishlist": []
}


//Insert the documents.
db.houses.insertOne(williamWatlington)
db.houses.insertOne(manelPhiseme)
db.houses.insertOne(andresMacias)