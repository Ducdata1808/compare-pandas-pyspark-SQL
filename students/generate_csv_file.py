import pandas as pd
import random
import uuid # Để tạo student_id duy nhất

# --- Cấu hình ---
num_students = 100 # Số lượng sinh viên muốn tạo
output_csv_filename = "students.csv"

# --- Danh sách các giá trị có thể có ---
majors = [
    "Computer Science", "Electrical Engineering", "Mechanical Engineering",
    "Civil Engineering", "Business Administration", "Marketing",
    "Finance", "Accounting", "Data Science", "Artificial Intelligence",
    "Biomedical Engineering", "Chemistry", "Physics", "Mathematics",
    "Literature", "History", "Psychology", "Sociology", "Economics"
]
years = [1, 2, 3, 4] # Năm học

# --- Tạo dữ liệu ---
data = []
for _ in range(num_students):
    student_id = str(uuid.uuid4())[:8] # Tạo ID duy nhất, cắt ngắn để dễ nhìn
    name = f"SinhVien {random.randint(1, 999)}" # Tên ngẫu nhiên
    major = random.choice(majors) # Ngành học ngẫu nhiên
    score = round(random.uniform(2.0, 4.0), 2) # Điểm trung bình (GPA) từ 2.0 đến 4.0, làm tròn 2 chữ số thập phân
    year = random.choice(years) # Năm học ngẫu nhiên

    data.append({
        "student_id": student_id, # mã sinh viên
        "name": name,             # tên
        "major": major,           # ngành học
        "score": score,           # điểm trung bình (GPA)
        "year": year              # năm học (1, 2, 3, 4)
    })

# --- Tạo DataFrame từ dữ liệu đã tạo ---
df = pd.DataFrame(data)

# --- Ghi DataFrame ra file CSV ---
# index=False để không ghi cột index của DataFrame vào file CSV
# encoding='utf-8' để hỗ trợ các ký tự tiếng Việt hoặc ký tự đặc biệt khác
df.to_csv(output_csv_filename, index=False, encoding='utf-8')

print(f"Đã tạo thành công file '{output_csv_filename}' với {num_students} bản ghi.")
print("Vài dòng đầu tiên của DataFrame:")
print(df.head())