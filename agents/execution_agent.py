import random

def create_ticket():

    ticket_id = random.randint(
        100000,
        999999
    )

    return f"INC{ticket_id}"