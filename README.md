
# Tính toán và phân tích điểm thi (Test Grade Calculator)

## Mô tả
Đây là một chương trình Python dùng để **đọc file điểm danh sách học sinh**, **kiểm tra định dạng dữ liệu**, **chấm điểm dựa trên đáp án đúng**, **thống kê kết quả**, và **ghi kết quả ra file mới**.

##  Cấu trúc dữ liệu đầu vào

- Mỗi dòng trong file `.txt` chứa thông tin 1 học sinh, bao gồm:
  ```
  NXXXXXXXX,Ans1,Ans2,...,Ans25
  ```
  - `NXXXXXXXX` là mã số học sinh (bắt đầu bằng `N`, theo sau là 8 chữ số).
  - `Ans1` đến `Ans25` là các câu trả lời trắc nghiệm, có thể là `A`, `B`, `C`, `D` hoặc để trống.

- File đầu vào được đặt tên như: `class1.txt`, `class2.txt`,...

---
##  Cách hoạt động

Chương trình thực hiện các bước sau:

1. **Yêu cầu người dùng nhập tên lớp** (ví dụ: `class1`).
2. **Đọc file** tương ứng (`class1.txt`) và xử lý dữ liệu.
3. **Kiểm tra định dạng dữ liệu**:
   - Dòng phải có đúng 26 giá trị.
   - Mã học sinh phải theo mẫu `NXXXXXXXX`.
4. **Chấm điểm**:
   - Mỗi câu đúng: +4 điểm
   - Mỗi câu sai: -1 điểm
   - Câu không trả lời: 0 điểm
5. **Thống kê**:
   - Điểm trung bình (Mean)
   - Điểm cao nhất/thấp nhất
   - Khoảng cách điểm (Range)
   - Trung vị (Median)
6. **Ghi kết quả ra file mới** tên là: `class1_grades.txt`
---
##  Ví dụ kết quả (class1_grades.txt)
```
# this is what class1_grades.txt should look like
N12345678,80
N98765432,60
...
```
---
## Chạy chương trình

Chạy trực tiếp bằng IDE hoặc Jupyternotebook trên anaconda:

```bash
python lastname_firstname_grade_the_exams.py
```

Nhập tên lớp khi được yêu cầu:
```
Enter a class file to grade (i.e. class1 for class1.txt): class1
.......
```
---
## Thư viện sử dụng

- `os`: làm việc với file hệ thống
- `re`: kiểm tra định dạng bằng biểu thức chính quy (`regex`)
---
## Ghi chú

- Đảm bảo file dữ liệu `.txt` nằm cùng thư mục với chương trình.
- File đầu ra sẽ tự động được tạo nếu dữ liệu hợp lệ.

---
## Tác giả

- Viết bởi: *Ngô Phạm Thế Duy*  
- Dùng trong: ASM1 - Giới thiệu về Machine Learning - MLP301x.

[Link GitHub]https://github.com/DuyNgo123-456/ASM1-MLP301x





