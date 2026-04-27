import multiprocessing
import random
import time


from datetime import datetime

def worker():
    sleep_time = random.random()
    time.sleep(sleep_time)
    current_time = datetime.now().strftime("%H:%M:%S.%f")
    
    process_name = multiprocessing.current_process().name
    print(f"{process_name} Woke Up then Exited: {current_time} (Time Slept: {sleep_time:.2f}s)")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f"Process-{i+1}")
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()