#!/usr/bin/env python3
"""This module returns the list of school with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school with the topic"""
    return list( mongo_collection.find(
            { "topics": topic }
            ))
