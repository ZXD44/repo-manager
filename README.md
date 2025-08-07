# 🚀 Repo Manager - เครื่องมือจัดการ GitHub Repository และ Release

**Repo Manager** เป็นเครื่องมือ GUI ที่พัฒนาด้วย Python (Tkinter) สำหรับช่วยให้การจัดการ GitHub repository ของคุณง่ายขึ้น สามารถ Push โค้ดและสร้าง Release ได้อย่างสะดวกผ่านหน้าต่างเดียว

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## ✨ คุณสมบัติหลัก (Features)

### 🔄 การจัดการโค้ด
- **Push อัตโนมัติ:** ทำ `git add .`, `git commit`, และ `git push` ในคลิกเดียว
- **ตรวจสอบสถานะ:** แสดงสถานะ Git repository แบบ real-time
- **เลือกโฟลเดอร์:** เปลี่ยนโฟลเดอร์ทำงานได้ง่าย

### 📦 การจัดการ Release
- **สร้าง Release:** สร้าง GitHub Release พร้อม tag และ changelog อัตโนมัติ
- **Changelog อัตโนมัติ:** สร้างรายการเปลี่ยนแปลงจาก commit messages
- **กำหนดเวอร์ชัน:** ระบุเวอร์ชันและคำอธิบายได้เอง

### 🛠️ ความสะดวก
- **Do All:** ทำทั้ง Push และสร้าง Release ในคำสั่งเดียว
- **ตรวจสอบอัตโนมัติ:** ตรวจสอบการตั้งค่า Git, Token และ Repository
- **สร้าง Repository:** สร้าง repository ใหม่บน GitHub ได้โดยตรง
- **บันทึกการทำงาน:** แสดงผลการทำงานแบบ real-time

---

## 📋 ความต้องการของระบบ (Requirements)

- **Python 3.x** - ภาษาโปรแกรมหลัก
- **Git** - ติดตั้งและเชื่อมต่อกับโฟลเดอร์โปรเจค
- **Internet Connection** - สำหรับเชื่อมต่อ GitHub API
- **GitHub Account** - พร้อม Personal Access Token

### ไลบรารีที่ต้องการ
```bash
pip install requests
```
*หมายเหตุ: โปรแกรมจะพยายามติดตั้งให้อัตโนมัติหากยังไม่มี*

---

## 🔒 ความปลอดภัย (Security)

โปรเจคนี้มีระบบป้องกันข้อมูลสำคัญผ่านไฟล์ `.gitignore`:

### ไฟล์ที่ถูกป้องกัน
- **🔐 Environment Variables:** `.env`, `.env.local`, `.env.production`
- **🐍 Python Cache:** `__pycache__/`, `*.pyc`, `build/`, `dist/`
- **💻 IDE Settings:** `.vscode/`, `.idea/`, `*.swp`
- **🖥️ OS Files:** `.DS_Store`, `Thumbs.db`

### การใช้ Environment Variables
สร้างไฟล์ `.env` เพื่อเก็บ GitHub Token อย่างปลอดภัย:
```env
GITHUB_TOKEN=ghp_your_token_here
```

---

## 🚀 การติดตั้งและใช้งาน (Installation & Usage)

### 1. ดาวน์โหลดและเตรียมพร้อม
```bash
# Clone หรือดาวน์โหลดโปรเจค
git clone <repository-url>
cd repo-manager

# ติดตั้ง dependencies
pip install requests
```

### 2. เตรียม GitHub Token
1. ไปที่ GitHub → Settings → Developer settings → Personal access tokens
2. สร้าง token ใหม่ด้วยสิทธิ์:
   - `repo` (Full control of private repositories)
   - `workflow` (Update GitHub Action workflows)
3. คัดลอก token ที่ได้

### 3. เรียกใช้โปรแกรม
```bash
python repo_manager.py
```

---

## 📖 คู่มือการใช้งาน (How to Use)

### 🎯 ขั้นตอนพื้นฐาน

#### 1. ตั้งค่าเริ่มต้น
- **เลือกโฟลเดอร์:** คลิก "เลือก" เพื่อเลือกโฟลเดอร์โปรเจค Git
- **ใส่ Token:** วาง GitHub Personal Access Token ในช่อง "GitHub Token"
- **ตรวจสอบ:** คลิก "ตรวจสอบ" เพื่อยืนยันการตั้งค่า

#### 2. การใช้งานหลัก

| ปุ่ม | คำอธิบาย | การทำงาน |
|------|----------|----------|
| 📤 **อัปโหลดไฟล์** | อัปโหลดโค้ดไปยัง GitHub | `git add .` → `git commit` → `git push` |
| 🎯 **สร้าง Release** | สร้าง GitHub Release | สร้าง tag, release notes, และ changelog |
| 🚀 **ทำทั้งหมด** | ทำทั้งสองอย่างทีละขั้นตอน | Push ก่อน แล้วสร้าง Release |
| 🔍 **ตรวจสอบ** | ตรวจสอบการตั้งค่า | ตรวจ Git, Token, Repository |

### 🔧 ฟีเจอร์ขั้นสูง

#### สร้าง Repository ใหม่
- Repository จะถูกสร้างอัตโนมัติเมื่อไม่พบ repository ที่ระบุ
- ระบบจะถามยืนยันก่อนสร้าง repository ใหม่
- Repository จะถูกสร้างเป็น Public โดยอัตโนมัติ

#### การกำหนด Release
- **เวอร์ชัน:** ระบุเวอร์ชันในรูปแบบ `v1.0.0`
- **คำอธิบาย:** เพิ่มรายละเอียดของ release
- **Changelog:** โปรแกรมจะสร้างจาก commit messages อัตโนมัติ

---

## 🎨 ตัวอย่างการใช้งาน (Examples)

### การ Push โค้ดครั้งแรก
```
1. เลือกโฟลเดอร์โปรเจค
2. ใส่ GitHub Token
3. คลิก "ตรวจสอบ" → ✅ ผ่าน
4. คลิก "อัปโหลดไฟล์" → 📤 กำลังอัปโหลด...
5. ✅ Push สำเร็จ!
```

### การสร้าง Release
```
1. ใส่เวอร์ชัน: v1.0.0
2. ใส่คำอธิบาย: "เวอร์ชันแรก - เพิ่มฟีเจอร์พื้นฐาน"
3. คลิก "สร้าง Release" → 📦 กำลังสร้าง...
4. ✅ Release v1.0.0 สร้างสำเร็จ!
```

---

## 🐛 การแก้ไขปัญหา (Troubleshooting)

### ปัญหาที่พบบ่อย

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|-------|--------|----------|
| ❌ Token ไม่ถูกต้อง | Token หมดอายุหรือสิทธิ์ไม่เพียงพอ | สร้าง token ใหม่ด้วยสิทธิ์ `repo` |
| ❌ ไม่พบ Git | ไม่ได้ติดตั้ง Git หรือไม่ได้ init | ติดตั้ง Git และรัน `git init` |
| ❌ Repository ไม่พบ | ชื่อ repository ผิดหรือไม่มีสิทธิ์ | ตรวจสอบชื่อและสิทธิ์การเข้าถึง |
| ❌ Push ไม่สำเร็จ | มีไฟล์ขัดแย้งหรือ branch ไม่ sync | รัน `git pull` ก่อน push |

### การตรวจสอบปัญหา
```bash
# ตรวจสอบ Git status
git status

# ตรวจสอบ remote
git remote -v

# ตรวจสอบ branch
git branch -a
```

---

## 📄 ใบอนุญาต (License)

โปรเจคนี้ใช้ใบอนุญาต **MIT License**

```
MIT License

Copyright (c) 2025 ZirconX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 ผู้พัฒนา (Author)

### **ZirconX** 
*Full Stack Developer & Open Source Enthusiast*

- 🌟 **ความเชี่ยวชาญ:** Python, GUI Development, Git Automation
- 🎯 **เป้าหมาย:** สร้างเครื่องมือที่ทำให้การพัฒนาซอฟต์แวร์ง่ายขึ้น
- 💡 **ปรัชญา:** เครื่องมือที่ดีควรทำให้งานซับซ้อนกลายเป็นเรื่องง่าย

#### 🤝 การสนับสนุน
- ⭐ **Star** โปรเจคนี้หากคุณชอบ
- 🐛 **Report Issues** หากพบปัญหา
- 💡 **Suggest Features** หากมีไอเดียใหม่
- 🔧 **Contribute** ยินดีรับ Pull Requests

#### 📞 ติดต่อ
- 📧 **Email:** [[ติดต่อผ่าน GitHub Issues](https://github.com/ZXD44)]
- 🐙 **GitHub:** [@ZirconX](www.zirconx.my)
- 💬 **Discussions:** ใช้ GitHub Discussions สำหรับคำถาม

---

## 🙏 ขอบคุณ (Acknowledgments)

- **Python Community** - สำหรับ Tkinter และ ecosystem ที่ยอดเยี่ยม
- **GitHub** - สำหรับ API ที่ใช้งานง่าย
- **Git** - สำหรับระบบ version control ที่ทรงพลัง
- **Open Source Community** - สำหรับแรงบันดาลใจและการสนับสนุน

---

*สร้างด้วย ❤️ โดย ZirconX | © 2025 All Rights Reserved*