#!/usr/bin/env python3
"""This module inserts a new document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a document and returns the _id"""
    return mongo_collection.insert_one(kwargs).inserted_id
