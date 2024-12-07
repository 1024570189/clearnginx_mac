#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

def clear_screen():
    """清理屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def list_nginx_processes():
    """查看所有运行中的 Nginx 进程，并返回进程列表"""
    try:
        # 修改进程查找命令，避免管道符号导致的语法错误
        cmd = "ps aux | grep nginx"
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True, 
                              shell=True)
        
        processes = [line for line in result.stdout.split('\n') 
                    if 'nginx' in line and 'grep nginx' not in line]
        
        if processes:
            print("\n当前运行的 Nginx 进程列表：")
            print("-" * 80)
            for process in processes:
                # 提取并显示进程信息
                parts = process.split()
                if len(parts) >= 2:
                    pid = parts[1]
                    print(f"PID: {pid} - {process}")
        else:
            print("\n未发现正在运行的 Nginx 进程")
            
        return processes
    except Exception as e:
        print(f"\n发生错误：{str(e)}")
        return []

def get_sudo_permission():
    """获取 sudo 权限"""
    try:
        print("\n需要获取管理员权限来执行操作...")
        subprocess.run(['sudo', '-v'], check=True)
        return True
    except subprocess.CalledProcessError:
        print("\n获取管理员权限失败，请确保您有 sudo 权限")
        return False

def kill_nginx_by_pid():
    """根据用户输入的进程号关闭指定的 Nginx 进程"""
    processes = list_nginx_processes()
    if not processes:
        input("\n按回车键继续...")
        return
    
    # 获取 sudo 权限
    if not get_sudo_permission():
        input("\n按回车键继续...")
        return
    
    try:
        pid = input("\n请输入要关闭的进程号 (PID): ")
        if not pid.strip():
            return
            
        print(f"\n正在关闭进程号为 {pid} 的 Nginx 进程...")
        subprocess.run(['sudo', 'kill', '-9', pid], check=True)
        print(f"进程 {pid} 已关闭")
    except subprocess.CalledProcessError:
        print(f"关闭进程失败，请检查进程号是否存在")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    
    input("\n按回车键继续...")

def kill_all_nginx():
    """关闭所有 Nginx 进程"""
    # 首先检查是否有运行的 nginx 进程
    processes = list_nginx_processes()
    if not processes:
        print("\n当前没有运行的 Nginx 进程")
        input("\n按回车键继续...")
        return
        
    # 获取 sudo 权限
    if not get_sudo_permission():
        input("\n按回车键继续...")
        return
        
    try:
        print("\n正在关闭所有 Nginx 进程...")
        # 使用 pkill 命令
        subprocess.run(['sudo', 'pkill', '-9', 'nginx'], check=True)
        print("所有 Nginx 进程已关闭")
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            print("\n没有找到任何 Nginx 进程")
        else:
            print("\n关闭进程失败，请检查权限或进程状态")
    except Exception as e:
        print(f"\n发生错误：{str(e)}")
    
    input("\n按回车键继续...")

def main():
    """主函数"""
    while True:
        clear_screen()
        print("=== Nginx 进程管理工具 ===")
        print("\n1. 查看所有 Nginx 进程")
        print("2. 关闭指定进程")
        print("3. 关闭所有进程")
        print("4. 退出程序")
        
        choice = input("\n请输入选项 (1-4): ").strip()
        
        if choice == '1':
            list_nginx_processes()
            input("\n按回车键继续操作...")
        elif choice == '2':
            kill_nginx_by_pid()
        elif choice == '3':
            kill_all_nginx()
        elif choice == '4':
            print("\n感谢使用，再见～～")
            sys.exit(0)
        else:
            print("\n无效的选项，请重新选择")
            input("\n按回车键继续...")

if __name__ == "__main__":
    main()