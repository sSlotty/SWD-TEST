
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def convert_to_roman_numeral(number):
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    result = ""
    for value, numeral in roman_numerals.items():
        #หารเอาจำนวนเต็ม
        count = number // value 
        #เพิ่มตัวอักษร โดยการนำ numeral คูณกับ count เมื่อ count = 1 => numeral จะเพิ่มตามจำนวน count หาก count = 0 => numeral จะไม่เพิ่มเพราะ numeral x count = ค่าว่าง เนื่องจาก count = 0
        result += numeral * count 
        #นำ value x count เมื่อ count = 1 => number จะลดลงตามจำนวน value ที่คูณได้ หาก count = 0 => number จะไม่เปลี่ยนแปลงเพราะ value x count = 0
        number -= value * count 
        
        
    return result

if __name__ == "__main__":
    number = 987
    print(convert_to_roman_numeral(number))