import psutil
import ctypes
import time
import subprocess
import datetime
import os
process_name = "my_process.exe"
process_path = "C:\\Program Files\\MyApp\\my_process.exe"
process_rundir ="C:\\Program Files\\MyApp"
isJudgeNotResponding="1"
# 获取当前 .exe 文件所在路径
exe_path = os.path.dirname(os.path.abspath(__file__))
print(".exe 文件所在路径为：", exe_path)

with open(exe_path+'\\config.txt', 'rb') as f:
    content = f.readline().decode('utf-8')
    print(content)
    content = content.replace("\r\n","")
    ls = content.split('=')
    process_path = ls[1]  
    ls2 = ls[1].split('\\')
    process_name = ls2[-1]  
    ls3 = ls[1].split(process_name)
    process_rundir = ls3[0]
    print(process_rundir)
    content2 = f.readline().decode('utf-8')
    print(content2)
    ls4 = content2.split('=')
    isJudgeNotResponding = ls4[1]

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

def is_responding(process_name):
    # 要执行的命令
    cmd = 'tasklist /fi "STATUS eq Not Responding" /fi "imagename eq '+process_name +'" /fo csv'    
    # 执行命令，捕获输出结果
    output = subprocess.check_output(cmd, shell=True)
    if process_name.encode() in output:
        return False
    else:
        return True
    
def kill_process(process_name):
    cmd = 'taskkill /f /im '+process_name
    os.system(cmd)

#取消控制台快速编辑模式
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

while(True):
    if not is_running(process_name):
         print("program died,restart...")
         start_process(process_path)
    if isJudgeNotResponding == "1" and not is_responding(process_name):
        time.sleep(5)
        if not is_responding(process_name):
            print("program not responding,restart...")
            kill_process(process_name)
            start_process(process_path)
    time.sleep(5)
     # 获取当前时间
    now = datetime.datetime.now()
    # 格式化时间输出
    print("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("program is running...")