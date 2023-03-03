#2.3

numbers = [1, 2, 1, 3, 5, 6, 4,10,20,50,100,5,2,1,3]

max_num = numbers[0]   # เก็บค่าตัวเลขที่มีค่ามากที่สุด
max_index = 0   # เก็บ index ของตัวเลขที่มีค่ามากที่สุด

# วนลูปตรวจสอบค่าตัวเลขที่มีค่ามากที่สุด
for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_index = i

print(f"Index ของตัวเลขที่มีค่ามากที่สุดคือ {max_index}")