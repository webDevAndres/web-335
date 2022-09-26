# Title: usersp2.py
# Author: Andres Macias
# Date: 09/25/22
# Description: Exercise 7.3 - Python with MongoDB, Part 2

# import MongoClient
from pymongo import MongoClient
import datetime

# build connection string to connect to the client
myclient = MongoClient(
    "mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.pldlt.mongodb.net/?retryWrites=true&w=majority")

db = myclient['web335DB']

# Write the Python code to create a new user document.
db.users.insert_one({
    "firstName": "Joseph",
    "lastName": "Haydn",
    "employeeId": "1014",
    "email": "jhaydn@me.com",
    "dateCreated": datetime.datetime.now()
})


# Write the Python code to display the newly created document.
print(db.users.find_one({"employeeId": "1014"}))

# Write the Python code to update the email address of the document you created in step 2.
print(db.users.update_one(
    {"email": "jhaydn@me.com"},
    {"$set": {"email": "josephHaydn@me.com"}}
))

# Write the Python code to display the updated document.
print(db.users.find_one({"email": "josephHaydn@me.com"}))

# Write the Python code to delete the document you created in step 3.
db.users.delete_one({"email": "josephHaydn@me.com"})

# Write the Python code to prove the document was deleted.
print(db.users.find_one({"email": "josephHaydn@me.com"}))
