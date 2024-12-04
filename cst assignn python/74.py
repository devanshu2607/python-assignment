##74.	Create a system for monitoring server performance metrics and notifying on anomalies.

import psutil
import smtplib
from time import sleep

def send_alert(subject, message):
    server = smtplib.SMTP("smtp.example.com", 587)  # Replace with your SMTP server
    server.starttls()
    server.login("your_email@example.com", "your_password")
    server.sendmail("your_email@example.com", "recipient@example.com",f"Subject: {subject}\n\n{message}")
    server.quit()

def monitor_server(threshold=80):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            send_alert("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%!")
        sleep(5)

# Example usage
monitor_server()