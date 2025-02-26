from pymongo import MongoClient
import time

def connect_to_db():
    """Connects to MongoDB and returns the client and database instance."""
    uri = "mongodb://localhost:27017"  # Replace with your MongoDB URI
    client = MongoClient(uri)
    db = client['DM']  # Replace with your database name
    return client, db

def delete_invalid_comments(db):
    """Deletes comments that reference non-existing posts."""
    collection = db["Comments"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "PostId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    comments_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [comment["Id"] for comment in comments_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid comments.")
    else:
        print("No invalid comments to delete.")

    print(f"Execution time for delete_invalid_comments: {time.time() - start_time:.2f} seconds")

def delete_invalid_posthistory(db):
    """Deletes posthistory records that reference non-existing posts."""
    collection = db["PostHistory"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "PostId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    posthistory_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [ph["Id"] for ph in posthistory_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid posthistory records.")
    else:
        print("No invalid posthistory records to delete.")

    print(f"Execution time for delete_invalid_posthistory: {time.time() - start_time:.2f} seconds")

def delete_invalid_postlinks(db):
    """Deletes postlinks that reference non-existing posts."""
    collection = db["PostLinks"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "PostId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    postlinks_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [pl["Id"] for pl in postlinks_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid postlinks.")
    else:
        print("No invalid postlinks to delete.")

    print(f"Execution time for delete_invalid_postlinks: {time.time() - start_time:.2f} seconds")

def delete_invalid_postlinks_related(db):
    """Deletes postlinks that reference non-existing related posts."""
    collection = db["PostLinks"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "RelatedPostId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    postlinks_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [pl["Id"] for pl in postlinks_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid postlinks based on relatedpostid.")
    else:
        print("No invalid postlinks based on relatedpostid to delete.")

    print(f"Execution time for delete_invalid_postlinks_related: {time.time() - start_time:.2f} seconds")

def delete_invalid_votes(db):
    """Deletes votes that reference non-existing posts."""
    collection = db["Votes"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "PostId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    votes_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [v["Id"] for v in votes_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid votes.")
    else:
        print("No invalid votes to delete.")

    print(f"Execution time for delete_invalid_votes: {time.time() - start_time:.2f} seconds")

def delete_invalid_badges(db):
    """Deletes badges that reference non-existing users."""
    collection = db["Badges"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Users",
                "localField": "UserId",
                "foreignField": "Id",
                "as": "matchedUsers"
            }
        },
        {"$match": {"matchedUsers": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    badges_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [b["Id"] for b in badges_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid badges.")
    else:
        print("No invalid badges to delete.")

    print(f"Execution time for delete_invalid_badges: {time.time() - start_time:.2f} seconds")

def delete_invalid_posthistory_user(db):
    """Deletes posthistory records that reference non-existing users."""
    collection = db["PostHistory"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Users",
                "localField": "UserId",
                "foreignField": "Id",
                "as": "matchedUsers"
            }
        },
        {"$match": {"matchedUsers": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    posthistory_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [ph["Id"] for ph in posthistory_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid posthistory records based on userid.")
    else:
        print("No invalid posthistory records based on userid to delete.")

    print(f"Execution time for delete_invalid_posthistory_user: {time.time() - start_time:.2f} seconds")

def delete_invalid_posts(db):
    """Deletes posts that reference non-existing users."""
    collection = db["Posts"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Users",
                "localField": "OwnerUserId",
                "foreignField": "Id",
                "as": "matchedUsers"
            }
        },
        {"$match": {"matchedUsers": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    posts_to_delete = list(collection.aggregate(pipeline))
    ids_to_delete = [p["Id"] for p in posts_to_delete]

    if ids_to_delete:
        result = collection.delete_many({"Id": {"$in": ids_to_delete}})
        print(f"Deleted {result.deleted_count} invalid posts.")
    else:
        print("No invalid posts to delete.")

    print(f"Execution time for delete_invalid_posts: {time.time() - start_time:.2f} seconds")

def update_accepted_answer(db):
    """Updates posts to nullify invalid accepted answers."""
    collection = db["Posts"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "AcceptedAnswerId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    posts_to_update = list(collection.aggregate(pipeline))
    ids_to_update = [p["Id"] for p in posts_to_update]

    if ids_to_update:
        result = collection.update_many({"Id": {"$in": ids_to_update}}, {"$set": {"AcceptedAnswerId": None}})
        print(f"Updated {result.modified_count} posts to nullify invalid accepted answers.")
    else:
        print("No posts to update for accepted answers.")

    print(f"Execution time for update_accepted_answer: {time.time() - start_time:.2f} seconds")

def update_parent_id(db):
    """Updates posts to nullify invalid parent IDs."""
    collection = db["Posts"]
    start_time = time.time()
    pipeline = [
        {
            "$lookup": {
                "from": "Posts",
                "localField": "ParentId",
                "foreignField": "Id",
                "as": "matchedPosts"
            }
        },
        {"$match": {"matchedPosts": {"$size": 0}}},
        {"$project": {"Id": 1}}
    ]

    posts_to_update = list(collection.aggregate(pipeline))
    ids_to_update = [p["Id"] for p in posts_to_update]

    if ids_to_update:
        result = collection.update_many({"Id": {"$in": ids_to_update}}, {"$set": {"ParentId": None}})
        print(f"Updated {result.modified_count} posts to nullify invalid parent IDs.")
    else:
        print("No posts to update for parent IDs.")

    print(f"Execution time for update_parent_id: {time.time() - start_time:.2f} seconds")

def main():
    client, db = connect_to_db()
    try:
        delete_invalid_comments(db)
        delete_invalid_posthistory(db)
        delete_invalid_postlinks(db)
        delete_invalid_postlinks_related(db)
        delete_invalid_votes(db)
        delete_invalid_badges(db)
        delete_invalid_posthistory_user(db)
        delete_invalid_posts(db)
        update_accepted_answer(db)
        update_parent_id(db)
    finally:
        client.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
