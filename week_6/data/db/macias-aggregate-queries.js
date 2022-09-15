// Title: macias-aggregate-queries.js
// Author: Andres Macias
// Date: 09/12/2022
// Description: queries for displaying user information from a mongoDB database.


// query that shows a list of documents in the houses collection
printjson(db.houses.find());

// query that shows a list of documents in the student's collection
printjson(db.students.find());

// query to add a document to the student's collection and write a query to prove the document was added
printjson(db.students.insertOne({ "firstName": 'Ronald', "lastName": 'Weasley', "studentId": 's1019', "houseId": 'h1010' }));
printjson(db.students.findOne({ "lastName": "Weasley" }));

// query that deletes the document added above (add weasley as a student) and write a query to prove the document was deleted
printjson(db.students.deleteOne({ "studentId": "s1019" }));
printjson(db.students.findOne({ "lastName": "Weasley" }));

// query that list of students by house (lookup operation)
printjson(db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "house"
        }
    }
])
);

// query that shows a list of students for house Gryffindor
printjson(db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            pipeline: [
                {
                    $match: {
                        houseId: "h1007"
                    }
                }
            ],
            as: "house"
        },
    }
])
);

// query that shows a list of students for the Eagle mascot
printjson(db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            as: "houseMascot",
            let: { houseId: "$houseId" },
            pipeline: [
                {
                    $match: {
                        $expr: {
                            $and: [
                                { $eq: ["$houseId", "$$houseId"] },
                                { $eq: ["$mascot", "Eagle"] }
                            ]
                        }
                    }
                }
            ],
        }
    }
])
);