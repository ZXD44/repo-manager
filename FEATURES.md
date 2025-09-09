# 🆕 ฟีเจอร์ใหม่ - Private/Public Repository Selection

## 🔒 เลือกความเป็นส่วนตัว Repository

**Repo Manager** ตอนนี้รองรับการเลือกว่าจะสร้าง Repository แบบ **Private** หรือ **Public**!

---

## 🔧 การใช้งาน

### 1. Checkbox ความเป็นส่วนตัว
ในส่วนการตั้งค่า คุณจะพบ checkbox:
```
🔒 ความเป็นส่วนตัว: ☐ สร้าง Repository แบบส่วนตัว (Private)
💡 Private = เฉพาะคุณเท่านั้น | Public = ทุกคนเห็นได้
```

### 2. สลับอย่างรวดเร็ว
ใช้ปุ่ม **"🔄 Private/Public"** ในแถบเครื่องมือเพื่อสลับการตั้งค่าได้อย่างรวดเร็ว

### 3. แสดงสถานะ
เมื่อใช้ปุ่ม **"🔍 ตรวจสอบ"** โปรแกรมจะแสดง:
```
🔒 การตั้งค่าความเป็นส่วนตัว: ส่วนตัว (Private)
```
หรือ
```
🔒 การตั้งค่าความเป็นส่วนตัว: สาธารณะ (Public)
```

---

## 🔐 ความแตกต่างระหว่าง Private และ Public

| ประเภท | การเข้าถึง | เหมาะสำหรับ | ข้อจำกัด |
|--------|------------|-------------|----------|
| **🔒 Private** | เฉพาะคุณและผู้ที่ได้รับอนุญาต | โปรเจคส่วนตัว, งานบริษัท, โค้ดที่ยังไม่พร้อม | มีข้อจำกัดในแผนฟรี |
| **🌐 Public** | ทุกคนสามารถเห็นและดาวน์โหลดได้ | โปรเจค Open Source, Portfolio, ตัวอย่างโค้ด | ไม่จำกัด |

---

## 💡 เคล็ดลับ

### ⚠️ สิ่งที่ควรรู้
- การตั้งค่านี้จะมีผลเฉพาะกับ **Repository ที่จะสร้างใหม่** เท่านั้น
- Repository ที่มีอยู่แล้วสามารถเปลี่ยนได้ในหน้า Settings ของ GitHub
- GitHub แผนฟรีจำกัดจำนวน Private Repository

### 🎯 แนะนำการใช้งาน

#### สำหรับ Private Repository:
- ✅ โปรเจคงาน/บริษัท
- ✅ การทดลองและพัฒนา
- ✅ ข้อมูลที่มีลิขสิทธิ์
- ✅ โค้ดที่ยังไม่เสร็จ

#### สำหรับ Public Repository:
- ✅ โปรเจค Open Source
- ✅ Portfolio และผลงาน
- ✅ ตัวอย่างการเขียนโค้ด
- ✅ Documentation และ Tutorial

---

## 🔄 การเปลี่ยนแปลงในโค้ด

### การเปลี่ยนแปลงหลัก:
1. **เพิ่มพารามิเตอร์ `is_private`** ในฟังก์ชัน `create_repo()`
2. **เพิ่มตัวแปร `self.is_private`** สำหรับเก็บสถานะ
3. **เพิ่ม Checkbox UI** สำหรับเลือกความเป็นส่วนตัว
4. **เพิ่มปุ่ม Toggle** สำหรับสลับการตั้งค่า
5. **ปรับปรุงข้อความแจ้งเตือน** ให้แสดงสถานะความเป็นส่วนตัว

### ตัวอย่างการใช้งาน:
```python
# เมื่อสร้าง repository
privacy_type = "ส่วนตัว (Private)" if self.is_private.get() else "สาธารณะ (Public)"
self.log(f"🔨 กำลังสร้าง repository แบบ{privacy_type}...")
response = self.api.create_repo(self.repo_name.get(), self.is_private.get())
```

---

## 🚀 การใช้งานขั้นสูง

### เปลี่ยนการตั้งค่าหลังสร้าง Repository
หากต้องการเปลี่ยนความเป็นส่วนตัวของ Repository ที่มีอยู่แล้ว:

1. ไปที่ GitHub.com
2. เข้า Repository ที่ต้องการ
3. Settings → General
4. เลื่อนลงไปหา "Danger Zone"
5. เลือก "Change repository visibility"

### การจัดการ Collaborators (Private Repository)
สำหรับ Private Repository ที่ต้องการแชร์:
1. Settings → Manage access
2. กด "Invite a collaborator"
3. ใส่ username หรือ email
4. เลือกสิทธิ์ (Read, Write, Admin)

---

*อัพเดทโดย ZirconX | Version 0.0.2 - เพิ่มฟีเจอร์ Private/Public Selection*
