# Nginx 进程管理工具

## 简介
这是一个专门为 Mac 系统设计的 Nginx 进程管理工具，可以帮助你方便地查看和管理系统中的 Nginx 进程。本工具提供了进程查看、启动、停止、重启等核心功能。

## 系统要求

### 操作系统
- macOS 10.x 或更高版本

### Python 环境
- Python 3.6 或更高版本
- 可以通过以下命令检查 Python 版本：
```bash
python3 --version
```

## 安装说明
1. 克隆或下载本项目到本地
2. 确保系统已安装 Python 3.6 或更高版本
3. 确保已安装 Nginx

## 使用方法

### 启动工具
由于需要管理系统进程，请使用 sudo 权限运行：
```bash
sudo python3 nginx_manager.py
```

### 主要功能
工具启动后，你可以使用以下命令：

1. 查看 Nginx 进程状态
   - 输入: `status`
   - 功能: 显示当前所有 Nginx 相关进程

2. 启动 Nginx
   - 输入: `start`
   - 功能: 启动 Nginx 服务

3. 停止 Nginx
   - 输入: `stop`
   - 功能: 停止所有 Nginx 进程

4. 重启 Nginx
   - 输入: `restart`
   - 功能: 重启 Nginx 服务

5. 退出程序
   - 输入: `quit` 或 `exit`
   - 功能: 安全退出管理工具

## 常见问题

### 1. 权限不足
问题：运行时提示权限不足
解决：使用 sudo 运行程
```bash
sudo python3 nginx_manager.py
```

### 2. Python 版本错误
问题：提示 Python 版本不支持
解决：安装或升级到 Python 3.6 或更高版本

### 3. Nginx 未安装
问题：提示找不到 Nginx
解决：通过 Homebrew 安装 Nginx
```bash
brew install nginx
```

## 注意事项
- 请确保使用 sudo 权限运行
- 使用前请确认 Nginx 已正确安装
- 建议在操作前备份重要的 Nginx 配置文件

## 技术支持
如遇到问题，请提交 Issue 或发送邮件至：[1024570189@qq.com]

## 许可证
MIT License

