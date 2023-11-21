from parking_lot.models import ParkingGate


class GateRepository:
    def __init__(self):
        self.gates = []

    def get_gate(self, gate_id: int) -> ParkingGate:
        for gate in self.gates:
            if gate.id == gate_id:
                return gate
        raise ValueError("Gate not found")
