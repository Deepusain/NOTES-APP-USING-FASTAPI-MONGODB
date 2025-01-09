from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://deepaknai1881:xC0xT3BHtIzcXsbJ@notesapp.xiy9h.mongodb.net/")
db = client.notes_app
notes_collection = db.notes
