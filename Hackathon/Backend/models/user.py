from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError
from bson import ObjectId

# MongoDB connection URI
mongo_uri = "mongodb+srv://Rajan2125:Rajan2125@cluster0.odasbup.mongodb.net/iNotes"

# Create a MongoDB client
client = MongoClient(mongo_uri)

# Access a specific database (e.g., "iNotes" in this case)
db = client.iNotes

# Define the User collection (equivalent to a table in SQL databases)
user_collection: Collection = db.user

# Define a User document schema (equivalent to a document structure in MongoDB)
user_schema = {
    "name": {
        "type": "string",
        "required": True,
    },
    "email": {
        "type": "string",
        "required": True,
        "unique": True,
    },
    "password": {
        "type": "string",
        "required": True,
    },
    "date": {
        "type": "date",
        "default": "Date.now",
    },
}

# Function to create a new User document
def create_user(user_data):
    try:
        result = user_collection.insert_one(user_data)
        return result.inserted_id
    except DuplicateKeyError:
        return None

# Function to get a User by email
def get_user_by_email(email):
    return user_collection.find_one({"email": email})

# Function to get a User by ObjectId
def get_user_by_id(user_id):
    return user_collection.find_one({"_id": ObjectId(user_id)})

# Example usage:
# user_data = {
#     "name": "John Doe",
#     "email": "johndoe@example.com",
#     "password": "hashed_password",
#     "date": "optional_date",
# }
# user_id = create_user(user_data)
# user = get_user_by_email("johndoe@example.com")
# user_by_id = get_user_by_id(user_id)
