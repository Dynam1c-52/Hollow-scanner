import psutil
import os 
import time
try:
    while True:
        proc = psutil.process_iter()
        for process in proc:
            try:
                mem = process.memory_maps()
                for mem in mem:
                    if mem.path:
                     print(f"Detected! {process.name()} (PID: {process.pid})")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
        time.sleep(5)
except KeyboardInterrupt:
    print("Stoping now!")
                