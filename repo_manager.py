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
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
        self.root.geometry("1000x750")
        self.root.configure(bg='#f0f0f0')
        
        # ตัวแปร
        self.project_path = tk.StringVar(value=os.getcwd())
        
        # Load GitHub credentials from environment variables
        self.github_token = tk.StringVar(value=os.getenv('GITHUB_TOKEN', ''))
        self.github_username = tk.StringVar(value=os.getenv('GITHUB_USERNAME', ''))
        
        # Initialize repository variables
        self.repo_owner = tk.StringVar()
        self.repo_name = tk.StringVar()
        
        self.setup_ui()
        self.load_repo_info()
        
    def setup_ui(self):
        """สร้าง UI ธีม GitHub"""
        # GitHub Colors
        self.colors = {
            'bg': '#0d1117',           # GitHub dark background
            'surface': '#161b22',      # GitHub surface
            'border': '#30363d',       # GitHub border
            'text': '#f0f6fc',         # GitHub text
            'text_muted': '#8b949e',   # GitHub muted text
            'primary': '#238636',      # GitHub green
            'danger': '#da3633',       # GitHub red
            'warning': '#d29922',      # GitHub yellow
            'info': '#1f6feb',         # GitHub blue
            'secondary': '#6e7681',    # GitHub gray
        }
        
        # Configure root
        self.root.configure(bg=self.colors['bg'])
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors['surface'], height=70)
        header_frame.pack(fill='x', padx=2, pady=2)
        header_frame.pack_propagate(False)
        
        # GitHub-style header
        header_content = tk.Frame(header_frame, bg=self.colors['surface'])
        header_content.pack(expand=True, fill='both', padx=20, pady=15)
        
        tk.Label(header_content, text="🐙 ตัวจัดการ GitHub Repository", 
                font=('Segoe UI', 18, 'bold'), fg=self.colors['text'], 
                bg=self.colors['surface']).pack(side='left')
        
        # Status indicator
        self.status_var = tk.StringVar(value="พร้อมใช้งาน")
        status_label = tk.Label(header_content, textvariable=self.status_var,
                               font=('Segoe UI', 10), fg=self.colors['text_muted'],
                               bg=self.colors['surface'])
        status_label.pack(side='right')
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Settings Panel
        settings_panel = tk.Frame(main_container, bg=self.colors['surface'], 
                                 relief='solid', bd=1)
        settings_panel.pack(fill='x', pady=(0, 10))
        
        # Settings header
        settings_header = tk.Frame(settings_panel, bg=self.colors['surface'])
        settings_header.pack(fill='x', padx=15, pady=(15, 10))
        
        tk.Label(settings_header, text="⚙️ การตั้งค่า", 
                font=('Segoe UI', 12, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(side='left')
        
        # Settings content
        settings_content = tk.Frame(settings_panel, bg=self.colors['surface'])
        settings_content.pack(fill='x', padx=15, pady=(0, 15))
        
        # Project path
        self.create_input_field(settings_content, "📁 โฟลเดอร์โปรเจค:", 
                               self.project_path, 0, browse=True)
        
        # GitHub token
        self.create_input_field(settings_content, "🔑 GitHub Token:", 
                               self.github_token, 1, password=True, help=True)
        
        # Repository info - Hidden as we'll use GITHUB_USERNAME
        self.repo_owner.set(self.github_username.get())  # Auto-set repo owner to GITHUB_USERNAME
        # Repository name input only
        tk.Label(settings_content, text="📦 ชื่อ repository:", 
                font=('Segoe UI', 10), fg=self.colors['text'], 
                bg=self.colors['surface']).grid(row=5, column=0, sticky='w', pady=5, padx=5)
        
        repo_entry = tk.Entry(settings_content, textvariable=self.repo_name, 
                            font=('Segoe UI', 10), bg=self.colors['bg'], 
                            fg=self.colors['text'], insertbackground=self.colors['text'],
                            relief='solid', bd=1)
        repo_entry.grid(row=5, column=1, sticky='ew', pady=5, padx=5)
        repo_entry.bind('<Return>', lambda e: self.load_repo_info())
        
        # Add a note about the repository owner
        tk.Label(settings_content, text=f"Repository owner: {self.github_username.get()}", 
                font=('Segoe UI', 9), fg=self.colors['text_muted'], 
                bg=self.colors['surface']).grid(row=6, column=0, columnspan=2, sticky='w', padx=5)
        
        # Action Buttons Panel
        actions_panel = tk.Frame(main_container, bg=self.colors['surface'], 
                                relief='solid', bd=1)
        actions_panel.pack(fill='x', pady=(0, 10))
        
        # Actions header
        actions_header = tk.Frame(actions_panel, bg=self.colors['surface'])
        actions_header.pack(fill='x', padx=15, pady=(15, 10))
        
        tk.Label(actions_header, text="🚀 การดำเนินการ", 
                font=('Segoe UI', 12, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(side='left')
        
        # Main action buttons - simplified to 3 main buttons
        main_actions = tk.Frame(actions_panel, bg=self.colors['surface'])
        main_actions.pack(fill='x', padx=15, pady=(0, 15))
        
        # Primary actions (3 main buttons only)
        primary_frame = tk.Frame(main_actions, bg=self.colors['surface'])
        primary_frame.pack(fill='x', pady=(0, 15))
        
        self.create_action_button(primary_frame, "📤 อัปโหลดไฟล์", 
                                 self.push_files, self.colors['primary'], 0, 0, large=True)
        
        self.create_action_button(primary_frame, "🎯 สร้าง Release", 
                                 self.create_release, self.colors['warning'], 0, 1, large=True)
        
        self.create_action_button(primary_frame, "🚀 ทำทั้งหมด", 
                                 self.do_all, self.colors['info'], 0, 2, large=True)
        
        # Configure grid weights for 3 buttons
        for i in range(3):
            primary_frame.columnconfigure(i, weight=1)
        
        # Secondary actions - simplified
        secondary_frame = tk.Frame(main_actions, bg=self.colors['surface'])
        secondary_frame.pack(fill='x')
        
        # Left side - simple buttons
        left_frame = tk.Frame(secondary_frame, bg=self.colors['surface'])
        left_frame.pack(side='left')
        
        tk.Button(left_frame, text="🔍 ตรวจสอบ", command=self.check_setup,
                 font=('Segoe UI', 9), bg=self.colors['secondary'], fg='white',
                 relief='flat', cursor='hand2', width=10).pack(side='left', padx=(0, 5))
        
        tk.Button(left_frame, text="📋 ดู Releases", command=self.view_releases,
                 font=('Segoe UI', 9), bg=self.colors['secondary'], fg='white',
                 relief='flat', cursor='hand2', width=12).pack(side='left', padx=5)
        
        # Right side - exit button
        right_frame = tk.Frame(secondary_frame, bg=self.colors['surface'])
        right_frame.pack(side='right')
        
        tk.Button(right_frame, text="❌ ออก", command=self.root.quit,
                 font=('Segoe UI', 9), bg=self.colors['danger'], fg='white',
                 relief='flat', cursor='hand2', width=8).pack()
        
        # Log Panel
        log_panel = tk.Frame(main_container, bg=self.colors['surface'], 
                            relief='solid', bd=1)
        log_panel.pack(fill='both', expand=True)
        
        # Log header
        log_header = tk.Frame(log_panel, bg=self.colors['surface'])
        log_header.pack(fill='x', padx=15, pady=(15, 10))
        
        tk.Label(log_header, text="📝 บันทึกการทำงาน", 
                font=('Segoe UI', 12, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(side='left')
        
        # Clear log button
        clear_btn = tk.Button(log_header, text="ล้าง", font=('Segoe UI', 9),
                             bg=self.colors['secondary'], fg='white', relief='flat',
                             command=self.clear_log, cursor='hand2')
        clear_btn.pack(side='right')
        
        # Log content
        log_content = tk.Frame(log_panel, bg=self.colors['surface'])
        log_content.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        self.log_text = scrolledtext.ScrolledText(log_content, height=12, 
                                                 bg=self.colors['bg'], fg=self.colors['text'], 
                                                 font=('Consolas', 10), relief='solid', bd=1,
                                                 insertbackground=self.colors['text'])
        self.log_text.pack(fill='both', expand=True)
        
    def create_input_field(self, parent, label, variable, row, browse=False, password=False, help=False):
        """สร้างช่องกรอกข้อมูล"""
        tk.Label(parent, text=label, font=('Segoe UI', 10),
                fg=self.colors['text'], bg=self.colors['surface']).grid(row=row, column=0, sticky='w', pady=5)
        
        field_frame = tk.Frame(parent, bg=self.colors['surface'])
        field_frame.grid(row=row, column=1, sticky='ew', padx=(10, 0), pady=5)
        field_frame.columnconfigure(0, weight=1)
        
        entry = tk.Entry(field_frame, textvariable=variable, font=('Segoe UI', 10),
                        bg=self.colors['bg'], fg=self.colors['text'], 
                        insertbackground=self.colors['text'], relief='solid', bd=1,
                        show='*' if password else '')
        entry.grid(row=0, column=0, sticky='ew', padx=(0, 5))
        
        if browse:
            browse_btn = tk.Button(field_frame, text="เลือก", font=('Segoe UI', 9),
                                  bg=self.colors['secondary'], fg='white', relief='flat',
                                  command=self.browse_folder, cursor='hand2')
            browse_btn.grid(row=0, column=1)
        
        if help:
            help_btn = tk.Button(field_frame, text="ช่วยเหลือ", font=('Segoe UI', 9),
                                bg=self.colors['info'], fg='white', relief='flat',
                                command=self.show_token_help, cursor='hand2')
            help_btn.grid(row=0, column=2 if browse else 1, padx=(5, 0))
    
    def create_action_button(self, parent, text, command, color, row, col, large=False):
        """สร้างปุ่มหลัก"""
        height = 3 if large else 2
        width = 18 if large else 15
        
        btn = tk.Button(parent, text=text, command=command, 
                       font=('Segoe UI', 10, 'bold'), bg=color, fg='white',
                       relief='flat', height=height, width=width, cursor='hand2')
        btn.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
        
        # Hover effects
        def on_enter(e):
            btn.configure(bg=self.darken_color(color))
        def on_leave(e):
            btn.configure(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
    
    def create_small_button(self, parent, text, command, color, tooltip):
        """สร้างปุ่มเล็ก"""
        btn = tk.Button(parent, text=text, command=command, 
                       font=('Segoe UI', 10), bg=color, fg='white',
                       relief='flat', width=3, height=1, cursor='hand2')
        btn.pack(side='left', padx=2)
        
        # Tooltip
        self.create_tooltip(btn, tooltip)
    
    def create_tooltip(self, widget, text):
        """สร้าง tooltip"""
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = tk.Label(tooltip, text=text, background=self.colors['surface'],
                           foreground=self.colors['text'], relief='solid', bd=1,
                           font=('Segoe UI', 9))
            label.pack()
            widget.tooltip = tooltip
        
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
    
    def darken_color(self, color):
        """ทำให้สีเข้มขึ้น"""
        color_map = {
            self.colors['primary']: '#1f7a2e',
            self.colors['danger']: '#b92d2b',
            self.colors['warning']: '#b8851c',
            self.colors['info']: '#1a5fb4',
            self.colors['secondary']: '#5a6169',
        }
        return color_map.get(color, color)
    

    def clear_log(self):
        """ล้าง log"""
        self.log_text.delete(1.0, tk.END)
        self.log("📝 ล้างบันทึกแล้ว")
    
    def create_repo_only(self):
        """สร้าง repository เท่านั้น"""
        if not self.github_token.get():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ GitHub Token")
            return
        if not self.repo_owner.get() or not self.repo_name.get():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ชื่อเจ้าของและ Repository")
            return
        
        def create_thread():
            self.status_var.set("กำลังสร้าง repository...")
            if self.create_repository():
                self.log("✅ สร้าง Repository สำเร็จ!")
                self.status_var.set("สร้าง Repository สำเร็จ")
                messagebox.showinfo("สำเร็จ", "สร้าง Repository สำเร็จ!")
            else:
                self.status_var.set("สร้าง Repository ล้มเหลว")
            
        threading.Thread(target=create_thread, daemon=True).start()
    
    def open_github(self):
        """เปิด GitHub repository"""
        if self.repo_owner.get() and self.repo_name.get():
            url = f"https://github.com/{self.repo_owner.get()}/{self.repo_name.get()}"
            webbrowser.open(url)
            self.log(f"🌐 Opened: {url}")
        else:
            messagebox.showwarning("คำเตือน", "กรุณาใส่ชื่อเจ้าของและ Repository")
        
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
            
            # Always use the GitHub username from environment variables
            self.repo_owner.set(self.github_username.get())
            
            # Try to get repo name from git remote
            result = subprocess.run('git remote get-url origin', shell=True, 
                                  capture_output=True, text=True)
            
            if result.returncode == 0 and result.stdout:
                url = result.stdout.strip()
                self.log(f"Found remote URL: {url}")
                
                if 'github.com' in url:
                    if url.startswith('https://'):
                        parts = url.replace('https://github.com/', '').replace('.git', '').split('/')
                    elif url.startswith('git@'):
                        parts = url.replace('git@github.com:', '').replace('.git', '').split('/')
                    
                    if len(parts) >= 2:
                        # Only set the repository name, owner comes from GITHUB_USERNAME
                        self.repo_name.set(parts[1])
                        self.log(f"📁 Repository: {self.github_username.get()}/{parts[1]}")
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
                    self.log(f"✅ ตั้งค่า git user.name: {name}")
                    
            if not email_result or not email_result.stdout.strip():
                self.log("⚠️ ไม่พบ git user.email")
                email = messagebox.askstring("Git Config", "ใส่อีเมล Git:")
                if email:
                    self.run_command(f'git config user.email "{email}"')
                    self.log(f"✅ ตั้งค่า git user.email: {email}")
                    
        except Exception as e:
            self.log(f"ข้อผิดพลาดในการตรวจสอบ git config: {e}")

    def check_repository_exists(self):
        """ตรวจสอบว่า repository มีอยู่จริง"""
        if not self.github_token.get() or not self.repo_owner.get() or not self.repo_name.get():
            return False
            
        try:
            url = f"https://api.github.com/repos/{self.repo_owner.get()}/{self.repo_name.get()}"
            headers = {
                'Authorization': f'Bearer {self.github_token.get()}',
                'Accept': 'application/vnd.github.v3+json',
                'X-GitHub-Api-Version': '2022-11-28'
            }
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
                'Authorization': f'Bearer {self.github_token.get()}',
                'Accept': 'application/vnd.github.v3+json',
                'X-GitHub-Api-Version': '2022-11-28'
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
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ชื่อเจ้าของและ Repository")
            return
            
        self.show_quick_release_dialog()
    


    def show_quick_release_dialog(self):
        """แสดงหน้าต่างสำหรับ quick release"""
        dialog = tk.Toplevel(self.root)
        dialog.title("สร้าง Release")
        dialog.geometry("580x480")  # ลดขนาดลง
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg=self.colors['surface'])
        
        # ย้ายไปข้างบนและกึ่งกลาง
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 20))
        
        # Get version info
        latest_tag = self.get_latest_tag()
        all_tags = self.get_all_tags()
        suggested_version = self.increment_version(latest_tag)
        
        # Header - ปรับให้กะทัดรัดขึ้น
        header_frame = tk.Frame(dialog, bg=self.colors['surface'])
        header_frame.pack(fill='x', padx=15, pady=15)
        
        tk.Label(header_frame, text="🎯 สร้าง GitHub Release", 
                font=('Segoe UI', 16, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack()
        
        tk.Label(header_frame, text=f"เวอร์ชันล่าสุด: {latest_tag or 'ไม่มี'}", 
                font=('Segoe UI', 10), fg=self.colors['text_muted'],
                bg=self.colors['surface']).pack(pady=(3, 0))
        
        # Credit - ย้ายไปด้านล่าง
        tk.Label(header_frame, text="👨‍💻 ZirconX", 
                font=('Segoe UI', 8), fg=self.colors['text_muted'],
                bg=self.colors['surface']).pack(pady=(1, 0))
        
        # Content - ปรับ padding ให้เหมาะสม
        content_frame = tk.Frame(dialog, bg=self.colors['surface'])
        content_frame.pack(fill='both', expand=True, padx=15, pady=8)
        
        # Show existing tags - ปรับให้กะทัดรัด
        if all_tags:
            tk.Label(content_frame, text="📋 เวอร์ชันที่มี:", 
                    font=('Segoe UI', 9, 'bold'), fg=self.colors['text'],
                    bg=self.colors['surface']).pack(anchor='w', pady=(0, 3))
            
            tags_text = ", ".join(all_tags[:6])  # Show first 6 tags
            if len(all_tags) > 6:
                tags_text += f" ... (อีก {len(all_tags)-6} เวอร์ชัน)"
            
            tk.Label(content_frame, text=tags_text, 
                    font=('Segoe UI', 8), fg=self.colors['text_muted'],
                    bg=self.colors['surface'], wraplength=380, justify='left').pack(anchor='w', pady=(0, 10))
        
        # Version selection
        tk.Label(content_frame, text="🏷️ เวอร์ชันใหม่:", 
                font=('Segoe UI', 10, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(anchor='w', pady=(0, 5))
        
        version_frame = tk.Frame(content_frame, bg=self.colors['surface'])
        version_frame.pack(fill='x', pady=(0, 10))
        
        version_var = tk.StringVar(value=suggested_version)
        version_entry = tk.Entry(version_frame, textvariable=version_var, 
                                font=('Segoe UI', 12), bg=self.colors['bg'], 
                                fg=self.colors['text'], insertbackground=self.colors['text'],
                                relief='solid', bd=1, width=15)
        version_entry.pack(side='left', padx=(0, 15))
        
        # Simplified version increment - only one button
        def next_version():
            current = version_var.get()
            new_ver = self.increment_version_type(current, 'patch')
            version_var.set(new_ver)
        
        next_btn = tk.Button(version_frame, text="เวอร์ชันถัดไป", command=next_version,
                            font=('Segoe UI', 10), bg=self.colors['primary'], fg='white',
                            relief='flat', cursor='hand2', width=12)
        next_btn.pack(side='left')
        
        # Release Notes - Editable - ปรับให้กะทัดรัด
        tk.Label(content_frame, text="📝 รายละเอียด Release:", 
                font=('Segoe UI', 10, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(anchor='w', pady=(12, 4))
        
        changelog = self.generate_changelog(latest_tag)
        notes_text = tk.Text(content_frame, height=10, width=65,
                            bg=self.colors['bg'], fg=self.colors['text'],
                            font=('Segoe UI', 9), relief='solid', bd=1,
                            insertbackground=self.colors['text'], wrap='word')
        notes_text.pack(anchor='w', pady=(0, 12), fill='both', expand=True)
        
        notes_text.insert('1.0', changelog)
        
        # Buttons - ปรับ padding
        btn_frame = tk.Frame(dialog, bg=self.colors['surface'])
        btn_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        def create_quick_release():
            new_version = version_var.get().strip()
            if not new_version:
                messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่เวอร์ชัน")
                return
            
            if new_version in all_tags:
                messagebox.showerror("ข้อผิดพลาด", f"เวอร์ชัน {new_version} มีอยู่แล้ว!")
                return
            
            # Get edited release notes
            release_notes = notes_text.get('1.0', 'end-1c').strip()
            if not release_notes:
                release_notes = f"Release {new_version}"
            
            dialog.destroy()
            self.do_quick_release(new_version, release_notes)
        
        # Center the buttons
        btn_container = tk.Frame(btn_frame, bg=self.colors['surface'])
        btn_container.pack(expand=True)
        
        ok_btn = tk.Button(btn_container, text="✅ ตกลง", 
                          command=create_quick_release,
                          font=('Segoe UI', 11, 'bold'), bg=self.colors['primary'], 
                          fg='white', relief='flat', cursor='hand2', width=14, height=2)
        ok_btn.pack(side='left', padx=(0, 12))
        
        cancel_btn = tk.Button(btn_container, text="❌ ยกเลิก", command=dialog.destroy,
                              font=('Segoe UI', 10), bg=self.colors['secondary'], 
                              fg='white', relief='flat', cursor='hand2', width=10, height=2)
        cancel_btn.pack(side='left')
        
        # Make OK button the default (Enter key)
        ok_btn.focus_set()
        dialog.bind('<Return>', lambda e: create_quick_release())
    
    def get_all_tags(self):
        """ดึง tags ทั้งหมด"""
        try:
            result = subprocess.run('git tag --sort=-version:refname', shell=True, 
                                  cwd=self.project_path.get(), capture_output=True, text=True)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split('\n')
        except:
            pass
        return []
    
    def increment_version_type(self, version, version_type):
        """เพิ่มเวอร์ชันตามประเภท"""
        if not version:
            return "v1.0.0"
        
        clean_version = version.lstrip('v')
        parts = clean_version.split('.')
        
        try:
            if len(parts) >= 3:
                major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
                
                if version_type == 'major':
                    return f"v{major + 1}.0.0"
                elif version_type == 'minor':
                    return f"v{major}.{minor + 1}.0"
                elif version_type == 'patch':
                    return f"v{major}.{minor}.{patch + 1}"
        except:
            pass
        
        return f"v{clean_version}.1"
    
    def do_quick_release(self, version, changelog):
        """สร้าง quick release"""
        def quick_release_thread():
            try:
                self.status_var.set("Creating quick release...")
                self.log("⚡ Starting quick release creation...")
                self.log(f"📋 Version: {version}")
                
                # Create release
                success = self.create_release_sync(version, version, changelog)
                
                if success:
                    self.log("🎉 Quick release created successfully!")
                    self.status_var.set("Release created")
                    messagebox.showinfo("Success", f"Release {version} created successfully!")
                else:
                    self.log("❌ Failed to create release")
                    self.status_var.set("Release failed")
                    
            except Exception as e:
                self.log(f"❌ Error: {e}")
                self.status_var.set("Error")
                messagebox.showerror("Error", f"Failed to create release: {e}")
        
        threading.Thread(target=quick_release_thread, daemon=True).start()
        
    def show_release_dialog(self, parent_dialog=None):
        """หน้าต่างสร้าง release แบบ custom"""
        if parent_dialog:
            parent_dialog.destroy()
            
        dialog = tk.Toplevel(self.root)
        dialog.title("Custom Release")
        dialog.geometry("520x420")  # ลดขนาดลง
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg=self.colors['surface'])
        
        # ย้ายไปข้างบนและกึ่งกลาง
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 60, self.root.winfo_rooty() + 25))
        
        # Get latest tag
        latest_tag = self.get_latest_tag()
        suggested_version = self.increment_version(latest_tag)
        
        # Header
        header_frame = tk.Frame(dialog, bg=self.colors['surface'])
        header_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(header_frame, text="🛠️ Custom GitHub Release", 
                font=('Segoe UI', 16, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack()
        
        tk.Label(header_frame, text=f"Latest tag: {latest_tag or 'None'}", 
                font=('Segoe UI', 10), fg=self.colors['text_muted'],
                bg=self.colors['surface']).pack(pady=(5, 0))
        
        # Content frame
        content_frame = tk.Frame(dialog, bg=self.colors['surface'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Version
        tk.Label(content_frame, text="🏷️ Version:", font=('Segoe UI', 10, 'bold'),
                fg=self.colors['text'], bg=self.colors['surface']).pack(anchor='w', pady=(0,5))
        
        version_var = tk.StringVar(value=suggested_version)
        version_entry = tk.Entry(content_frame, textvariable=version_var, 
                                font=('Segoe UI', 10), bg=self.colors['bg'], 
                                fg=self.colors['text'], insertbackground=self.colors['text'],
                                relief='solid', bd=1, width=40)
        version_entry.pack(anchor='w', pady=(0,15))
        
        # Name
        tk.Label(content_frame, text="📝 Release Name:", font=('Segoe UI', 10, 'bold'),
                fg=self.colors['text'], bg=self.colors['surface']).pack(anchor='w', pady=(0,5))
        
        name_var = tk.StringVar(value=suggested_version)
        name_entry = tk.Entry(content_frame, textvariable=name_var, 
                             font=('Segoe UI', 10), bg=self.colors['bg'], 
                             fg=self.colors['text'], insertbackground=self.colors['text'],
                             relief='solid', bd=1, width=40)
        name_entry.pack(anchor='w', pady=(0,15))
        
        # Description
        tk.Label(content_frame, text="📋 Release Notes:", font=('Segoe UI', 10, 'bold'),
                fg=self.colors['text'], bg=self.colors['surface']).pack(anchor='w', pady=(0,5))
        
        desc_text = tk.Text(content_frame, width=60, height=10, 
                           bg=self.colors['bg'], fg=self.colors['text'], 
                           font=('Segoe UI', 9), relief='solid', bd=1,
                           insertbackground=self.colors['text'])
        desc_text.pack(anchor='w', pady=(0,15))
        
        # Auto changelog
        changelog = self.generate_changelog(latest_tag)
        desc_text.insert('1.0', changelog)
        
        # Buttons
        btn_frame = tk.Frame(dialog, bg=self.colors['surface'])
        btn_frame.pack(fill='x', padx=20, pady=(0,20))
        
        def create_action():
            self.do_create_release(version_var.get(), name_var.get(), desc_text.get('1.0', 'end'))
            dialog.destroy()
            
        create_btn = tk.Button(btn_frame, text="🚀 Create Release", command=create_action, 
                              font=('Segoe UI', 10, 'bold'), bg=self.colors['primary'], 
                              fg='white', relief='flat', cursor='hand2', width=15)
        create_btn.pack(side='left', padx=(0,10))
        
        cancel_btn = tk.Button(btn_frame, text="Cancel", command=dialog.destroy, 
                              font=('Segoe UI', 10), bg=self.colors['secondary'], 
                              fg='white', relief='flat', cursor='hand2', width=10)
        cancel_btn.pack(side='left')
                 
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
                    'Authorization': f'Bearer {self.github_token.get()}',
                    'Accept': 'application/vnd.github.v3+json',
                    'X-GitHub-Api-Version': '2022-11-28'
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
        """ทำทั้งหมด - ทีละขั้นตอน"""
        # ตรวจสอบข้อมูลพื้นฐานก่อน
        if not self.repo_owner.get() or not self.repo_name.get():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ชื่อเจ้าของและ Repository")
            return
        
        if not self.github_token.get():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ GitHub Token")
            return
        
        self.log("🚀 เริ่มทำงานทั้งหมด - ทีละขั้นตอน")
        
        # ขั้นตอนที่ 1: Push ไฟล์
        self.do_push_step()
    
    def do_push_step(self):
        """ขั้นตอนที่ 1: Push ไฟล์"""
        def push_thread():
            try:
                self.status_var.set("ขั้นตอน 1/2: กำลัง push ไฟล์...")
                self.log("📤 ขั้นตอนที่ 1: เริ่ม push ไฟล์")
                
                project_dir = self.project_path.get()
                os.chdir(project_dir)
                
                # ตรวจสอบ git config
                self.check_git_config()
                
                # ตรวจสอบ repository
                if not self.check_repository_exists():
                    self.log("❌ ไม่สามารถดำเนินการต่อได้")
                    self.status_var.set("ล้มเหลว")
                    return
                
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
                    self.log("✅ ขั้นตอนที่ 1 เสร็จสิ้น: Push ไฟล์สำเร็จ!")
                    self.status_var.set("ขั้นตอน 1/2 เสร็จสิ้น")
                    
                    # ไปขั้นตอนที่ 2: สร้าง release
                    self.root.after(1000, self.do_release_step)  # รอ 1 วินาทีแล้วไปขั้นตอนต่อไป
                else:
                    self.log("❌ ขั้นตอนที่ 1 ล้มเหลว: Push ไฟล์ไม่สำเร็จ")
                    self.status_var.set("Push ล้มเหลว")
                
            except Exception as e:
                self.log(f"❌ ข้อผิดพลาดในขั้นตอนที่ 1: {e}")
                self.status_var.set("เกิดข้อผิดพลาด")
                
        threading.Thread(target=push_thread, daemon=True).start()
    
    def do_release_step(self):
        """ขั้นตอนที่ 2: สร้าง Release"""
        self.log("🎯 ขั้นตอนที่ 2: เริ่มสร้าง Release")
        self.status_var.set("ขั้นตอน 2/2: กำลังสร้าง Release...")
        
        # เปิด popup เลือกเวอร์ชัน
        self.show_quick_release_dialog_for_do_all()
    
    def show_quick_release_dialog_for_do_all(self):
        """แสดงหน้าต่างเลือกเวอร์ชันสำหรับ ทำทั้งหมด"""
        dialog = tk.Toplevel(self.root)
        dialog.title("ขั้นตอนที่ 2: สร้าง Release")
        dialog.geometry("600x500")  # ลดขนาดลง
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg=self.colors['surface'])
        
        # ย้ายไปข้างบนและกึ่งกลาง
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 60, self.root.winfo_rooty() + 25))
        
        # Get version info
        latest_tag = self.get_latest_tag()
        all_tags = self.get_all_tags()
        suggested_version = self.increment_version(latest_tag)
        
        # Header - ปรับให้กะทัดรัดขึ้น
        header_frame = tk.Frame(dialog, bg=self.colors['surface'])
        header_frame.pack(fill='x', padx=15, pady=15)
        
        tk.Label(header_frame, text="🎯 ขั้นตอนที่ 2: สร้าง Release", 
                font=('Segoe UI', 16, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack()
        
        tk.Label(header_frame, text=f"✅ Push เสร็จแล้ว | เวอร์ชันล่าสุด: {latest_tag or 'ไม่มี'}", 
                font=('Segoe UI', 10), fg=self.colors['text_muted'],
                bg=self.colors['surface']).pack(pady=(5, 0))
        
        # Content - ปรับ padding ให้เหมาะสม
        content_frame = tk.Frame(dialog, bg=self.colors['surface'])
        content_frame.pack(fill='both', expand=True, padx=15, pady=8)
        
        # Show existing tags - ปรับให้กะทัดรัด
        if all_tags:
            tk.Label(content_frame, text="📋 เวอร์ชันที่มี:", 
                    font=('Segoe UI', 9, 'bold'), fg=self.colors['text'],
                    bg=self.colors['surface']).pack(anchor='w', pady=(0, 3))
            
            tags_text = ", ".join(all_tags[:6])  # Show first 6 tags
            if len(all_tags) > 6:
                tags_text += f" ... (อีก {len(all_tags)-6} เวอร์ชัน)"
            
            tk.Label(content_frame, text=tags_text, 
                    font=('Segoe UI', 8), fg=self.colors['text_muted'],
                    bg=self.colors['surface'], wraplength=520, justify='left').pack(anchor='w', pady=(0, 12))
        
        # Version selection - ปรับให้กะทัดรัด
        tk.Label(content_frame, text="🏷️ เวอร์ชันใหม่:", 
                font=('Segoe UI', 10, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(anchor='w', pady=(0, 5))
        
        version_frame = tk.Frame(content_frame, bg=self.colors['surface'])
        version_frame.pack(fill='x', pady=(0, 12))
        
        version_var = tk.StringVar(value=suggested_version)
        version_entry = tk.Entry(version_frame, textvariable=version_var, 
                                font=('Segoe UI', 12), bg=self.colors['bg'], 
                                fg=self.colors['text'], insertbackground=self.colors['text'],
                                relief='solid', bd=1, width=15)
        version_entry.pack(side='left', padx=(0, 15))
        
        # Next version button
        def next_version():
            current = version_var.get()
            new_ver = self.increment_version_type(current, 'patch')
            version_var.set(new_ver)
        
        next_btn = tk.Button(version_frame, text="เวอร์ชันถัดไป", command=next_version,
                            font=('Segoe UI', 10), bg=self.colors['primary'], fg='white',
                            relief='flat', cursor='hand2', width=12)
        next_btn.pack(side='left')
        
        # Release notes - ปรับให้กะทัดรัด
        tk.Label(content_frame, text="📝 รายละเอียด Release:", 
                font=('Segoe UI', 10, 'bold'), fg=self.colors['text'],
                bg=self.colors['surface']).pack(anchor='w', pady=(0, 4))
        
        changelog = self.generate_changelog(latest_tag)
        notes_text = tk.Text(content_frame, height=10, width=70,
                            bg=self.colors['bg'], fg=self.colors['text'],
                            font=('Segoe UI', 9), relief='solid', bd=1,
                            insertbackground=self.colors['text'], wrap='word')
        notes_text.pack(anchor='w', pady=(0, 12), fill='both', expand=True)
        
        notes_text.insert('1.0', changelog)
        
        # Buttons - ปรับ padding
        btn_frame = tk.Frame(dialog, bg=self.colors['surface'])
        btn_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        def create_final_release():
            new_version = version_var.get().strip()
            if not new_version:
                messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่เวอร์ชัน")
                return
            
            if new_version in all_tags:
                messagebox.showerror("ข้อผิดพลาด", f"เวอร์ชัน {new_version} มีอยู่แล้ว!")
                return
            
            # Get edited release notes
            release_notes = notes_text.get('1.0', 'end-1c').strip()
            if not release_notes:
                release_notes = f"Release {new_version}"
            
            dialog.destroy()
            self.do_final_release(new_version, release_notes)
        

        # Center the buttons - simplified to 2 main buttons
        btn_container = tk.Frame(btn_frame, bg=self.colors['surface'])
        btn_container.pack(expand=True)
        
        # Main OK button (most prominent)
        ok_btn = tk.Button(btn_container, text="✅ ตกลง", 
                          command=create_final_release,
                          font=('Segoe UI', 11, 'bold'), bg=self.colors['primary'], 
                          fg='white', relief='flat', cursor='hand2', width=14, height=2)
        ok_btn.pack(side='left', padx=(0, 12))
        
        # Cancel button
        cancel_btn = tk.Button(btn_container, text="❌ ยกเลิก", command=dialog.destroy,
                              font=('Segoe UI', 10), bg=self.colors['secondary'], 
                              fg='white', relief='flat', cursor='hand2', width=10, height=2)
        cancel_btn.pack(side='left')
        
        # Make OK button the default (Enter key)
        ok_btn.focus_set()
        dialog.bind('<Return>', lambda e: create_final_release())
        dialog.bind('<Escape>', lambda e: dialog.destroy())
    
    def do_final_release(self, version, release_notes):
        """สร้าง release ขั้นตอนสุดท้าย"""
        def final_release_thread():
            try:
                self.status_var.set("กำลังสร้าง Release...")
                self.log(f"🎯 สร้าง release {version}")
                
                # Create release
                success = self.create_release_sync(version, version, release_notes)
                
                if success:
                    self.log("🎉 ขั้นตอนที่ 2 เสร็จสิ้น: สร้าง Release สำเร็จ!")
                    self.log("✨ เสร็จสิ้นทั้งหมด! Push ไฟล์และสร้าง Release สำเร็จ!")
                    self.status_var.set("เสร็จสิ้นทั้งหมด")
                    messagebox.showinfo("สำเร็จ", f"เสร็จสิ้นทั้งหมด!\n✅ Push ไฟล์สำเร็จ\n✅ สร้าง Release {version} สำเร็จ")
                else:
                    self.log("❌ ขั้นตอนที่ 2 ล้มเหลว: สร้าง Release ไม่สำเร็จ")
                    self.status_var.set("สร้าง Release ล้มเหลว")
                    
            except Exception as e:
                self.log(f"❌ ข้อผิดพลาดในขั้นตอนที่ 2: {e}")
                self.status_var.set("เกิดข้อผิดพลาด")
        
        threading.Thread(target=final_release_thread, daemon=True).start()

    def create_release_sync(self, version, name, description):
        """สร้าง release แบบ sync"""
        try:
            self.status_var.set("กำลังสร้าง release...")
            self.log(f"🎯 สร้าง release {version}")
            
            url = f"https://api.github.com/repos/{self.repo_owner.get()}/{self.repo_name.get()}/releases"
            headers = {
                'Authorization': f'Bearer {self.github_token.get()}',
                'Accept': 'application/vnd.github.v3+json',
                'X-GitHub-Api-Version': '2022-11-28'
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
                    headers = {
                        'Authorization': f'Bearer {self.github_token.get()}',
                        'Accept': 'application/vnd.github.v3+json',
                        'X-GitHub-Api-Version': '2022-11-28'
                    }
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
        self.log("👨‍💻 สร้างโดย ZirconX - ขอบคุณที่ใช้งาน!")
        self.log("📄 MIT License - ใช้งานได้อย่างอิสระ")
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