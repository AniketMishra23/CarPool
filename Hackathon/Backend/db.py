from pymongo import MongoClient

# MongoDB connection URI
mongo_uri = "mongodb+srv://Rajan2125:Rajan2125@cluster0.odasbup.mongodb.net/iNotes"

def mongo_connection():
    try:
        # Create a MongoDB client
        client = MongoClient(mongo_uri)
        
        # Access a specific database (e.g., "iNotes" in this case)
        db = client.iNotes

        print("MongoDB connected")

        return db
    except Exception as e:
        print(f"MongoDB not connected because: {e}")

# Example usage:
# db = mongo_connection()
# collection = db['your_collection_name']
# Now you can perform database operations using the 'collection' object.
