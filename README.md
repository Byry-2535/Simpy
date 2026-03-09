# Simpy 🐱‍💻

## A Simple Python Script inspired by neofetch and fastfetch

**Simpy** is a lightweight Python script that displays your system’s specifications, including CPU, GPU, RAM, storage, network, battery, Python version, and uptime with a fun ASCII art cat!  

---

## What It Does

It uses Python modules such as **psutil**, **platform**, **shutil**, **cpuinfo**, and **GPUtil** to gather and display your system information in a clean, readable format.

**Features include:**  

- CPU brand, cores, and usage  
- GPU info (if available)  
- RAM usage and disk storage  
- Active network interfaces  
- Battery percentage (if present)  
- Python version and system uptime  
- Cute ASCII art display  

---

## How to Use It

1. Make sure **Python 3.6+** is installed on your device.  
2. Install required packages via pip:

```bash
pip install py-cpuinfo GPUtil psutil
```

3. Download the `simpy.py` file and save it locally.
4. Run the script:

```bash
python simpy.py
```

5. Wait a few seconds for the system information to load.

---

## Sample Output

![My Laptop Specs](./images/sample.png)

---

## Notes

For `windows` system currently. This is a hobby project and is still being improved. You can customize:

- The `asciimoji` list for different ASCII art
- The storage path in `get_storage(path='C:\\')`
- Tinker on it

---

## Thank You!

Enjoy checking your system specs with a fun and simple Python script! 😸