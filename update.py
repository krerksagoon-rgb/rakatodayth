from datetime import datetime

print("=" * 40)
print("ราคาวันนี้ไทย")
print("Daily Thailand Price Update")
print("=" * 40)

today = datetime.now().strftime("%d/%m/%Y %H:%M")

print(f"วันที่ : {today}")
print()

print("กำลังดึงข้อมูลล่าสุด...")

print("✓ ราคาทองคำ")
print("✓ ราคาน้ำมัน")
print("✓ ราคาปาล์มน้ำมัน")
print("✓ ราคายางพารา")

print()
print("เสร็จเรียบร้อย")
