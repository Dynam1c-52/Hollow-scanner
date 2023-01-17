#https://t.me/PPI_LAB
import psutil
import os 
import time

try:
    while True:
        processes = psutil.process_iter()
        for process in processes:
            try:
                memory_maps = process.memory_maps()
                for memory_map in memory_maps:
                    if memory_map.path:
                       
                            print(f"Detected!!! {process.name()} (PID: {process.pid})")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
        time.sleep(5)
except KeyboardInterrupt:
    print("Stoping now!")