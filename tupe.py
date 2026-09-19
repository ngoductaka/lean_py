point = (10, 20)
# Có thứ tự (Ordered): Các phần tử được sắp xếp theo thứ tự cụ thể, truy cập thông qua chỉ số (index bắt đầu từ 0).
# Bất biến (Immutable): Không thể thay đổi, thêm hoặc xóa phần tử sau khi đã tạo.
# Đa dạng kiểu dữ liệu & Cho phép trùng lặp: Một tuple có thể chứa số, chuỗi, boolean, list,... và các giá trị có thể giống nhau.

point = (1920, 1080)
width, height = point
print(type(point))
print(width)
print(height)

my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(my_tuple.count(7))   # 2 (số 7 xuất hiện 2 lần)
print(my_tuple.index(8))   # 3 (số 8 xuất hiện đầu tiên ở index 3)

# Các hàm tích hợp sẵn
print(len(my_tuple))       # 10 (độ dài)
print(min(my_tuple))       # 1
print(max(my_tuple))       # 8
print(sum(my_tuple))       # 49
