#!/usr/bin/env python3
import time
import requests
from anybar import AnyBar

AnyBar(port=1738).change('black')

def check_internet_connection(url='http://www.google.com/', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return True, response.elapsed.total_seconds() * 1000  # Convert to milliseconds
    except (requests.ConnectionError, requests.Timeout):
        return False, None

print("Launching the AnyBar script")

while True:
    success, duration = check_internet_connection()
    if success:
        print(f"CONNECTED: Host replied in {duration:.2f} ms")
        AnyBar().change('green')
    else:
        print("Timeout")
        AnyBar().change('red')
    time.sleep(5)
