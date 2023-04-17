import psutil
import ctypes
import time
import subprocess
import datetime
process_name = "my_process.exe"
process_path = "C:\\Program Files\\MyApp\\my_process.exe"
process_rundir ="C:\\Program Files\\MyApp"

with open('config.txt', 'r') as f:
    content = f.read()
    print(content)
    ls = content.split('=')
    process_path = ls[1]  
    ls2 = ls[1].split('\\')
    process_name = ls2[-1]  
    ls3 = ls[1].split(process_name)
    process_rundir = ls3[0]
    print(process_rundir)

def get_pid(process_name):
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return proc.pid
    return None
    
def is_running(process_name):
    pid = get_pid(process_name)
    return pid is not None and psutil.pid_exists(pid)

def start_process(process_path):
    subprocess.Popen([process_path],cwd=process_rundir)

#取消控制台快速编辑模式
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

while(True):
    if not is_running(process_name):
         print("program died,restart...")
         start_process(process_path)
    time.sleep(5)
     # 获取当前时间
    now = datetime.datetime.now()
    # 格式化时间输出
    print("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("program is running...")