from parking_lot.models import ParkingTicket
from parking_lot.enums import ParkingSpotStatus, ParkingSpotType, VehicleType
from parking_lot.repositories.ticket_repository import TicketRepository
from parking_lot.services.spot_service import ParkingSpotService
from parking_lot.services.gate_service import GateService
from parking_lot.services.vehicle_service import VehicleService
from parking_lot.dtos import IssueTicketRequest


class TicketService:
    def __init__(
        self,
        spot_service: ParkingSpotService,
        gate_service: GateService,
        vehicle_service: VehicleService,
        ticket_repository: TicketRepository,
    ):
        self.spot_service = spot_service
        self.gate_service = gate_service
        self.vehicle_service = vehicle_service
        self.ticket_repository = ticket_repository

    def issue_ticket(self, request: IssueTicketRequest) -> ParkingTicket:
        # Check if a parking spot is available
        parking_spot = self.spot_service.allocate_spot(
            request.parking_lot_id, TicketService.decide_spot_type(request.vehicle_type)
        )
        if parking_spot is None:
            raise ValueError("No parking spot available")

        # Update the parking spot to mark it as occupied
        parking_spot.status = ParkingSpotStatus.OCCUPIED

        # Save the spot in the database
        self.spot_service.save_parking_spot(parking_spot)

        # Fetch the entry gate from the database
        entry_gate = self.gate_service.get_gate(request.entry_gate_id)

        # Create a new vehicle object if the vehicle is not present in the system, else fetch the vehicle from the database
        vehicle = self.vehicle_service.find_or_create_vehicle(
            request.vehicle_number, request.vehicle_type
        )

        # Create a new ticket object
        ticket = ParkingTicket(parking_spot, request.entry_time, vehicle, entry_gate)

        # Save the ticket in the database
        self.ticket_repository.create_ticket(ticket)
        return ticket

    @staticmethod
    def decide_spot_type(vehicle_type: VehicleType) -> ParkingSpotType:
        return {
            VehicleType.CAR: ParkingSpotType.MEDIUM,
            VehicleType.TRUCK: ParkingSpotType.LARGE,
            VehicleType.BUS: ParkingSpotType.LARGE,
            VehicleType.BIKE: ParkingSpotType.SMALL,
            VehicleType.SCOOTER: ParkingSpotType.SMALL,
        }[vehicle_type]
