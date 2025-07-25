#!/usr/bin/env python3
"""This module changes all topics of a document"""


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of school document"""
    mongo_collection.update_many(
        { "name": name },
        { "$set" : { "topics": topics }})
