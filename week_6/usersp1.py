# Title: usersp1.py
# Author: Andres Macias
# Date: 09/15/22
# Description: Exercise 6.3 - Python with MongoDB, Part 1

# import MongoClient
from pymongo import MongoClient

# build connection string to connect to the client
myclient = MongoClient(
    "mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.pldlt.mongodb.net/?retryWrites=true&w=majority")

db = myclient['web335DB']

# Write the Python code to display all documents in the user’s collection.
for user in db.users.find({}):
    print(user)

# Write the Python code to display a document where the employeeId is 1011.
print(db.users.find_one({"employeeId": "1007"}))

# Write the Python code to display a document where the lastName is Mozart.
print(db.users.find_one({"lastName": "Mozart"}))
