#!/usr/bin/env python3
import time
from anybar import AnyBar
from ping3 import ping

AnyBar(port=1738).change('black')

def check_ping(host='google.com'):
    try:
        result = ping(host, timeout=2)
        if result is not None:
            return True, result * 1000  # Convert to milliseconds
        else:
            return False, None
    except Exception:
        return False, None

print("Launching the AnyBar script")

while True:
    success, duration = check_ping()
    if success:
        print(f"CONNECTED: Host replied in {duration:.2f} ms")
        AnyBar().change('green')
    else:
        print("Timeout")
        AnyBar().change('red')
    time.sleep(5)