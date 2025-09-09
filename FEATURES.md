<div align="center">

# 🆕 ฟีเจอร์ใหม่ - Private/Public Repository Selection

## 🔒 เลือกความเป็นส่วนตัว Repository อย่างง่ายดาย!

<p align="center">
  <img src="https://img.shields.io/badge/Feature-Private%2FPublic%20Selection-brightgreen?style=for-the-badge" alt="Feature">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/UI-User%20Friendly-blue?style=for-the-badge" alt="UI">
</p>

**🎯 ตอนนี้ Repo Manager รองรับการเลือกว่าจะสร้าง Repository แบบ Private หรือ Public แล้ว!**

---

</div>

## 🔧 วิธีการใช้งาน

<table>
<tr>
<td align="center" width="50%">

### ☑️ Checkbox ความเป็นส่วนตัว
ในส่วนการตั้งค่า คุณจะพบ checkbox:

```
🔒 ความเป็นส่วนตัว: ☐ สร้าง Repository แบบส่วนตัว (Private)
💡 Private = เฉพาะคุณเท่านั้น | Public = ทุกคนเห็นได้
```

**✅ เลือก:** Repository จะเป็น Private  
**❌ ไม่เลือก:** Repository จะเป็น Public

</td>
<td align="center" width="50%">

### 🔄 ปุ่มสลับอย่างรวดเร็ว
ใช้ปุ่ม **"🔄 Private/Public"** ในแถบเครื่องมือ

**🚀 ความสะดวก:**
- สลับได้ในคลิกเดียว
- ไม่ต้องหา checkbox
- เหมาะสำหรับการเปลี่ยนแปลงบ่อยๆ

</td>
</tr>
</table>

### 🔍 การแสดงสถานะ

เมื่อใช้ปุ่ม **"🔍 ตรวจสอบ"** โปรแกรมจะแสดง:

<div align="center">

| สถานะ | ข้อความที่แสดง |
|-------|---------------|
| 🔒 **Private** | `🔒 การตั้งค่าความเป็นส่วนตัว: ส่วนตัว (Private)` |
| 🌐 **Public** | `🔒 การตั้งค่าความเป็นส่วนตัว: สาธารณะ (Public)` |

</div>

---

## 🔐 ความแตกต่างระหว่าง Private และ Public

<div align="center">

### 📊 ตารางเปรียบเทียบ

| หัวข้อ | 🔒 **Private Repository** | 🌐 **Public Repository** |
|--------|-------------------------|-------------------------|
| **👥 การเข้าถึง** | เฉพาะคุณและผู้ที่ได้รับอนุญาต | ทุกคนสามารถเห็นและดาวน์โหลดได้ |
| **💰 ค่าใช้จ่าย** | มีข้อจำกัดในแผนฟรี | ไม่จำกัดและฟรี |
| **🎯 เหมาะสำหรับ** | งานส่วนตัว, บริษัท, โค้ดลับ | Open Source, Portfolio, ตัวอย่าง |
| **🔍 SEO & Discovery** | ค้นหาไม่เจอใน Google | ค้นหาเจอใน Google |
| **📈 GitHub Stats** | ไม่นับในสถิติสาธารณะ | นับในสถิติสาธารณะ |
| **👨‍💻 Collaboration** | เชิญคนเข้ามาได้ | ใครก็ Fork ได้ |

</div>

---

## 💡 เคล็ดลับและคำแนะนำ

### ⚠️ สิ่งที่ควรรู้

<details>
<summary><b>🔽 คลิกเพื่อดูข้อมูลสำคัญ</b></summary>

**📌 เกี่ยวกับการตั้งค่า:**
- การตั้งค่านี้จะมีผลเฉพาะกับ **Repository ที่จะสร้างใหม่** เท่านั้น
- Repository ที่มีอยู่แล้วสามารถเปลี่ยนได้ในหน้า Settings ของ GitHub
- GitHub แผนฟรีจำกัดจำนวน Private Repository (ตรวจสอบ quota ปัจจุบัน)

**🔒 เกี่ยวกับ Private Repository:**
- ต้องใช้ GitHub Token ที่มี `repo` scope เสมอ
- สามารถเชิญ Collaborators เข้ามาได้
- ไฟล์จะไม่ปรากฏใน Google Search

**🌐 เกี่ยวกับ Public Repository:**
- ใครก็เข้าถึงได้โดยไม่ต้อง login
- มีประโยชน์สำหรับการสร้างชื่อเสียง
- เหมาะสำหรับ Open Source Projects

</details>

### 🎯 แนะนำการใช้งาน

<table>
<tr>
<td width="50%">

#### 🔒 ใช้ Private Repository เมื่อ:
- ✅ โปรเจคงาน/บริษัท
- ✅ การทดลองและพัฒนา
- ✅ ข้อมูลที่มีลิขสิทธิ์
- ✅ โค้ดที่ยังไม่เสร็จ
- ✅ เก็บ API Keys หรือข้อมูลลับ
- ✅ โปรเจคส่วนตัวที่ไม่อยากให้ใครเห็น

</td>
<td width="50%">

#### 🌐 ใช้ Public Repository เมื่อ:
- ✅ โปรเจค Open Source
- ✅ Portfolio และผลงาน
- ✅ ตัวอย่างการเขียนโค้ด
- ✅ Documentation และ Tutorial
- ✅ เครื่องมือที่อยากแชร์
- ✅ ต้องการ SEO และการค้นหา

</td>
</tr>
</table>

---

## 🔄 การเปลี่ยนแปลงในโค้ด

<div align="center">

### 🛠️ การปรับปรุงทางเทคนิค

</div>

<details>
<summary><b>🔽 คลิกเพื่อดูรายละเอียดการพัฒนา</b></summary>

### การเปลี่ยนแปลงหลัก:

1. **🔧 เพิ่มพารามิเตอร์ `is_private`** ในฟังก์ชัน `create_repo()`
   ```python
   def create_repo(self, repo_name, is_private=False):
       data = {
           'name': repo_name,
           'private': is_private,  # 🆕 ใหม่!
           'auto_init': True
       }
   ```

2. **📊 เพิ่มตัวแปร `self.is_private`** สำหรับเก็บสถานะ
   ```python
   self.is_private = tk.BooleanVar(value=False)
   ```

3. **🖱️ เพิ่ม Checkbox UI** สำหรับเลือกความเป็นส่วนตัว
   ```python
   self.private_checkbox = tk.Checkbutton(
       text="🔒 สร้าง Repository แบบส่วนตัว (Private)",
       variable=self.is_private
   )
   ```

4. **🔄 เพิ่มปุ่ม Toggle** สำหรับสลับการตั้งค่า
   ```python
   def toggle_privacy(self):
       current = self.is_private.get()
       self.is_private.set(not current)
   ```

5. **📝 ปรับปรุงข้อความแจ้งเตือน** ให้แสดงสถานะความเป็นส่วนตัว
   ```python
   privacy_type = "ส่วนตัว (Private)" if self.is_private.get() else "สาธารณะ (Public)"
   self.log(f"🔨 กำลังสร้าง repository แบบ{privacy_type}...")
   ```

</details>

---

## 🚀 การใช้งานขั้นสูง

### 🔧 เปลี่ยนการตั้งค่าหลังสร้าง Repository

<div align="center">

**💡 หากต้องการเปลี่ยนความเป็นส่วนตัวของ Repository ที่มีอยู่แล้ว:**

</div>

<details>
<summary><b>🔽 คลิกเพื่อดูขั้นตอน</b></summary>

1. **🌐 ไปที่ GitHub.com**
2. **📂 เข้า Repository ที่ต้องการ**
3. **⚙️ Settings → General**
4. **⬇️ เลื่อนลงไปหา "Danger Zone"**
5. **🔄 เลือก "Change repository visibility"**
6. **✅ ยืนยันการเปลี่ยนแปลง**

**⚠️ หมายเหตุ:** การเปลี่ยนจาก Private เป็น Public ทำได้เสมอ แต่การเปลี่ยนกลับอาจมีข้อจำกัดตาม GitHub plan

</details>

### 👥 การจัดการ Collaborators (Private Repository)

<div align="center">

**🤝 สำหรับ Private Repository ที่ต้องการแชร์:**

</div>

<details>
<summary><b>🔽 คลิกเพื่อดูวิธีเชิญคนอื่น</b></summary>

1. **📂 เข้า Repository บน GitHub**
2. **⚙️ Settings → Manage access**
3. **➕ กด "Invite a collaborator"**
4. **👤 ใส่ username หรือ email**
5. **🔐 เลือกสิทธิ์:**
   - **Read:** อ่านได้อย่างเดียว
   - **Write:** อ่าน + เขียนได้
   - **Admin:** ควบคุมทั้งหมด

**💡 เคล็ดลับ:** ใช้สิทธิ์ "Write" สำหรับคนที่ทำงานร่วมกัน และ "Read" สำหรับคนที่ต้องการดูโค้ดเท่านั้น

</details>

---

<div align="center">

## 🎉 สรุป

**🔒 Private Repository:** เหมาะสำหรับงานที่ต้องการความเป็นส่วนตัว  
**🌐 Public Repository:** เหมาะสำหรับงานที่ต้องการแชร์และโชว์

**⚡ ความสะดวก:** สลับได้ง่ายผ่าน UI ที่ใช้งานง่าย!

---

*🚀 Repo Manager - ทำให้การจัดการ GitHub ง่ายขึ้นทุกวัน!*

**Made with ❤️ by ZirconX**

</div>
