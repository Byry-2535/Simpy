import getpass
import platform
import psutil
import shutil
import time
import wmi
from plyer import notification

c = wmi.WMI()

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

def get_arch():
    return f'Architecture: {platform.machine()}'

def get_device_type():
    try:
        for enclosure in c.Win32_SystemEnclosure():
            chassis = enclosure.ChassisTypes
            laptop_types = [8, 9, 10, 14]
            if any(t in chassis for t in laptop_types):
                return 'Device: Laptop'
        return 'Device: Desktop'
    except:
        return 'Device: Unknown'

def get_username():
    return getpass.getuser()

def dash_lines():
    lines = len(get_os_name()) + len(get_username()) + 4
    return '-' * lines

def get_cpu_specs():
    try:
        cpu = c.Win32_Processor()[0]
        name = cpu.Name.strip()
        return f'CPU: {name}'
    except:
        return 'CPU: Unknown'

def get_cpu_usage():
    usage = psutil.cpu_percent(interval=None)
    return f'{usage}%'

def get_cpu_cores():
    physical = psutil.cpu_count(logical=False)
    logical = psutil.cpu_count(logical=True)
    return f'Cores/Threads: {physical}C/{logical}T'

def get_gpu_specs():
    try:
        gpus = c.Win32_VideoController()
        if gpus:
            return f'GPU: {gpus[0].Name.strip()}'
        return 'GPU: Unknown'
    except:
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
    return f'Python: {platform.python_implementation()} {platform.python_version()}'

def get_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    h, rem = divmod(uptime_seconds, 3600)
    m, s = divmod(rem, 60)

    return f'Uptime: {h}h {m}m {s}s'

def ty_notif(username):
    return notification.notify(title=f'Thank You {username}!', message='for using my simple script.', timeout=1)

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
        get_arch(),
        get_device_type(),
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
        
    input('\nPress any key to exit...')

if __name__ == '__main__':
    print()
    main()
    ty_notif(get_username())