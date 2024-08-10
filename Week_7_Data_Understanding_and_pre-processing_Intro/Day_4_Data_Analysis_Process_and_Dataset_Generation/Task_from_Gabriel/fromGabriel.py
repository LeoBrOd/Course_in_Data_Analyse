from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:VBms5kvdy7wR7MD4@cluster0.pkbvtyy.mongodb.net/")
db = client["bootcamp"]
collection = db["tweets"]

high_retweets = collection.find({"retweets": {"$gt": 100}})
for tweet in high_retweets:
    print(f"Tweet ID: {tweet['_id']}, Retweets: {tweet['retweets']}")
user_id_to_update = "6660c606301d30583f9712a3"
update_query = {"user": user_id_to_update}
update_operation = {"$inc": {"replies.likes": 10}}
collection.update_many(update_query, update_operation)
print(f"Likes incremented by 10 for all replies to user: {user_id_to_update}")
client.close()
