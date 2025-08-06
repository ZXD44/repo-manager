# 🚀 Repository & Release Manager

เครื่องมือ GUI สำหรับจัดการ Git repository และสร้าง GitHub releases อย่างง่ายดาย

## ✨ คุณสมบัติ

- **🖥️ GUI ใช้งานง่าย**: Interface แบบกราฟิกที่เข้าใจง่าย
- **📁 เลือกโฟลเดอร์**: เลือกโฟลเดอร์โปรเจคได้ง่าย ๆ
- **📤 Push ไฟล์**: Commit และ push ไฟล์ไปยัง GitHub
- **🎯 สร้าง Releases**: สร้าง GitHub releases พร้อม changelog อัตโนมัติ
- **🚀 ทำทั้งหมด**: Push และสร้าง release ในคลิกเดียว
- **🔄 Auto-increment**: เพิ่มเวอร์ชันอัตโนมัติ
- **📝 Log แบบ Real-time**: ดูผลการทำงานแบบ real-time
- **🇹🇭 รองรับภาษาไทย**: Interface เป็นภาษาไทยทั้งหมด

## 📦 การติดตั้งและใช้งาน

### วิธีที่ 1: ใช้ไฟล์ .bat (แนะนำ)
```cmd
run.bat
```

### วิธีที่ 2: รัน Python โดยตรง
```cmd
python repo_manager.py
```

## 🔧 การตั้งค่าเบื้องต้น

### 1. GitHub Personal Access Token
1. ไปที่ [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. คลิก "Generate new token (classic)"
3. เลือก scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
4. Copy token และใส่ในโปรแกรม

### 2. ข้อมูล Repository
- **Owner/User**: ชื่อ GitHub username หรือ organization
- **Repository**: ชื่อ repository
- **โฟลเดอร์โปรเจค**: เลือกโฟลเดอร์ที่มีไฟล์โปรเจค

## 🎮 วิธีใช้งาน

### การใช้งานครั้งแรก
1. รัน `run.bat`
2. เลือกโฟลเดอร์โปรเจค
3. ใส่ GitHub Token
4. ใส่ชื่อ Owner และ Repository
5. คลิก "🚀 ทำทั้งหมด"

### ปุ่มต่าง ๆ ในโปรแกรม

| ปุ่ม | คำอธิบาย |
|------|----------|
| 📤 Push ไฟล์ | Commit และ push ไฟล์ไปยัง GitHub |
| 🎯 สร้าง Release | สร้าง GitHub release ใหม่ |
| 🚀 ทำทั้งหมด | Push ไฟล์และสร้าง release |
| 🔄 รีเฟรช | โหลดข้อมูล repository ใหม่ |
| 📋 ดู Releases | เปิดหน้า releases ใน browser |
| ❌ ออก | ปิดโปรแกรม |

## 📸 หน้าตาโปรแกรม

```
🚀 Repository & Release Manager
========================================

📁 การตั้งค่าโปรเจค
📂 โฟลเดอร์โปรเจค: [C:\my-project] [เลือก]
🔑 GitHub Token: [**********] [ช่วยเหลือ]
👤 Owner/User: [username]
📦 Repository: [repo-name]

⚡ การดำเนินการ
[📤 Push ไฟล์] [🎯 สร้าง Release] [🚀 ทำทั้งหมด]
[🔄 รีเฟรช] [📋 ดู Releases] [❌ ออก]

📝 Log การทำงาน
[12:34:56] 🚀 Repository & Release Manager พร้อมใช้งาน
[12:34:57] 📁 พบ repository: username/repo-name
[12:35:00] 🔧 รันคำสั่ง: git add .
[12:35:01] ✅ Push เสร็จสิ้น!
```

## 🔍 การแก้ไขปัญหา

### ปัญหาที่พบบ่อย

1. **ไม่พบ Python**
   - ติดตั้ง Python จาก [python.org](https://python.org)
   - ตรวจสอบว่าเพิ่ม Python ใน PATH แล้ว

2. **ไม่พบ requests library**
   - โปรแกรมจะติดตั้งอัตโนมัติ
   - หรือรันคำสั่ง: `pip install requests`

3. **GitHub API Error**
   - ตรวจสอบ GitHub Token ว่าถูกต้อง
   - ตรวจสอบ scopes ของ token
   - ตรวจสอบชื่อ repository และ username

4. **Push ไม่สำเร็จ**
   - ตรวจสอบว่าตั้งค่า Git config แล้ว
   - ตรวจสอบสิทธิ์ในการ push

## 📁 ไฟล์ในโปรเจค

| ไฟล์ | คำอธิบาย |
|------|----------|
| `repo_manager.py` | โปรแกรมหลัก GUI |
| `run.bat` | ไฟล์รันโปรแกรมสำหรับ Windows |
| `README.md` | คู่มือการใช้งาน |

## 📝 ข้อกำหนดระบบ

- Windows OS
- Python 3.6+
- Git
- GitHub Personal Access Token
- Python package: `requests` (ติดตั้งอัตโนมัติ)

## 💡 Tips การใช้งาน

- โปรแกรมจะจำข้อมูล repository อัตโนมัติจาก git remote
- สามารถใช้งานกับหลายโปรเจคได้โดยเปลี่ยนโฟลเดอร์
- Log จะแสดงผลการทำงานแบบ real-time
- ระบบจะสร้าง changelog อัตโนมัติจาก git commits

## 🤝 การสนับสนุน

หากพบปัญหาหรือต้องการคุณสมบัติเพิ่มเติม สามารถสร้าง Issue ได้

## 📄 License

MIT License - ใช้งานได้อย่างอิสระ