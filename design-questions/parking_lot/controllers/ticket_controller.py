from parking_lot.models import ParkingTicket
from parking_lot.dtos import IssueTicketRequest
from parking_lot.services.ticket_service import TicketService


class TicketController:
    def __init__(self, ticket_service: TicketService):
        self.ticket_service = ticket_service

    def issue_ticket(self, request: IssueTicketRequest) -> ParkingTicket:
        self.validate_request(request)
        return self.ticket_service.issue_ticket(request)

    def validate_request(self, request: IssueTicketRequest):
        if request.parking_lot_id is None:
            raise ValueError("Parking lot ID is required")

        if request.vehicle_number is None:
            raise ValueError("Vehicle number is required")

        if request.entry_gate_id is None:
            raise ValueError("Entry gate ID is required")
