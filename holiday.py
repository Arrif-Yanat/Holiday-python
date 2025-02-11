import datetime  # นำเข้าโมดูล datetime เพื่อจัดการวันที่

# รายการวันหยุดที่กำหนดไว้ (ในรูปแบบ YYYY-MM-DD)
holidays = [
    "2024-01-01",  # วันปีใหม่
    "2024-04-06",  # วันจักรี
    "2024-04-13",  # วันสงกรานต์
    "2024-04-14",  # วันสงกรานต์
    "2024-04-15",  # วันสงกรานต์
    "2024-05-01",  # วันแรงงาน
    "2024-12-05",  # วันพ่อแห่งชาติ
    "2024-12-31"   # วันสิ้นปี
]

# ฟังก์ชันตรวจสอบว่าวันที่เป็นวันหยุดหรือไม่
def check_holiday(date_str):
    if date_str in holidays:
        return True
    return False

# ฟังก์ชันหลัก
def main():
    print("โปรแกรมตรวจสอบวันหยุด 🎉")
    try:
        # รับอินพุตวันที่จากผู้ใช้
        input_date = input("ป้อนวันที่ (YYYY-MM-DD): ")
        
        # ตรวจสอบว่ารูปแบบวันที่ถูกต้องหรือไม่
        date_obj = datetime.datetime.strptime(input_date, "%Y-%m-%d")
        
        # ตรวจสอบวันหยุด
        if check_holiday(input_date):
            print(f"{input_date} เป็นวันหยุด! 🎊")
        else:
            print(f"{input_date} ไม่ใช่วันหยุด")
    
    except ValueError:
        print("รูปแบบวันที่ไม่ถูกต้อง! โปรดป้อนในรูปแบบ YYYY-MM-DD")

# เริ่มโปรแกรม
main()
