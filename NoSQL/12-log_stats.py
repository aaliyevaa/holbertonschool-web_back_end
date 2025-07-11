#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """ Returns and prints"""
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_count = mongo_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{status_count} status check")
                                                     

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
