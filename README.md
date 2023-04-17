# Windows监控程序

## 程序功能说明

在Windows系统下监控某个程序是否在运行，若不在运行，则拉起

## 使用说明：

将dist目录下的ProgramMonitor文件夹拷贝到你的电脑上，然后编辑ProgramMonitor/config.txt文件，设置程序运行路径。注意在末尾不要换行。

例如：
```
program_path=G:\NetReflash\dist\NetReflash\NetReflash.exe
```

## bug记录：

bug描述：点击控制台，会进快速编辑模式，按下按键，才会继续运行。
解决方法：代码中取消控制台快速编辑模式。