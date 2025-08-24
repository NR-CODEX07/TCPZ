import subprocess
import time
import sys

MAIN_SCRIPT = "v1.py"
DNS_SERVER = "8.8.8.8"  # ya "1.1.1.1"

def set_dns():
    try:
        print(f"[WATCHDOG] Setting DNS → {DNS_SERVER}")
        with open("/etc/resolv.conf", "w") as f:
            f.write(f"nameserver {DNS_SERVER}\n")
    except Exception as e:
        print(f"[WATCHDOG] DNS set error: {e}")

def run_script():
    while True:
        set_dns()
        print(f"[WATCHDOG] Starting {MAIN_SCRIPT} ...")
        process = subprocess.Popen([sys.executable, MAIN_SCRIPT])
        process.wait()

        if process.returncode == 0:
            print(f"[WATCHDOG] {MAIN_SCRIPT} exited normally.")
            break
        else:
            print(f"[WATCHDOG] {MAIN_SCRIPT} crashed (code {process.returncode}). Restarting in 5s...")
            time.sleep(5)

if __name__ == "__main__":
    run_script()