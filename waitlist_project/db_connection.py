from pymongo import MongoClient

client = MongoClient('mongodb+srv://bonnil1:RSbwNeR6PEjKIDr0@cluster0.l5tb27a.mongodb.net/waitlist_app?retryWrites=true&w=majority')
db = client['waitlist_app']