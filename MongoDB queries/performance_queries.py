from pymongo import MongoClient
from datetime import datetime, timedelta
import time

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["DM"]

# Define MongoDB collections
posts = db["Posts"]
users = db["Users"]
comments = db["Comments"]

def measure_time(func, description):
    start_time = time.time()
    print(f"Starting {description} at {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}")
    func()
    end_time = time.time()
    print(f"{description} executed in {end_time - start_time:.4f} seconds\n")

# 1. Simple Reads
def simple_reads():
    results = posts.find({"CreationDate": {"$gte": datetime(2009, 1, 1), "$lte": datetime(2009, 12, 31)}})
    for post in results:
        pass  # Simulating processing

#measure_time(simple_reads, "Simple Reads")

# 2. Write Operations
def write_operations():
    posts.insert_many([
        {"Id": 2, "PostTypeId": 1, "CreationDate": datetime.now(), "Score": 10, "Title": "Title 1", "Body": "Body 1", "Tags": "<mac><crash>"},
        {"Id": 3, "PostTypeId": 2, "CreationDate": datetime.now(), "Score": 15, "Title": "Title 2", "Body": "Body 2", "Tags": "<windows>"}
    ])

#measure_time(write_operations, "Write Operations")

# 3. Joins
def joins():
    results = posts.aggregate([
        {"$lookup": {"from": "Users", "localField": "OwnerUserId", "foreignField": "Id", "as": "owner"}},
        {"$unwind": "$owner"},
        {"$project": {"_id": 0, "Title": 1, "OwnerDisplayName": "$owner.DisplayName"}}
    ])
    for result in results:
        pass  # Simulating processing

#measure_time(joins, "Joins")

# 4. Aggregation
def aggregation():
    results = posts.aggregate([
        {"$unwind": "$Tags"},
        {"$group": {"_id": "$Tags", "count": {"$sum": 1}}}
    ])
    for result in results:
        pass  # Simulating processing

#measure_time(aggregation, "Aggregation")

# 5. Text Search
def text_search():
    results = posts.find({"Body": {"$regex": "virtual machine", "$options": "i"}})
    for post in results:
        pass  # Simulating processing

#measure_time(text_search, "Text Search")

# 6. Nested Updates
def nested_updates():
    owners_with_more_than_10_posts = posts.aggregate([
        {"$group": {"_id": "$OwnerUserId", "postCount": {"$sum": 1}}},
        {"$match": {"postCount": {"$gt": 10}}}
    ])
    owner_ids = [owner["_id"] for owner in owners_with_more_than_10_posts]
    users.update_many({"Id": {"$in": owner_ids}}, {"$inc": {"Reputation": 10}})

#measure_time(nested_updates, "Nested Updates")

# 7. Complex Joins
def complex_joins():
    results = posts.aggregate([
        {"$lookup": {"from": "Comments", "localField": "Id", "foreignField": "PostId", "as": "comments"}},
        {"$unwind": "$comments"},
        {"$lookup": {"from": "Users", "localField": "comments.UserId", "foreignField": "Id", "as": "commentUser"}},
        {"$unwind": "$commentUser"},
        {"$project": {"_id": 0, "Title": 1, "CommentText": "$comments.Text", "CommenterName": "$commentUser.DisplayName"}}
    ])
    for result in results:
        pass  # Simulating processing

#measure_time(complex_joins, "Complex Joins")

# 8. Pagination
def pagination():
    results = posts.find().sort("CreationDate", -1).skip(20).limit(10)
    for post in results:
        pass  # Simulating processing

measure_time(pagination, "Pagination")

# 9. Deletion
def deletion():
    post_ids_with_comments = comments.distinct("PostId")
    posts.delete_many({"Score": {"$lt": 5}, "Id": {"$nin": post_ids_with_comments}})

measure_time(deletion, "Deletion")

# 10. Counting
def counting():
    count = users.count_documents({"Reputation": {"$gt": 100}})
    print(f"Number of users with Reputation > 100: {count}")

measure_time(counting, "Counting")

# Close the connection
client.close()
