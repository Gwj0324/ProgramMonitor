# Windows监控程序

## 程序功能说明

1，在Windows系统下监控某个程序是否在运行，若不在运行，则拉起。
2，在Windows系统下监控某个程序是否未响应，若检测到未响应，则将程序杀死，重新拉起。

## 使用说明：

将dist目录下的ProgramMonitor文件夹拷贝到你的电脑上，然后编辑ProgramMonitor/config.txt文件，设置程序运行路径。
`isJudgeNotResponding=1`这里若将`isJudgeNotResponding`设置为1则会开启检测未响应功能，置为0则会关闭检测未响应功能。注意在末尾不要换行。

例如：
```
program_path=G:\NetReflash\dist\NetReflash\NetReflash.exe
isJudgeNotResponding=1
```

**注意：**

如果需要监控的程序要以管理员权限运行，则需要进行以下配置：

在win10系统，只要是图标右下角带盾牌标志的软件，加入系统的启动文件夹：如：C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp 里面，每次开机后都会启动失败！据说这个是win10出于系统安全考虑，加入了UAC，对系统管理员权限做了限制造成的。

解决方法：运行输入gpedit.msc打开组策略（家庭版没有组策略功能）

依次展开计算机配置-》Windows设置-》安全设置-》本地策略-》安全选项-》用户账户控制：以管理员批准模式运行所有管理员，设置为已禁用

## bug记录：

### 1,bug描述：点击控制台，会进快速编辑模式，按下按键，才会继续运行。

解决方法：代码中取消控制台快速编辑模式。

### 2,bug描述：配置文件无法存储中文路径

解决方法：以二进制格式读取配置文件，再以utf-8格式解析配置文件。
