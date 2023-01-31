import psutil
import os 
import time
try:
    while True:
        proc = psutil.process_iter()
        for process in proc:
            try:
                if process.children():
                    print(f"Detected: {process.name()} (PID: {process.pid})")
                IP = process.connections()
                for conn in IP:
                    if conn.raddr:
                        print(f"IP: {conn.raddr[0]}:{conn.raddr[1]}")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
        time.sleep(5)
except KeyboardInterrupt:
    print("Stoping now!")
