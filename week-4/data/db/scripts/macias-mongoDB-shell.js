// Title: macias-mongoDB-shell.js
// Author: Andres Macias
// Date: 09/04/2022
// Description: queries for displaying user information from a mongoDB database.


// query to display all of the documents in the user's collection
printjson( db.users.find());

// query that finds the user with an email address of jbach@me.com
printjson(db.users.findOne({"email": "jbach@me.com"}));

// query that finds a user with the last name of Mozart
printjson(db.users.findOne({"lastName": "Mozart"}));

// query that finds the user with the first name of Richard
printjson(db.users.find({"firstName": "Richard"}));

// query that finds a user with an employeeId of 1010
printjson(db.users.findOne({"employeeId": "1010"}));