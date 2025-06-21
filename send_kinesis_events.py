# Simulate sending random traffic events to Kinesis stream
import json
import random
import time
import subprocess

STREAM_NAME = "Traffic-Stream"
sensor_types = ["loop_detector", "camera", "radar"]
locations = ["Sydney-GeorgeSt-5", "Sydney-PittSt-2", "Sydney-KentSt-9"]
incident_types = ["accident", "construction", "none", "breakdown"]

for i in range(10):
    payload = {
        "eventId": 100 + i,
        "sensorType": random.choice(sensor_types),
        "location": random.choice(locations),
        "eventTime": "2025-05-30T14:00:{:02d}Z".format(i),
        "trafficSpeed": random.randint(20, 80),
        "congestionLevel": random.randint(1, 5),
        "incidentType": random.choice(incident_types),
        "vehicleCount": random.randint(5, 30),
        "avgVehicleLength": round(random.uniform(3.0, 6.0), 1),
        "weatherCondition": random.choice(["clear", "rain", "fog"]),
        "temperature": random.randint(10, 30),
        "laneClosed": random.choice([True, False]),
        "reportedBy": "city_traffic_monitor"
    }

    command = [
        "aws", "kinesis", "put-record",
        "--stream-name", STREAM_NAME,
        "--partition-key", "sensor1",
        "--data", json.dumps(payload),
        "--cli-binary-format", "raw-in-base64-out"
    ]

    print(f"Sending event {i+1}...")
    subprocess.run(command)
    time.sleep(1)
