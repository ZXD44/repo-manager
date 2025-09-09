<div align="center">

# 🚀 GitHub Repository & Release Manager

### ⚡ เครื่องมือจัดการ GitHub แบบ All-in-One ที่ทรงพลังที่สุด!

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=for-the-badge" alt="Platform">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange.svg?style=for-the-badge" alt="GUI">
  <img src="https://img.shields.io/badge/GitHub-API-purple.svg?style=for-the-badge&logo=github" alt="GitHub API">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg?style=for-the-badge" alt="Status">
</p>

**🎯 ทำให้การจัดการ GitHub Repository และ Release ง่ายเหมือนกดปุ่มเดียว!**

*พัฒนาด้วย ❤️ โดย ZirconX | สร้างเพื่อความสะดวกของ Developer ทุกคน*

---

</div>

## ✨ คุณสมบัติหลัก (Features)

<table>
<tr>
<td align="center" width="33%">

### 📤 การจัดการไฟล์
🔥 **Push อัตโนมัติ**
- `git add .` ✅
- `git commit` ✅  
- `git push` ✅

🔍 **ตรวจสอบสถานะ**
- Real-time status
- Git repository check
- โฟลเดอร์เปลี่ยนได้ง่าย

</td>
<td align="center" width="33%">

### 🎯 การจัดการ Release
🚀 **สร้าง Release**
- GitHub Release พร้อม tag
- Changelog อัตโนมัติ
- กำหนดเวอร์ชันได้เอง

📝 **ความสะดวก**
- เลือกเวอร์ชันจาก dropdown
- สร้าง changelog จาก commits
- เปิด GitHub ได้ทันที

</td>
<td align="center" width="33%">

### ⚡ ความสะดวก
🎁 **Do All**
- Push + Release ในครั้งเดียว
- ทำงานทีละขั้นตอน
- แสดงสถานะชัดเจน

🔧 **ตรวจสอบระบบ**
- Git config check
- Token validation
- Repository status

</td>
</tr>
</table>

---

## ❓ วิธีใช้งาน (Usage)

### 1. ตั้งค่าเริ่มต้น
1. **แก้ไขไฟล์ `.env`**
   ```env
   GITHUB_TOKEN=your_token_here
   GITHUB_USERNAME=your_username
   ```

2. **รันโปรแกรม**
   - Windows: ดับเบิลคลิกที่ `run.bat`
   - หรือใช้คำสั่ง: `python repo_manager.py`

### 2. ใช้งานฟีเจอร์หลัก
- **📁 เลือกโฟลเดอร์โปรเจค**
  - คลิกปุ่ม "Browse" เพื่อเลือกโฟลเดอร์โปรเจค
  - ระบบจะดึงข้อมูล repository อัตโนมัติ

- **🔄 Push ไฟล์**
  - ระบบจะแสดงรายการไฟล์ที่เปลี่ยนแปลง
  - กด "Push" เพื่ออัปโหลดไฟล์

- **🚀 สร้าง Release**
  - ระบบจะแนะนำเวอร์ชันถัดไปอัตโนมัติ
  - สามารถเพิ่มรายละเอียด Release ได้
  - สร้าง Changelog อัตโนมัติ

### 3. หน้าต่าง Log
- แสดงสถานะการทำงานแบบเรียลไทม์
- แจ้งเตือนเมื่อเกิดข้อผิดพลาด
- แสดง URL ของ Release ที่สร้างเสร็จ

### 4. ปุ่มลัด
- **F5**: รีเฟรชข้อมูล
- **Ctrl+Q**: ออกจากโปรแกรม
- **Ctrl+P**: Push ไฟล์
- **Ctrl+R**: สร้าง Release

> **⚠️ คำเตือน:** อย่าแชร์ไฟล์ `.env` หรือ Token กับผู้อื่น!

---

## 🚀 เริ่มต้นใช้งาน (Getting Started)

### 📋 ข้อกำหนดเบื้องต้น
- Python 3.6 ขึ้นไป
- Git
- GitHub Account
- GitHub Personal Access Token (มีสิทธิ์ repo, workflow, write:packages, delete_repo)

### ⚙️ การติดตั้ง

1. **โคลนโปรเจค**
   - คัดลอก Token ทันที (ขึ้นต้นด้วย `ghp_`)
   - ⚠️ **สำคัญ**: Token จะแสดงครั้งเดียวเท่านั้น!

4. **💾 บันทึกใน .env**
   ```bash
   # สร้างไฟล์ .env ในโฟลเดอร์โปรเจค
   echo "GITHUB_TOKEN=ghp_your_token_here" > .env
   ```

</details>

### 🏃‍♂️ ขั้นตอนที่ 3: เรียกใช้โปรแกรม

<div align="center">

### 🪟 Windows Users
```cmd
# วิธีที่ 1: ใช้ Batch File (แนะนำ)
run.bat

# วิธีที่ 2: Command Line
python repo_manager.py
```

### 🍎 macOS/Linux Users
```bash
# วิธีที่ 1: Command Line
python3 repo_manager.py

# วิธีที่ 2: Make executable
chmod +x repo_manager.py
./repo_manager.py
```

</div>

---

## 📖 คู่มือการใช้งาน (How to Use)

### 🎯 ขั้นตอนพื้นฐาน

#### 1. 🛠️ ตั้งค่าเริ่มต้น
- **📁 เลือกโฟลเดอร์**: คลิก "เลือก" เพื่อเลือกโฟลเดอร์โปรเจค Git
- **🔑 ใส่ Token**: วาง GitHub Personal Access Token ในช่อง "GitHub Token"
- **🔍 ตรวจสอบ**: คลิก "ตรวจสอบ" เพื่อยืนยันการตั้งค่า

#### 2. 🚀 การใช้งานหลัก

<table>
<tr>
<td width="50%">

**📤 อัปโหลดไฟล์**
- คลิก "📤 อัปโหลดไฟล์"
- ระบบจะทำ:
  - `git add .`
  - `git commit` พร้อมเวลา
  - `git push` ไปยัง repository

</td>
<td width="50%">

**🎯 สร้าง Release**
- คลิก "🎯 สร้าง Release"
- เลือกเวอร์ชัน (v1.0.0, v1.1.0, ฯลฯ)
- ระบบสร้าง changelog อัตโนมัติ
- Release พร้อมใช้บน GitHub

</td>
</tr>
</table>

#### 3. ⚡ วิธีใช้แบบ Pro

<details>
<summary><b>🔽 คลิกเพื่อดู Pro Tips</b></summary>

**🚀 ทำทั้งหมด (Do All)**
- คลิกปุ่มเดียว = Push + Release
- ประหยัดเวลา เหมาะสำหรับการพัฒนาแบบเร็ว
- ระบบจะทำงานเป็นขั้นตอน แสดงสถานะชัดเจน

**🔒 Private/Public Repository**
- เลือก checkbox "ความเป็นส่วนตัว"
- หรือใช้ปุ่ม "🔄 Private/Public" สลับเร็ว
- เหมาะสำหรับงานที่ต้องการความเป็นส่วนตัว

**📊 ติดตาม Real-time**
- หน้าต่าง Log แสดงสถานะแบบเรียลไทม์
- เห็นความคืบหน้าของการทำงาน
- แจ้งเตือนเมื่อเสร็จสิ้น

</details>

---

## 🔧 การแก้ไขปัญหา (Troubleshooting)

<div align="center">

### 🚨 ปัญหาที่พบบ่อย

</div>

<details>
<summary><b>❌ GitHub Token Error 403</b></summary>

**อาการ:** ไม่สามารถสร้าง Release ได้
**สาเหตุ:** Token ไม่มีสิทธิ์ `repo` scope

**✅ วิธีแก้:**
1. สร้าง Token ใหม่ที่ https://github.com/settings/tokens/new
2. เลือก scope `repo` (Full control of repositories)
3. อัปเดตไฟล์ `.env`
4. รีสตาร์ทโปรแกรม

**📄 คู่มือเต็ม:** ดูไฟล์ `QUICK_FIX.txt`

</details>

<details>
<summary><b>🔴 Git Command Failed</b></summary>

**อาการ:** ไม่สามารถ push ได้
**สาเหตุ:** Git ไม่ได้ตั้งค่าหรือไม่มี remote

**✅ วิธีแก้:**
```bash
# ตั้งค่า Git user
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# ตรวจสอบ remote
git remote -v

# เพิ่ม remote หากไม่มี
git remote add origin https://github.com/username/repo-name.git
```

</details>

<details>
<summary><b>🟡 Repository Not Found</b></summary>

**อาการ:** ไม่พบ repository บน GitHub
**สาเหตุ:** Repository ยังไม่ถูกสร้าง

**✅ วิธีแก้:**
1. ใช้ปุ่ม "🔨 สร้าง Repository" ในโปรแกรม
2. หรือสร้างใน GitHub.com ก่อน
3. ตรวจสอบชื่อ Owner และ Repository ให้ถูกต้อง

</details>

---

## 🎨 ธีมและการปรับแต่ง (Themes & Customization)

<div align="center">

### 🌙 GitHub Dark Theme

โปรแกรมใช้ธีมสีเข้มแบบ GitHub ที่ออกแบบมาให้:
- 👁️ สบายตาในการใช้งานยาวๆ
- 💻 เข้ากับสภาพแวดล้อมการพัฒนา
- 🎯 โฟกัสกับงานได้ดีขึ้น

</div>

---

## 🤝 การมีส่วนร่วม (Contributing)

<div align="center">

**🚀 ต้องการช่วยพัฒนาโปรเจคนี้?**

</div>

### 📋 วิธีการช่วยเหลือ
1. 🍴 **Fork** repository นี้
2. 🌿 สร้าง **branch** ใหม่สำหรับฟีเจอร์ (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** การเปลี่ยนแปลง (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** ไปยัง branch (`git push origin feature/AmazingFeature`)
5. 🎯 เปิด **Pull Request**

### 🔍 สิ่งที่เรากำลังมองหา
- 🐛 **Bug Fixes** - แก้ไขข้อผิดพลาด
- ✨ **New Features** - ฟีเจอร์ใหม่ที่น่าสนใจ
- 📖 **Documentation** - ปรับปรุงเอกสาร
- 🎨 **UI/UX Improvements** - ปรับปรุงหน้าตา
- 🔧 **Performance** - เพิ่มประสิทธิภาพ

---

## 📄 สัญญาอนุญาต (License)

<div align="center">

### 📋 MIT License

**🎉 ใช้งานได้อย่างอิสระ!**

โปรเจคนี้อยู่ภายใต้ [MIT License](LICENSE) - ดูรายละเอียดในไฟล์ LICENSE

**✅ สิ่งที่ทำได้:**
- ✨ ใช้งานเชิงพาณิชย์
- 🔄 แก้ไขและดัดแปลง
- 📦 แจกจ่ายต่อ
- 🔒 ใช้งานส่วนตัว

**📋 เงื่อนไข:**
- 📄 ระบุที่มาและสัญญาอนุญาต
- ⚖️ ความรับผิดชอบตามกฎหมาย

</div>

---

## 👨‍💻 ผู้พัฒนา (Developer)

<div align="center">

### 💎 ZirconX

**🚀 Passionate Developer | 🛠️ Open Source Enthusiast**

[![GitHub](https://img.shields.io/badge/GitHub-ZXD44-black?style=for-the-badge&logo=github)](https://github.com/ZXD44)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

### 💭 คำขอบคุณ

ขอบคุณทุกคนที่ใช้งานและสนับสนุนโปรเจคนี้! 

**🌟 หากโปรเจคนี้มีประโยชน์ กรุณา Star ⭐ ให้กำลังใจผู้พัฒนา**

*Made with ❤️ in Thailand 🇹🇭*

</div>

---

<div align="center">

### 🎯 เวอร์ชันปัจจุบัน: v1.1.0

**📅 อัปเดตล่าสุด:** กันยายน 2025

**🔄 Changelog:** ดู [Releases](https://github.com/ZXD44/repo-manager/releases) บน GitHub

**📚 เอกสารเพิ่มเติม:**
- [FEATURES.md](FEATURES.md) - รายละเอียดฟีเจอร์ Private/Public
- [QUICK_FIX.txt](QUICK_FIX.txt) - คู่มือแก้ไขปัญหา Token

</div>
