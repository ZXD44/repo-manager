# 🚀 Repository & Release Manager

เครื่องมือ GUI สำหรับจัดการ Git repository และสร้าง GitHub releases อย่างง่ายดาย

## ✨ คุณสมบัติ

- **� GitIHub Theme**: ธีมสีแบบ GitHub Dark Mode สวยงาม
- **� Quืick Actions**: ปุ่มหลัก 4 ปุ่มใช้งานง่าย
- **� Eassy Setup**: เลือกโฟลเดอร์และตั้งค่าได้ง่าย ๆ
- **1️⃣ Create Repository**: สร้าง GitHub repository ใหม่
- **2️⃣ Push Files**: Commit และ push ไฟล์อัตโนมัติ
- **3️⃣ Create Release**: สร้าง releases พร้อมตรวจสอบเวอร์ชันซ้ำ
- **4️⃣ Check Status**: ตรวจสอบการตั้งค่าและสถานะ
- **📋 Additional Actions**: เมนูเพิ่มเติมใน dropdown
- **🔄 Auto-increment**: เพิ่มเวอร์ชันอัตโนมัติ
- **📝 Activity Log**: ดูผลการทำงานแบบ real-time
- **💡 Tooltips**: คำแนะนำเมื่อ hover ปุ่ม

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
4. ใส่ชื่อเจ้าของและ Repository
5. ใช้ปุ่มหลักตามลำดับ:
   - **📤 อัปโหลดไฟล์** (อัปโหลดไฟล์)
   - **🎯 สร้าง Release** (สร้าง release)
   - **🚀 ทำทั้งหมด** (ทำทั้งสองอย่าง)

### 🎯 Create Release Options
เมื่อกดปุ่ม **3️⃣ Create Release** จะมีตัวเลือก 2 แบบ:

#### ⚡ Quick Create
- **📋 แสดง existing tags** - ดู tags ที่มีอยู่แล้ว
- **🏷️ เลือกเวอร์ชัน** - แก้ไขเอง หรือใช้ปุ่ม:
  - **Major** (v1.0.0 → v2.0.0) - เปลี่ยนแปลงใหญ่
  - **Minor** (v1.0.0 → v1.1.0) - ฟีเจอร์ใหม่
  - **Patch** (v1.0.0 → v1.0.1) - แก้บัค
- **✅ ตรวจสอบซ้ำ** - ป้องกันเวอร์ชันซ้ำ
- **📝 Preview** - ดู release notes ก่อนสร้าง
- **🚀 สร้างทันที** - กดปุ่มเดียวเสร็จ

#### 🛠️ Custom Create  
- เลือกเวอร์ชันเอง
- เขียน release notes เอง
- ปรับแต่งรายละเอียดได้

### ปุ่มต่าง ๆ ในโปรแกรม

#### 🚀 ปุ่มหลัก (เรียบง่าย ไม่สับสน)
| ปุ่ม | คำอธิบาย |
|------|----------|
| 📤 อัปโหลดไฟล์ | Commit และ push ไฟล์ไปยัง GitHub |
| 🎯 สร้าง Release | สร้าง GitHub release (เร็วหรือกำหนดเอง) |
| 🚀 ทำทั้งหมด | อัปโหลดไฟล์และสร้าง release |

#### 📋 ปุ่มเสริม
| ปุ่ม | คำอธิบาย |
|------|----------|
| 🔍 ตรวจสอบ | ตรวจสอบการตั้งค่าและสถานะ |
| 📋 ดู Releases | เปิดหน้า releases ใน browser |
| ❌ ออก | ออกจากโปรแกรม |

## 📸 หน้าตาโปรแกรม

```
🐙 ตัวจัดการ GitHub Repository                    [พร้อมใช้งาน]
═══════════════════════════════════════════════════════════════

⚙️ การตั้งค่า
📁 โฟลเดอร์โปรเจค: [C:\my-project] [เลือก]
🔑 GitHub Token: [**********] [ช่วยเหลือ]
👤 เจ้าของ: [username]  📦 ชื่อ Repository: [repo-name]

🚀 การดำเนินการ
┌─────────────────┬─────────────────┬─────────────────┐
│   📤 อัปโหลด    │   🎯 สร้าง      │   🚀 ทำทั้งหมด   │
│     ไฟล์        │   Release       │                │
└─────────────────┴─────────────────┴─────────────────┘

[🔍 ตรวจสอบ] [📋 ดู Releases]                    [❌ ออก]

📝 บันทึกการทำงาน                                [ล้าง]
[12:34:56] 🚀 ตัวจัดการ GitHub Repository พร้อมใช้งาน
[12:34:57] 📁 พบ repository: username/repo-name
[12:35:00] 🔧 รันคำสั่ง: git add .
[12:35:01] ✅ อัปโหลดเสร็จสิ้น!
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