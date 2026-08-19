import random


def create_incident():

    ticket_id = f"INC{random.randint(100000, 999999)}"

    return ticket_id