import cpuinfo
import GPUtil
import platform
import psutil
import shutil
import time

asciimoji = [
"         ",
"         ",
"         ",
"  /\\_/\\  ",
" ( o.o ) ",
"  > ^ <  "
]

def get_os_name():
    return platform.system()

def get_win_ver():
    return platform.release()

def get_username():
    return platform.node()

def dash_lines():
    lines = len(get_os_name()) + len(get_username()) + 4
    return '-' * lines

def get_cpu_specs():
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    return f'CPU: {cpu}'

def get_cpu_cores():
    physical = psutil.cpu_count(logical=False)
    logical = psutil.cpu_count(logical=True)
    return f'Cores: {physical}C/{logical}T'

def get_cpu_usage():
    usage = psutil.cpu_percent(interval=0.5)
    return f'{usage}%'

def get_gpu_specs():
    gpu = GPUtil.getGPUs()
    if gpu:
        return f'GPU: {gpu[0].name}'
    return 'GPU: Unknown'

def get_storage(path='C:\\'):
    usage = shutil.disk_usage(path)
    total_gb = round(usage.total / (1024**3), 2)
    used_gb = round((usage.total - usage.free) / (1024**3), 2)
    used_percentage = round((used_gb / total_gb) * 100, 2)
    return f'Storage: {used_gb}GB/{total_gb}GB ({used_percentage}%)'

def get_ram():
    mem = psutil.virtual_memory()
    used = round(mem.used / (1024**3), 2)
    total = round(mem.total / (1024**3), 2)
    percent = mem.percent
    return f'Memory: {used}GB/{total}GB ({percent}%)'

def get_network():
    stats = psutil.net_if_stats()
    active = [name for name, val in stats.items() if val.isup]
    return f"Network: {', '.join(active)}"

def get_battery():
    batt = psutil.sensors_battery()
    if batt:
        return f'Battery: {batt.percent}%'
    return 'Battery: Not Present'

def get_py_ver():
    return f'Python Version: {platform.python_version()}'

def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    h, rem = divmod(int(uptime_seconds), 3600)
    m, s = divmod(rem, 60)
    return f'Uptime: {h}:{m}:{s}'

def main():
    username = get_username()
    os_name = get_os_name()
    win_ver = get_win_ver()

    info = [
        f'{os_name}@{username}',
        dash_lines(),
        '',
        f'Username: {username}',
        f'OS: {os_name} {win_ver}',
        f'{get_cpu_specs()} ({get_cpu_usage()})',
        get_cpu_cores(),
        get_gpu_specs(),
        get_storage(),
        get_ram(),
        get_network(),
        get_battery(),
        get_py_ver(),
        get_uptime()
    ]

    max_len = max(len(asciimoji), len(info))

    for i in range(max_len):
        left = asciimoji[i] if i < len(asciimoji) else ' ' * 9
        right = info[i] if i < len(info) else ''
        print(f"{left}  {right}")

if __name__ == '__main__':
    print()
    main()
    print()