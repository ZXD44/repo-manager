#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Repository & Release Manager - Simple GUI Tool
"""

import os
import sys
import subprocess
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from datetime import datetime
import threading
import webbrowser

# ตรวจสอบและติดตั้ง requests
try:
    import requests
except ImportError:
    print("กำลังติดตั้ง requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

class RepoManagerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Repository & Release Manager")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # ตัวแปร
        self.project_path = tk.StringVar(value=os.getcwd())
        self.github_token = tk.StringVar(value=os.getenv('GITHUB_TOKEN', ''))
        self.repo_owner = tk.StringVar()
        self.repo_name = tk.StringVar()
        
        self.setup_ui()
        self.load_repo_info()
        
    def setup_ui(self):
        """สร้าง UI"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        tk.Label(title_frame, text="🚀 Repository & Release Manager", 
                font=('Arial', 16, 'bold'), fg='white', bg='#2c3e50').pack(pady=15)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Settings
        settings_frame = tk.LabelFrame(main_frame, text="การตั้งค่า", font=('Arial', 11, 'bold'))
        settings_frame.pack(fill='x', pady=(0, 10))
        
        # Project path
        tk.Label(settings_frame, text="โฟลเดอร์โปรเจค:").grid(row=0, column=0, sticky='w', padx=10, pady=8)
        path_frame = tk.Frame(settings_frame)
        path_frame.grid(row=0, column=1, sticky='ew', padx=10, pady=8)
        settings_frame.columnconfigure(1, weight=1)
        
        self.path_entry = tk.Entry(path_frame, textvariable=self.project_path, width=60)
        self.path_entry.pack(side='left', fill='x', expand=True)
        tk.Button(path_frame, text="เลือก", command=self.browse_folder).pack(side='right', padx=(5,0))
        
        # GitHub token
        tk.Label(settings_frame, text="GitHub Token:").grid(row=1, column=0, sticky='w', padx=10, pady=8)
        token_frame = tk.Frame(settings_frame)
        token_frame.grid(row=1, column=1, sticky='ew', padx=10, pady=8)
        
        self.token_entry = tk.Entry(token_frame, textvariable=self.github_token, show='*', width=50)
        self.token_entry.pack(side='left', fill='x', expand=True)
        tk.Button(token_frame, text="ช่วยเหลือ", command=self.show_token_help).pack(side='right', padx=(5,0))
        
        # Repository info
        tk.Label(settings_frame, text="Owner:").grid(row=2, column=0, sticky='w', padx=10, pady=8)
        tk.Entry(settings_frame, textvariable=self.repo_owner, width=30).grid(row=2, column=1, sticky='w', padx=10, pady=8)
        
        tk.Label(settings_frame, text="Repository:").grid(row=3, column=0, sticky='w', padx=10, pady=8)
        tk.Entry(settings_frame, textvariable=self.repo_name, width=30).grid(row=3, column=1, sticky='w', padx=10, pady=8)
        
        # Buttons
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=10)
        
        tk.Button(btn_frame, text="📤 Push ไฟล์", command=self.push_files, 
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🎯 สร้าง Release", command=self.create_release, 
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🚀 ทำทั้งหมด", command=self.do_all, 
                 bg='#9b59b6', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔄 รีเฟรช", command=self.refresh_info, 
                 bg='#34495e', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="📋 ดู Releases", command=self.view_releases, 
                 bg='#16a085', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔍 ตรวจสอบ", command=self.check_setup, 
                 bg='#f39c12', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=2).pack(side='left', padx=5)
        
        # Second row of buttons
        btn_frame2 = tk.Frame(main_frame)
        btn_frame2.pack(fill='x', pady=5)
        
        tk.Button(btn_frame2, text="🔧 แก้ไข Remote", command=self.fix_remote_manual, 
                 bg='#e67e22', fg='white', font=('Arial', 10, 'bold'), 
                 width=12, height=1).pack(side='left', padx=5)
        
        # Log
        log_frame = tk.LabelFrame(main_frame, text="Log", font=('Arial', 11, 'bold'))
        log_frame.pack(fill='both', expand=True, pady=(10, 0))
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, 
                                                 bg='#2c3e50', fg='#ecf0f1', 
                                                 font=('Consolas', 9))
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Status
        self.status_var = tk.StringVar(value="พร้อมใช้งาน")
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                            relief='sunken', anchor='w')
        status_bar.pack(side='bottom', fill='x')
        
    def log(self, message):
        """เพิ่มข้อความใน log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert('end', f"[{timestamp}] {message}\n")
        self.log_text.see('end')
        self.root.update()
        
    def run_command(self, command, cwd=None, check_error=True):
        """รันคำสั่ง"""
        if cwd is None:
            cwd = self.project_path.get()
            
        self.log(f"รันคำสั่ง: {command}")
        
        try:
            result = subprocess.run(command, shell=True, cwd=cwd, 
                                  capture_output=True, text=True, 
                                  check=check_error, encoding='utf-8')
            if result.stdout.strip():
                self.log(f"✅ {result.stdout.strip()}")
            if result.stderr.strip() and not check_error:
                self.log(f"⚠️ {result.stderr.strip()}")
            return result
        except subprocess.CalledProcessError as e:
            self.log(f"❌ ข้อผิดพลาด: {e}")
            if e.stderr:
                self.log(f"❌ {e.stderr.strip()}")
            return None
        except Exception as e:
            self.log(f"❌ ข้อผิดพลาด: {e}")
            return None
            
    def browse_folder(self):
        """เลือกโฟลเดอร์"""
        folder = filedialog.askdirectory(initialdir=self.project_path.get())
        if folder:
            self.project_path.set(folder)
            self.load_repo_info()
            
    def load_repo_info(self):
        """โหลดข้อมูล repository"""
        try:
            project_dir = self.project_path.get()
            if not os.path.exists(project_dir):
                return
                
            os.chdir(project_dir)
            result = subprocess.run('git remote get-url origin', shell=True, 
                                  capture_output=True, text=True)
            
            if result.returncode == 0 and result.stdout:
                url = result.stdout.strip()
                self.log(f"พบ remote URL: {url}")
                
                if 'github.com' in url:
                    if url.startswith('https://'):
                        parts = url.replace('https://github.com/', '').replace('.git', '').split('/')
                    elif url.startswith('git@'):
                        parts = url.replace('git@github.com:', '').replace('.git', '').split('/')
                    
                    if len(parts) >= 2:
                        self.repo_owner.set(parts[0])
                        self.repo_name.set(parts[1])
                        self.log(f"📁 Repository: {parts[0]}/{parts[1]}")
        except Exception as e:
            self.log(f"ไม่สามารถโหลดข้อมูล repo: {e}")
            
    def show_token_help(self):
        """แสดงวิธีสร้าง token"""
        help_text = """วิธีสร้าง GitHub Personal Access Token:

1. ไปที่ GitHub.com → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. เลือก scopes: repo, workflow
5. Copy token มาใส่ในช่อง"""
        
        messagebox.showinfo("ช่วยเหลือ", help_text)
        webbrowser.open("https://github.com/settings/tokens")
        
    def check_git_config(self):
        """ตรวจสอบ git config"""
        try:
            name_result = self.run_command('git config user.name', check_error=False)
            email_result = self.run_command('git config user.email', check_error=False)
            
            if not name_result or not name_result.stdout.strip():
                self.log("⚠️ ไม่พบ git user.name")
                name = messagebox.askstring("Git Config", "ใส่ชื่อผู้ใช้ Git:")
                if name:
                    self.run_command(f'git config user.name "{name}"')
                    
            if not email_result or not email_result.stdout.strip():
                self.log("⚠️ ไม่พบ git user.email")
                email = messagebox.askstring("Git Config", "ใส่อีเมล Git:")
                if email:
                    self.run_command(f'git config user.email "{email}"')
                    
        except Exception as e:
            self.log(f"ข้อผิดพลาดในการตรวจสอบ git config: {e}")

    def check_repository_exists(self):
        """ตรวจสอบว่า repository มีอยู่จริง"""
        if not self.github_token.get() or not self.repo_owner.get() or not self.repo_name.get():
            return False
            
        try:
            url = f"https://api.github.com/repos/{self.repo_owner.get()}/{self.repo_name.get()}"
            headers = {'Authorization': f'token {self.github_token.get()}'}
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                self.log("✅ Repository พบแล้ว")
                return True
            elif response.status_code == 404:
                self.log("❌ Repository ไม่พบ")
                create = messagebox.askyesno("Repository ไม่พบ", 
                    f"Repository {self.repo_owner.get()}/{self.repo_name.get()} ไม่พบ\n"
                    "ต้องการสร้าง repository ใหม่หรือไม่?")
                if create:
                    return self.create_repository()
                return False
            else:
                self.log(f"❌ ข้อผิดพลาดในการตรวจสอบ repo: {response.status_code}")
                return False
                
        except Exception as e:
            self.log(f"❌ ข้อผิดพลาด: {e}")
            return False

    def create_repository(self):
        """สร้าง repository ใหม่"""
        try:
            self.log("🔨 กำลังสร้าง repository...")
            
            url = "https://api.github.com/user/repos"
            headers = {
                'Authorization': f'token {self.github_token.get()}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            data = {
                'name': self.repo_name.get(),
                'description': f"Repository created by Repo Manager",
                'private': False,
                'auto_init': True  # สร้าง README.md อัตโนมัติ
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 201:
                self.log("✅ สร้าง repository สำเร็จ!")
                
                # รอให้ repository พร้อมใช้งาน
                self.log("⏳ รอ repository พร้อมใช้งาน...")
                import time
                time.sleep(3)
                
                # ตรวจสอบว่า repository พร้อมใช้งานแล้ว
                check_url = f"https://api.github.com/repos/{self.repo_owner.get()}/{self.repo_name.get()}"
                for i in range(5):  # ลองตรวจสอบ 5 ครั้ง
                    check_response = requests.get(check_url, headers=headers)
                    if check_response.status_code == 200:
                        self.log("✅ Repository พร้อมใช้งาน!")
                        return True
                    time.sleep(1)
                
                self.log("⚠️ Repository อาจยังไม่พร้อม แต่ลองดำเนินการต่อ")
                return True
            else:
                self.log(f"❌ ไม่สามารถสร้าง repository ได้: {response.status_code}")
                self.log(f"❌ {response.text}")
                return False
                
        except Exception as e:
            self.log(f"❌ ข้อผิดพลาด: {e}")
            return False

    def fix_remote_url(self):
        """แก้ไข remote URL"""
        try:
            # ลบ remote เก่า
            self.run_command('git remote remove origin', check_error=False)
            
            # เพิ่ม remote ใหม่
            repo_url = f"https://github.com/{self.repo_owner.get()}/{self.repo_name.get()}.git"
            self.run_command(f'git remote add origin {repo_url}')
            self.log(f"🔧 ตั้งค่า remote URL ใหม่: {repo_url}")
            
        except Exception as e:
            self.log(f"ข้อผิดพลาดในการแก้ไข remote: {e}")

    def push_files(self):
        """Push ไฟล์"""
        def push_thread():
            try:
                self.status_var.set("กำลัง push...")
                self.log("📤 เริ่ม push ไฟล์")
                
                project_dir = self.project_path.get()
                os.chdir(project_dir)
                
                # ตรวจสอบ git config
                self.check_git_config()
                
                # ตรวจสอบ repository
                repo_created = False
                if not self.check_repository_exists():
                    self.log("❌ ไม่สามารถดำเนินการต่อได้")
                    self.status_var.set("ล้มเหลว")
                    return
                
                # ตรวจสอบ git repo
                if not os.path.exists('.git'):
                    self.run_command('git init')
                    self.run_command('git branch -M main')
                    repo_created = True
                    
                # แก้ไข remote URL (สำคัญมาก!)
                self.fix_remote_url()
                    
                # ตรวจสอบว่ามีการเปลี่ยนแปลงหรือไม่
                self.run_command('git add .')
                status_result = self.run_command('git status --porcelain', check_error=False)
                    
                if status_result and status_result.stdout.strip():
                    # Commit
                    commit_msg = f"Update - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    commit_result = self.run_command(f'git commit -m "{commit_msg}"', check_error=False)
                    
                    if commit_result and commit_result.returncode == 0:
                        self.log("✅ Commit สำเร็จ")
                    else:
                        self.log("⚠️ ไม่สามารถ commit ได้")
                else:
                    self.log("⚠️ ไม่มีการเปลี่ยนแปลงใหม่")
                
                # ตรวจสอบ branch ปัจจุบัน
                branch_result = self.run_command('git branch --show-current', check_error=False)
                current_branch = 'main'
                if branch_result and branch_result.stdout.strip():
                    current_branch = branch_result.stdout.strip()
                
                # Push พร้อมรอสักครู่หลังสร้าง repo
                if repo_created:
                    self.log("⏳ รอ repository พร้อมใช้งาน...")
                    import time
                    time.sleep(2)
                
                self.log(f"📤 กำลัง push ไปยัง branch: {current_branch}")
                push_result = self.run_command(f'git push -u origin {current_branch}', check_error=False)
                
                if push_result and push_result.returncode == 0:
                    self.log("✅ Push เสร็จสิ้น!")
                    self.status_var.set("Push เสร็จสิ้น")
                else:
                    # ลองอีกครั้งด้วย force push
                    self.log("⚠️ ลอง force push...")
                    force_result = self.run_command(f'git push -f origin {current_branch}', check_error=False)
                    if force_result and force_result.returncode == 0:
                        self.log("✅ Force push สำเร็จ!")
                        self.status_var.set("Push เสร็จสิ้น")
                    else:
                        self.log("❌ Push ล้มเหลว")
                        self.status_var.set("Push ล้มเหลว")
                
            except Exception as e:
                self.log(f"❌ ข้อผิดพลาด: {e}")
                self.status_var.set("เกิดข้อผิดพลาด")
                
        threading.Thread(target=push_thread, daemon=True).start()
        
    def create_release(self):
        """สร้าง release"""
        if not self.github_token.get():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ GitHub Token")
            return
            
        if not self.repo_owner.get() or not self.repo_name.get():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ Owner และ Repository")
            return
            
        self.show_release_dialog()
        
    def show_release_dialog(self):
        """หน้าต่างสร้าง release"""
        dialog = tk.Toplevel(self.root)
        dialog.title("สร้าง Release")
        dialog.geometry("500x400")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Get latest tag
        latest_tag = self.get_latest_tag()
        suggested_version = self.increment_version(latest_tag)
        
        tk.Label(dialog, text="สร้าง GitHub Release", font=('Arial', 14, 'bold')).pack(pady=15)
        tk.Label(dialog, text=f"Tag ล่าสุด: {latest_tag or 'ไม่มี'}").pack()
        
        # Version
        tk.Label(dialog, text="เวอร์ชันใหม่:").pack(pady=(15,5))
        version_var = tk.StringVar(value=suggested_version)
        tk.Entry(dialog, textvariable=version_var, width=30).pack()
        
        # Name
        tk.Label(dialog, text="ชื่อ Release:").pack(pady=(15,5))
        name_var = tk.StringVar(value=suggested_version)
        tk.Entry(dialog, textvariable=name_var, width=30).pack()
        
        # Description
        tk.Label(dialog, text="คำอธิบาย:").pack(pady=(15,5))
        desc_text = tk.Text(dialog, width=50, height=8)
        desc_text.pack(pady=5)
        
        # Auto changelog
        changelog = self.generate_changelog(latest_tag)
        desc_text.insert('1.0', changelog)
        
        # Buttons
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=20)
        
        def create_action():
            self.do_create_release(version_var.get(), name_var.get(), desc_text.get('1.0', 'end'))
            dialog.destroy()
            
        tk.Button(btn_frame, text="สร้าง Release", command=create_action, 
                 bg='#e74c3c', fg='white').pack(side='left', padx=10)
        tk.Button(btn_frame, text="ยกเลิก", command=dialog.destroy, 
                 bg='#95a5a6', fg='white').pack(side='left')
                 
    def get_latest_tag(self):
        """ดึง tag ล่าสุด"""
        try:
            result = subprocess.run('git tag --sort=-version:refname', shell=True, 
                                  cwd=self.project_path.get(), capture_output=True, text=True)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split('\n')[0]
        except:
            pass
        return None
        
    def increment_version(self, version):
        """เพิ่มเวอร์ชัน"""
        if not version:
            return "v1.0.0"
            
        clean_version = version.lstrip('v')
        parts = clean_version.split('.')
        
        try:
            if len(parts) >= 3:
                parts[2] = str(int(parts[2]) + 1)
                return f"v{'.'.join(parts)}"
        except:
            pass
            
        return f"v{clean_version}.1"
        
    def generate_changelog(self, latest_tag):
        """สร้าง changelog"""
        if not latest_tag:
            return "Release notes"
            
        try:
            result = subprocess.run(f'git log {latest_tag}..HEAD --oneline', shell=True, 
                                  cwd=self.project_path.get(), capture_output=True, text=True)
            if result.returncode == 0 and result.stdout.strip():
                changelog = "## การเปลี่ยนแปลง\n\n"
                for commit in result.stdout.strip().split('\n'):
                    if commit.strip():
                        changelog += f"- {commit}\n"
                return changelog
        except:
            pass
            
        return "Release notes"
        
    def do_create_release(self, version, name, description):
        """สร้าง release จริง"""
        def release_thread():
            try:
                self.status_var.set("กำลังสร้าง release...")
                self.log(f"🎯 สร้าง release {version}")
                
                url = f"https://api.github.com/repos/{self.repo_owner.get()}/{self.repo_name.get()}/releases"
                headers = {
                    'Authorization': f'token {self.github_token.get()}',
                    'Accept': 'application/vnd.github.v3+json'
                }
                
                data = {
                    'tag_name': version,
                    'name': name,
                    'body': description.strip(),
                    'draft': False,
                    'prerelease': False
                }
                
                response = requests.post(url, headers=headers, json=data)
                
                if response.status_code == 201:
                    release_data = response.json()
                    self.log(f"🎉 สร้าง release {version} สำเร็จ!")
                    self.log(f"🔗 URL: {release_data['html_url']}")
                    self.status_var.set("สร้าง release สำเร็จ")
                    messagebox.showinfo("สำเร็จ", f"สร้าง release {version} สำเร็จ!")
                else:
                    self.log(f"❌ ข้อผิดพลาด: {response.status_code}")
                    self.log(f"❌ {response.text}")
                    messagebox.showerror("ข้อผิดพลาด", f"ไม่สามารถสร้าง release ได้")
                    
            except Exception as e:
                self.log(f"❌ ข้อผิดพลาด: {e}")
                messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาด: {e}")
                
            self.status_var.set("พร้อมใช้งาน")
            
        threading.Thread(target=release_thread, daemon=True).start()
        
    def do_all(self):
        """ทำทั้งหมด"""
        def all_thread():
            try:
                self.log("🚀 เริ่มทำงานทั้งหมด")
                
                # ตรวจสอบข้อมูลพื้นฐาน
                if not self.repo_owner.get() or not self.repo_name.get():
                    self.log("❌ กรุณาใส่ชื่อ Owner และ Repository")
                    messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ชื่อ Owner และ Repository")
                    return
                
                project_dir = self.project_path.get()
                os.chdir(project_dir)
                
                # ตรวจสอบ git config
                self.check_git_config()
                
                # ตรวจสอบ repository
                if not self.check_repository_exists():
                    self.log("❌ ไม่สามารถดำเนินการต่อได้")
                    self.status_var.set("ล้มเหลว")
                    return
                
                # Push first
                self.status_var.set("กำลัง push...")
                
                if not os.path.exists('.git'):
                    self.run_command('git init')
                    self.run_command('git branch -M main')
                    
                # ตรวจสอบการเปลี่ยนแปลง
                self.run_command('git add .')
                status_result = self.run_command('git status --porcelain', check_error=False)
                
                if status_result and status_result.stdout.strip():
                    commit_msg = f"Release prep - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    commit_result = self.run_command(f'git commit -m "{commit_msg}"', check_error=False)
                else:
                    self.log("⚠️ ไม่มีการเปลี่ยนแปลงใหม่")
                
                # แก้ไข remote URL
                self.fix_remote_url()
                
                # ตรวจสอบ branch
                branch_result = self.run_command('git branch --show-current', check_error=False)
                current_branch = 'main'
                if branch_result and branch_result.stdout.strip():
                    current_branch = branch_result.stdout.strip()
                
                # Push
                push_result = self.run_command(f'git push -u origin {current_branch}', check_error=False)
                
                if push_result and push_result.returncode == 0:
                    self.log("✅ Push เสร็จสิ้น!")
                    
                    # Create release
                    if self.github_token.get():
                        self.log("🎯 เริ่มสร้าง release...")
                        latest_tag = self.get_latest_tag()
                        new_version = self.increment_version(latest_tag)
                        changelog = self.generate_changelog(latest_tag)
                        
                        # สร้าง release ในเธรดเดียวกัน
                        self.create_release_sync(new_version, new_version, changelog)
                    else:
                        self.log("⚠️ ข้าม release เนื่องจากไม่มี token")
                        
                    self.log("🎉 เสร็จสิ้นทั้งหมด!")
                    self.status_var.set("เสร็จสิ้นทั้งหมด")
                else:
                    self.log("❌ Push ล้มเหลว")
                    self.status_var.set("Push ล้มเหลว")
                
            except Exception as e:
                self.log(f"❌ ข้อผิดพลาด: {e}")
                self.status_var.set("เกิดข้อผิดพลาด")
                
        threading.Thread(target=all_thread, daemon=True).start()

    def create_release_sync(self, version, name, description):
        """สร้าง release แบบ sync"""
        try:
            self.status_var.set("กำลังสร้าง release...")
            self.log(f"🎯 สร้าง release {version}")
            
            url = f"https://api.github.com/repos/{self.repo_owner.get()}/{self.repo_name.get()}/releases"
            headers = {
                'Authorization': f'token {self.github_token.get()}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            data = {
                'tag_name': version,
                'name': name,
                'body': description.strip(),
                'draft': False,
                'prerelease': False
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 201:
                release_data = response.json()
                self.log(f"🎉 สร้าง release {version} สำเร็จ!")
                self.log(f"🔗 URL: {release_data['html_url']}")
                return True
            else:
                self.log(f"❌ ข้อผิดพลาด: {response.status_code}")
                self.log(f"❌ {response.text}")
                return False
                
        except Exception as e:
            self.log(f"❌ ข้อผิดพลาด: {e}")
            return False
        
    def refresh_info(self):
        """รีเฟรช"""
        self.load_repo_info()
        self.log("🔄 รีเฟรชเสร็จสิ้น")
        
    def view_releases(self):
        """ดู releases"""
        if self.repo_owner.get() and self.repo_name.get():
            url = f"https://github.com/{self.repo_owner.get()}/{self.repo_name.get()}/releases"
            webbrowser.open(url)
            self.log(f"🌐 เปิด: {url}")
        else:
            messagebox.showwarning("คำเตือน", "กรุณาใส่ Owner และ Repository")

    def check_setup(self):
        """ตรวจสอบการตั้งค่า"""
        def check_thread():
            self.log("🔍 เริ่มตรวจสอบการตั้งค่า...")
            
            # ตรวจสอบโฟลเดอร์
            if not os.path.exists(self.project_path.get()):
                self.log("❌ โฟลเดอร์โปรเจคไม่พบ")
                return
            else:
                self.log("✅ โฟลเดอร์โปรเจคพบแล้ว")
            
            # ตรวจสอบ Git
            git_result = self.run_command('git --version', check_error=False)
            if git_result and git_result.returncode == 0:
                self.log("✅ Git พร้อมใช้งาน")
            else:
                self.log("❌ Git ไม่พบ")
                return
            
            # ตรวจสอบ Git config
            self.check_git_config()
            
            # ตรวจสอบ GitHub Token
            if not self.github_token.get():
                self.log("❌ ไม่พบ GitHub Token")
            else:
                self.log("✅ GitHub Token พบแล้ว")
                
                # ทดสอบ Token
                try:
                    headers = {'Authorization': f'token {self.github_token.get()}'}
                    response = requests.get('https://api.github.com/user', headers=headers)
                    if response.status_code == 200:
                        user_data = response.json()
                        self.log(f"✅ Token ใช้งานได้ - ผู้ใช้: {user_data.get('login', 'Unknown')}")
                    else:
                        self.log(f"❌ Token ไม่ถูกต้อง: {response.status_code}")
                except Exception as e:
                    self.log(f"❌ ข้อผิดพลาดในการทดสอบ token: {e}")
            
            # ตรวจสอบ Repository
            if self.repo_owner.get() and self.repo_name.get():
                self.log(f"🔍 ตรวจสอบ repository: {self.repo_owner.get()}/{self.repo_name.get()}")
                if self.check_repository_exists():
                    self.log("✅ Repository พร้อมใช้งาน")
                else:
                    self.log("❌ Repository ไม่พร้อมใช้งาน")
            else:
                self.log("⚠️ ไม่ได้ระบุชื่อ Owner หรือ Repository")
            
            self.log("🔍 การตรวจสอบเสร็จสิ้น")
            
        threading.Thread(target=check_thread, daemon=True).start()

    def fix_remote_manual(self):
        """แก้ไข remote URL แบบ manual"""
        def fix_thread():
            try:
                project_dir = self.project_path.get()
                os.chdir(project_dir)
                
                if not os.path.exists('.git'):
                    self.log("❌ ไม่พบ Git repository")
                    return
                
                if not self.repo_owner.get() or not self.repo_name.get():
                    self.log("❌ กรุณาใส่ชื่อ Owner และ Repository")
                    return
                
                self.log("🔧 กำลังแก้ไข remote URL...")
                self.fix_remote_url()
                
                # ตรวจสอบ remote ใหม่
                result = self.run_command('git remote -v', check_error=False)
                if result:
                    self.log("✅ แก้ไข remote URL เสร็จสิ้น")
                
            except Exception as e:
                self.log(f"❌ ข้อผิดพลาด: {e}")
                
        threading.Thread(target=fix_thread, daemon=True).start()
            
    def run(self):
        """รันโปรแกรม"""
        self.log("🚀 Repository & Release Manager พร้อมใช้งาน")
        self.log("💡 เลือกโฟลเดอร์และใส่ GitHub Token เพื่อเริ่มใช้งาน")
        self.root.mainloop()

def main():
    """ฟังก์ชันหลัก"""
    try:
        app = RepoManagerGUI()
        app.run()
    except KeyboardInterrupt:
        print("\nยกเลิกการทำงาน")
    except Exception as e:
        print(f"ข้อผิดพลาด: {e}")
        input("กด Enter เพื่อออก...")

if __name__ == "__main__":
    main()