##78.	Create a simulation of a simple traffic light system.

import time

# Function to simulate the traffic light system
def traffic_light():
    lights = ["Red","Green","Yellow"]
    durations = [5, 4, 2]  # Duration in seconds for each light

    while True:
        for light, duration in zip(lights, durations):
            print(f"The light is now {light}")
            time.sleep(duration)  # Wait for the duration of the current light

# Run the traffic light simulation
traffic_light()

