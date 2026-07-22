import time
import random
from opcua import Server
from digital_twin import ConveyorTwin

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4841/gateway/")
idx = server.register_namespace("http://conveyor.twin")

objects = server.get_objects_node()
gw = objects.add_object(idx, "ConveyorTwin")

count_a_var = gw.add_variable(idx, "CountA", 0)
count_b_var = gw.add_variable(idx, "CountB", 0)
enabled_var = gw.add_variable(idx, "SystemEnabled", True)

server.start()
print("Digital twin OPC UA server running at opc.tcp://0.0.0.0:4841/gateway/")

twin = ConveyorTwin()

try:
    while True:
        # Simulate a random object arriving, random type, occasional E-stop
        twin.object_sensor = random.random() < 0.4
        twin.type_sensor = random.random() < 0.5
        twin.e_stop = random.random() < 0.02   # rare, occasional E-stop event

        twin.scan_cycle()

        count_a_var.set_value(twin.count_a)
        count_b_var.set_value(twin.count_b)
        enabled_var.set_value(twin.system_enabled)

        time.sleep(1)
finally:
    server.stop()
