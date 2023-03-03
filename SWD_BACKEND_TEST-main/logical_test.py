
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


# ฟังก์ชันแปลงเลขเป็นภาษาไทย
def convert_to_thai_text(number):
    
    numText = list(str(number))
    TenState = True
    index = ["","สิบ","ร้อย","พัน","หมื่น","แสน","ล้าน"]
    numeric = ["","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]

    count = 0
    countIndex = len(numText) - len(index) - 1
    
    if countIndex >= 0 :
        return 'เกิน 10 ล้าน'
    
    TenState = True
    
    for i in numText:
        #จะทำในกรณี number มีค่ามากกว่า 2
        if number >= 2:
            
            
            if i == "0":
                numText[count] = ''
                #ถ้ากรณี 0 อยู่ในตำแหน่งหลักสิบ ให้เปลี่ยนเปลี่ยน TenState เป็น false
                if index[countIndex] == "สิบ":
                    TenState = False
            #ถ้า value i == 1 และ index == สิบ ให้เปลี่ยน เป็น สิบ
            elif i == "1" and index[countIndex] == "สิบ":
                numText[count] = "สิบ"
            
            #ถ้า value i == 2 และ index == สิบ ให้เปลี่ยน เป็น ยี่สิบ
            elif i == "2" and index[countIndex] == "สิบ":
                numText[count] = "ยี่สิบ"
            
            #ถ้า value i == 1 และ index == "" หรือ หลักหน่วย ให้เปลี่ยน เป็น เอ็ด
            elif i == "1" and index[countIndex] == "" and TenState:
                numText[count] = "เอ็ด"
            else :
            #จะทำการนำค่า count มาเป็น index ของ numtext และเป็น เป็น integer เพื่อนำไปหาค่าใน numeric และ index ตามตำแหน่ง
                print(numeric[int(numText[count])] , " " , index[countIndex])
                numText[count] = numeric[int(numText[count])] + index[countIndex]  
        else:
            if number == 0:
                numText = ["ศูนย์"]
            if number == 1:
                numText = ["หนึ่่ง"]
        # print(i, "  ",numText[count],"  " ,index[countIndex] )
        count = count + 1
        countIndex = countIndex - 1
        print(numText)
        
    return "".join(numText)
# รับค่าจากผู้ใช้และแสดงผลลัพธ์

if __name__ == '__main__':
    number = int(str(input('ป้อนเลขที่ต้องการแปลงเป็นภาษาไทย (ตัวเลข 0-9999999): ')))
    # if not(number < 0 or number > 9999999):
    # number = 
    print("Number => "+ str(number) +", Thai text => "+ convert_to_thai_text(number))





