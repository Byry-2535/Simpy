import cpuinfo
import getpass
import multiprocessing
import platform
import psutil
import time

asciimoji = [
"         ",
"         ",
"         ",
"  /\\_/\\  ",
" ( o.o ) ",
"  > ^ <  "
]

def get_os():
    return platform.system()

def get_kernel():
    return platform.release()

def get_arch():
    return platform.machine()

def get_username():
    return getpass.getuser()

def dash_lines():
    lines = len(get_os()) + len(get_username()) + 4
    return f'{'-' * lines}\n'

def get_cpu():
    cpu = cpuinfo.get_cpu_info()
    return cpu['brand_raw']

def get_cpu_usage():
    usage = psutil.cpu_percent(interval=None)
    return f'{usage}%'

def get_storage():
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        total = round(usage.total / (1024**3), 2)
        used = round(psutil.disk_usage(partition.mountpoint).used / (1024**3), 2)
        percent = usage.percent
        return f'{used} GB / {total} GB ({percent}%)'

def get_memory():
    mem = psutil.virtual_memory()
    total = round(mem.total / (1024**3), 2)
    used = round(mem.used / (1024**3), 2)
    percent = mem.percent
    return f'{used} GB / {total} GB ({percent}%)'

def get_battery():
    batt = psutil.sensors_battery()
    if batt:
        return f'{batt.percent:.0f}%'
    return 'Not Present'

def get_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    h, rem = divmod(uptime_seconds, 3600)
    m, s = divmod(rem, 60)
    return f'{h}h {m}m {s}s'

def main():
    start = time.perf_counter()
    username = get_username()
    os_name = get_os()

    info = [
        f'{os_name}@{username}',
        dash_lines(),
        f'Username: {username}',
        f'OS: {os_name} {get_kernel()}',
        f'Architecture: {get_arch()}',
        f'CPU: {get_cpu()} ({get_cpu_usage()})',
        f'Storage: {get_storage()}',
        f'Memory: {get_memory()}',
        f'Battery: {get_battery()}',
        f'Uptime: {get_uptime()}'
    ]

    max_len = max(len(asciimoji), len(info))

    for i in range(max_len):
        left = asciimoji[i] if i < len(asciimoji) else ' ' * 9
        right = info[i] if i < len(info) else ''
        print(f"{left}  {right}")

    end = time.perf_counter()
    print(f'\n{end - start:.2f} seconds.')
    getpass.getpass('Press enter key to exit...')

if __name__ == '__main__':
    multiprocessing.freeze_support()
    print()
    main()