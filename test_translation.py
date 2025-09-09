#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ทดสอบฟังก์ชันแปลภาษา
def translate_commit_message(commit):
    """แปลคำสำคัญใน commit message เป็นภาษาไทย"""
    # Dictionary สำหรับแปล
    translations = {
        # คำสำคัญทั่วไป
        'fix': '🔧 แก้ไข',
        'Fix': '🔧 แก้ไข', 
        'FIX': '🔧 แก้ไข',
        'add': '➕ เพิ่ม',
        'Add': '➕ เพิ่ม',
        'ADD': '➕ เพิ่ม',
        'update': '🔄 อัปเดต',
        'Update': '🔄 อัปเดต',
        'UPDATE': '🔄 อัปเดต',
        'remove': '❌ ลบ',
        'Remove': '❌ ลบ',
        'REMOVE': '❌ ลบ',
        'Enhanced': '⚡ ปรับปรุง',
        'Release': '🚀 รีลีส',
        'GitHub': 'GitHub',
        'API': 'API',
        'Log': 'ล็อก',
        'System': 'ระบบ',
        'Enhancement': 'การปรับปรุง',
        'Security': 'ความปลอดภัย',
        'Improvements': 'การปรับปรุง',
        'Simplified': '🎯 ทำให้ง่าย',
        'Notes': 'บันทึก',
        'Before': 'ก่อน',
        'After': 'หลัง',
        'Comparison': 'การเปรียบเทียบ',
        'vs': 'กับ',
        'Complete': 'สมบูรณ์',
        'prep': 'เตรียม'
    }
    
    # แปลทีละคำ
    words = commit.split()
    translated_words = []
    
    for word in words:
        # ลบเครื่องหมาย punctuation ออกก่อนแปล
        clean_word = word.strip('.,!?:;')
        punct = word[len(clean_word):]  # เก็บเครื่องหมายไว้
        
        if clean_word in translations:
            translated_words.append(translations[clean_word] + punct)
        else:
            translated_words.append(word)
    
    return ' '.join(translated_words)

# ทดสอบกับ commits จริง
test_commits = [
    "ccd4548  Simplified Release Notes v1.2.0 - Before vs After Comparison",
    "2e9ced0  Release v1.2.0 - Complete GitHub API & Log System Enhancement",
    "a1980ef Update - 2025-09-09 14:22:14",
    "2e49611  Enhanced Log System & Security Improvements",
    "1831c7b Release prep - 2025-09-09 13:47:30"
]

print("🔄 ทดสอบการแปล Commit Messages:\n")
for commit in test_commits:
    translated = translate_commit_message(commit)
    print(f"Original:  {commit}")
    print(f"แปลแล้ว:   {translated}")
    print("-" * 80)

# ทดสอบ changelog
print("\n📋 ตัวอย่าง Changelog ที่จะได้:")
print("## 📋 การเปลี่ยนแปลงในเวอร์ชันนี้\n")
for commit in test_commits:
    translated = translate_commit_message(commit)
    print(f"- {translated}")
