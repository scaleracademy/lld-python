from parking_lot.models import ParkingGate
from parking_lot.repositories.gate_repository import GateRepository


class GateService:
    def __init__(self, gate_repository: GateRepository):
        self.gate_repository = gate_repository

    def get_gate(self, gate_id: int) -> ParkingGate:
        return self.gate_repository.get_gate(gate_id)
