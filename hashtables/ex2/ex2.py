#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    start = hash_table_retrieve(hashtable, "NONE")
    index = 0
    current = start
    route[index] = current
    while current != 'NONE':
        index += 1
        new = hash_table_retrieve(hashtable, current)
        route[index] = new
        current = new
    route[index] = "NONE"
    return route
