from datetime import datetime
import os
import platform
import shutil
import subprocess

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
    lines = len(get_os_name()) + len(get_username()) + 4
    return '-' * lines

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
    used_gb = round((usage.total - usage.free) / (1024**3), 2)
    used_percentage = round((used_gb / total_gb) * 100, 2)

    return f'Storage: {used_gb}GB/{total_gb}GB ({used_percentage}%)'

def get_ram():
    cmd = [
        'powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize)'
    ]

    output = subprocess.check_output(cmd).decode().splitlines()
    free_kb = int(output[3].split()[0])
    total_kb = int(output[3].split()[1])
    total_gb = round(total_kb / 1024 / 1024, 2)
    free_gb = round(free_kb / 1024 / 1024, 2)
    used_gb = round(total_gb - free_gb, 2)
    used_percentage = round((used_gb / total_gb) * 100, 2)

    return f'RAM: {used_gb}GB/{total_gb}GB ({used_percentage}%)'

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

asciimoji = """
      /\\_/\\  
     ( o.o ) 
      > ^ <  
"""
username = get_username()
os_name = get_os_name()
win_ver = get_win_ver()
cpu = get_cpu_specs()
gpu = get_gpu_specs()
storage = get_storage()
memory = get_ram()
py_ver = get_py_ver()
up_time = get_uptime()

def get_cpu_specs_deep():
    cmd = [
        'powershell', '-NoProfile', '-Command', '''
            $cpu = Get-CimInstance Win32_Processor
            [PSCustomObject]@{
                Name = $cpu.Name
                Cores = $cpu.NumberOfCores
                Threads = $cpu.NumberOfLogicalProcessors
                Frequency = $cpu.MaxClockSpeed
            }
        '''
    ]
    
    cpu_info = subprocess.check_output(cmd).decode().strip()
    return cpu_info

def get_gpu_specs_deep():
    cmd = [
        'powershell', '-NoProfile', '-Command', '''
            $gpu = Get-CimInstance Win32_VideoController
            [PSCustomObject]@{
                Name = $gpu.Name
                Memory = $gpu.AdapterRAM / 1MB
                DriverVersion = $gpu.DriverVersion
            }
        '''
    ]
    
    gpu_info = subprocess.check_output(cmd).decode().strip()
    return gpu_info

def get_ram_deep():
    cmd_usage = [
        'powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize)'
    ]
    
    output_usage = subprocess.check_output(cmd_usage).decode().splitlines()
    free_kb = int(output_usage[3].split()[0])
    total_kb = int(output_usage[3].split()[1])
    total_gb = round(total_kb / 1024 / 1024, 2)
    free_gb = round(free_kb / 1024 / 1024, 2)
    used_gb = round(total_gb - free_gb, 2)
    used_percentage = round((used_gb / total_gb) * 100, 2)

    cmd_specs = [
        'powershell', '-NoProfile', '-Command', '''
            $ram = Get-CimInstance Win32_PhysicalMemory
            $ramInfo = $ram | Select-Object Capacity, Speed, MemoryType, Manufacturer, SlotDesignation
            $ramInfo | ForEach-Object {
                "Slot: $($_.SlotDesignation), Capacity: $( [math]::round($_.Capacity / 1GB, 2) ) GB, Speed: $($_.Speed) MHz, Type: $($_.MemoryType)"
            }
        '''
    ]
    
    ram_info = subprocess.check_output(cmd_specs).decode().strip()
    return f'RAM Usage: {used_gb}GB/{total_gb}GB ({used_percentage}%)\nRAM Details:\n{ram_info}'

pytoget = 'Pytoget'
pytoget_ver = '0.2'
cpu_full = get_cpu_specs_deep()
gpu_full = get_gpu_specs_deep()
ram_full = get_ram_deep()

def run():
    print(asciimoji, end="  ")
    system_info = (
        f'{os_name}@{username}\n'
        f'{dash_lines()}\n'
        f'Username: {username}\n'
        f'OS: {os_name} {win_ver}\n'
        f'{cpu}\n'
        f'{gpu}\n'
        f'{storage}\n'
        f'{memory}\n'
        f'{py_ver}\n'
        f'{up_time}\n'
    )
    print(system_info)

def main():
    run()
    while True:
        command = input(f'{pytoget}.{username} >> ').lower()
        if command in ['q', 'quit', 'exit']:
            quit()
        elif command == 'pytoget' or command == 'ptg':
            run()
        elif command == 'pytoget -v' or command == 'ptg -v':
            print(f'\n{pytoget} Version: {py_ver}\n')
        elif command == 'cls':
             os.system('cls')
        elif command == 'cpu':
            print(f'\n{cpu_full}\n')
        elif command == 'gpu':
            print(f'\n{gpu_full}\n')
        elif command == 'rom':
            print(f'\n{storage}\n')
        elif command == 'ram':
            print(f'\n{ram_full}\n')
        else:
            print('Invalid Command!')

if __name__ == '__main__':
    main()