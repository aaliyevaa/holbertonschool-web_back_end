#!/usr/bin/env python3
"""Provide some stats about Nginx logs"""
from pymongo import MongoClient


def main():
    client = MongoClient()
    collection = client.logs.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_count = collection.count_documents({"method": "GET",
                                               'path': '/status'})
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
