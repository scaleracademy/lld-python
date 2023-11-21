from typing import List
from parking_lot.models import Ticket


class TicketRepository:
    def __init__(self):
        self.tickets: List[Ticket] = []

    def create_ticket(self, ticket: Ticket) -> Ticket:
        self.tickets.append(ticket)
        return ticket
