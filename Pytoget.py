import shutil
import platform
import subprocess
from datetime import datetime

def get_os_name():
    os_name = platform.system()
    return os_name

def get_win_ver():
    os_release = platform.release()
    return os_release

def get_username():
    username = platform.node()
    return username

def dash_lines():
    lines = len(get_os_name()) + len(get_username())
    print('-'*lines + '\n')

def get_cpu_specs():
    cmd = [
        'powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_Processor).Name'
    ]

    cpu = subprocess.check_output(cmd).decode().strip()
    return f'CPU: {cpu}'

def get_gpu_specs():
    cmd = [
        'powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name)'
    ]

    gpu = subprocess.check_output(cmd).decode().strip()
    return f'GPU: {gpu}'

def get_storage(path='C:\\'):
    usage = shutil.disk_usage(path)
    total_gb = round(usage.total / (1024**3), 2)
    free_gb = round(usage.free / (1024**3), 2)

    return f'Storage: {free_gb}GB/{total_gb}GB'

def get_ram():
    cmd = [
        'powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize)'
    ]

    output = subprocess.check_output(cmd).decode().splitlines()
    free_kb = int(output[3].split()[0])
    total_kb = int(output[3].split()[1])
    total_gb = round(total_kb / 1024 / 1024, 2)
    free_gb = round(free_kb / 1024 / 1024, 2)

    return f'RAM: {free_gb}GB/{total_gb}GB'

def get_py_ver():
    python_version = platform.python_version()
    return f'Python Verson: {python_version}'

def get_uptime():
    t = subprocess.check_output([
        'powershell', '-NoProfile', '-Command', "(Get-CimInstance Win32_OperatingSystem).LastBootUpTime.ToString('yyyyMMddHHmmss')"
    ]).decode().strip()

    delta = datetime.now() - datetime.strptime(t, '%Y%m%d%H%M%S')
    h, rem = divmod(delta.seconds, 3600)
    m, s = divmod(rem, 60)
    h += delta.days * 24

    return f'Uptime: {h}:{m}:{s}'

def main():
    username = get_username()
    os_name = get_os_name()
    win_ver = get_win_ver()
    cpu = get_cpu_specs()
    gpu = get_gpu_specs()
    storage = get_storage()
    memory = get_ram()
    py_ver = get_py_ver()
    up_time = get_uptime()
    
    print(f'\n\n{os_name}@{username}')
    dash_lines()
    print(f'Username: {username}')
    print(f'OS: {os_name} {win_ver}')
    print(cpu)
    print(gpu)
    print(storage)
    print(memory)
    print(py_ver)
    print(up_time)
    print()
    
    while True:
        command = input(f'Pytoget.{os_name} >> ')
        if command == 'q':
            print('Thenkyow!!!')
            quit()
        print('Invalid Command!')
        continue

if __name__ == '__main__':
    main()