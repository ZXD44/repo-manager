# 🔧 การแก้ไขปัญหา GitHub Token - Error 403

## ❌ ปัญหาที่พบ
```
[09:22:57] ❌ ข้อผิดพลาด: 403
[09:22:57] ❌ {"message":"Resource not accessible by personal access token","documentation_url":"https://docs.github.com/rest/releases/releases#create-a-release","status":"403"}
```

## 🔍 สาเหตุ
**GitHub Token ไม่มีสิทธิ์เพียงพอ** ในการสร้าง Release

## ✅ วิธีแก้ไข

### 1. 🔑 สร้าง GitHub Token ใหม่ที่ถูกต้อง

#### ขั้นตอนการสร้าง Token:
1. ไปที่ GitHub.com → Profile → Settings
2. Developer settings → Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. **ตั้งชื่อ Token:** `Repo Manager Full Access`
5. **เลือก Expiration:** 90 days หรือ No expiration
6. **เลือก Scopes ที่จำเป็น:**

#### 📋 Scopes ที่ต้องเลือก:
- ✅ **`repo`** - Full control of private repositories
  - ✅ repo:status
  - ✅ repo_deployment
  - ✅ public_repo
  - ✅ repo:invite
  - ✅ security_events
- ✅ **`workflow`** - Update GitHub Action workflows (ถ้ามี)
- ✅ **`write:packages`** - Upload packages (ถ้าต้องการ)

### 2. 🔄 อัพเดท Token ในโปรแกรม

#### วิธีที่ 1: แก้ไขไฟล์ .env
```env
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### วิธีที่ 2: ใส่ใหม่ในโปรแกรม
1. เปิด Repo Manager
2. ใส่ Token ใหม่ในช่อง "🔑 GitHub Token"
3. กดปุ่ม "🔍 ตรวจสอบ" เพื่อทดสอบ

### 3. 🧪 ทดสอบ Token

#### ใช้ปุ่มตรวจสอบในโปรแกรม:
```
[เวลา] ✅ GitHub Token พบแล้ว
[เวลา] ✅ Token ใช้งานได้ - ผู้ใช้: YourUsername
[เวลา] ✅ Repository พร้อมใช้งาน
```

#### หรือทดสอบด้วย Command Line:
```bash
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

## 🚨 ข้อควรระวัง

### ⚠️ Token Security
- **อย่าแชร์ Token** กับใครหรือใส่ในโค้ดที่เป็น Public
- **ใช้ .env file** สำหรับเก็บ Token
- **ตั้ง Expiration** เพื่อความปลอดภัย
- **ลบ Token เก่า** ที่ไม่ใช้แล้ว

### 📝 การตรวจสอบ Scopes
ถ้า Token ยังไม่ทำงาน ให้ตรวจสอบว่ามี Scopes นี้:
```
repo (full control)
├── repo:status
├── repo_deployment  
├── public_repo
├── repo:invite
└── security_events
```

## 🔧 การแก้ไขเพิ่มเติมในโค้ด

ฉันจะเพิ่มฟังก์ชันตรวจสอบ Token Scopes ในโปรแกรม เพื่อช่วยตรวจสอบปัญหา

---

## 📞 ถ้ายังไม่สามารถแก้ไขได้

### ตรวจสอบเพิ่มเติม:
1. **Repository เป็น Private หรือไม่?** - ต้องใช้ Token ที่มี repo scope
2. **เป็นเจ้าของ Repository หรือไม่?** - ต้องมีสิทธิ์ write access
3. **Token หมดอายุหรือไม่?** - ตรวจสอบวันหมดอายุ
4. **GitHub มีปัญหาหรือไม่?** - ตรวจสอบที่ https://githubstatus.com/

### วิธีการตรวจสอบเพิ่มเติม:
```bash
# ตรวจสอบ Token และ Scopes
curl -H "Authorization: token YOUR_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/user \
     -I | grep "x-oauth-scopes"
```

---

*Created by ZirconX | วันที่: 9 กันยายน 2025*
