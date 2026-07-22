class ConveyorTwin:
    def __init__(self):
        self.object_sensor = False
        self.type_sensor = False   # False = Type A, True = Type B
        self.e_stop = False

        self.gate_a = False
        self.gate_b = False
        self.count_a = 0
        self.count_b = 0
        self.system_enabled = True

    def scan_cycle(self):
        # Mirrors your E-stop rung: overrides everything else
        self.system_enabled = not self.e_stop

        sort_a_request = self.object_sensor and not self.type_sensor and self.system_enabled
        sort_b_request = self.object_sensor and self.type_sensor and self.system_enabled

        self.gate_a = sort_a_request
        self.gate_b = sort_b_request

        if sort_a_request:
            self.count_a += 1
        if sort_b_request:
            self.count_b += 1


if __name__ == "__main__":
    twin = ConveyorTwin()
    twin.object_sensor = True
    twin.type_sensor = False
    twin.scan_cycle()
    print("CountA:", twin.count_a, "GateA:", twin.gate_a)

    twin.e_stop = True
    twin.scan_cycle()
    print("After E-stop -> GateA:", twin.gate_a, "SystemEnabled:", twin.system_enabled)
