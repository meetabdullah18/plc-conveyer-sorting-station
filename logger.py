import csv
import time
from datetime import datetime
from opcua import Client

client = Client("opc.tcp://localhost:4841/gateway/")
client.connect()

count_a_node = client.get_node("ns=2;i=2")
count_b_node = client.get_node("ns=2;i=3")
enabled_node = client.get_node("ns=2;i=4")

try:
    with open("conveyor_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        while True:
            writer.writerow([
                datetime.now().isoformat(),
                count_a_node.get_value(),
                count_b_node.get_value(),
                enabled_node.get_value()
            ])
            f.flush()
            time.sleep(2)
finally:
    client.disconnect()
