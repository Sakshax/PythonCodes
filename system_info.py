import platform
import psutil

def get_system_info():
    # Get basic system information
    system = platform.system()
    node_name = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()

    print("==== System Information ====")
    print(f"Operating System : {system}")
    print(f"Computer Name    : {node_name}")
    print(f"OS Release       : {release}")
    print(f"OS Version       : {version}")
    print(f"Machine Type     : {machine}")
    print(f"Processor        : {processor}")
    print()

def get_memory_info():
    # Get RAM information
    memory = psutil.virtual_memory()
    total = memory.total / (1024 ** 3)
    available = memory.available / (1024 ** 3)
    used = memory.used / (1024 ** 3)
    percent = memory.percent

    print("==== Memory (RAM) Information ====")
    print(f"Total     : {total:.2f} GB")
    print(f"Available : {available:.2f} GB")
    print(f"Used      : {used:.2f} GB")
    print(f"Usage     : {percent}%")
    print()

def get_cpu_info():
    # Get CPU information
    print("==== CPU Information ====")
    print(f"Physical cores   : {psutil.cpu_count(logical=False)}")
    print(f"Total cores      : {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency    : {psutil.cpu_freq().current:.2f} MHz")
    print(f"CPU Usage Per Core:")
    
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i + 1} : {percentage}%")
    
    print(f"Total CPU Usage  : {psutil.cpu_percent()}%")
    print()

if __name__ == "__main__":
    get_system_info()
    get_memory_info()
    get_cpu_info()
