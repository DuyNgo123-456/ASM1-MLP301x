# Gọi thư viện để xử lý tệp và chuỗi
import os
import re

ANSWER_KEY = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')

def read_class_file(): # Tạo hàm để đọc file có dùng xử lý ngoại lệ
    while True:
        class_name = input("Enter a class file to grade (i.e. class1 for class1.txt): ").strip()
        filename = class_name + ".txt"
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            print(f"Successfully opened {filename}")
            return lines, class_name
        except FileNotFoundError:
            print("File cannot be found.")


def analyze_data(lines): # Tạo hàm để đọc từng dòng dữ liệu kiểm tra xem dữ liệu có hợp lệ không?
    print("**** ANALYZING ****")
    valid_data = []
    invalid_count = 0

    for line in lines: # Xử lý dấu ,
        line = line.strip()
        parts = line.split(',')
 
        if len(parts) != 26: # Kiểm tra dòng dữ liệu có chứa 26 ký tự không?
            print("Invalid line of data: does not contain exactly 26 values:")
            print(line)
            invalid_count += 1
            continue

        student_id = parts[0]
        if not re.fullmatch(r"N\d{8}", student_id): # Kiểm tra mã số của học sinh có hợp lệ không?
            print("Invalid line of data: N# is invalid")
            print(line)
            invalid_count += 1
            continue

        valid_data.append(parts)

    if invalid_count == 0:
        print("No errors found!")

    print("**** REPORT ****")
    print(f"Total valid lines of data: {len(valid_data)}")
    print(f"Total invalid lines of data: {invalid_count}")
    return valid_data


def grade_students(valid_data): # Hàm tính điểm từng học sinh trong dữ liệu 
    scores = []
    graded_lines = []

    for parts in valid_data: # Lấy đáp án trong bài làm của học sinh
        student_id = parts[0]
        answers = parts[1:]
        score = 0
        for student_ans, correct_ans in zip(answers, ANSWER_KEY): # Ghép từng câu trả lời của học sinh với đáp án tương ứng
            if student_ans == '': # Đáp án trống thì bỏ qua
                continue  # skipped
            elif student_ans == correct_ans:
                score += 4
            else:
                score -= 1
        scores.append(score)
        graded_lines.append(f"{student_id},{score}")

    return scores, graded_lines


def compute_statistics(scores): #Hàm thống kê điểm của học sinh
    scores.sort()
    mean = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    score_range = highest - lowest
    if len(scores) % 2 == 1: #Tính trung vị
        median = scores[len(scores)//2]
    else:
        mid1 = scores[len(scores)//2 - 1]
        mid2 = scores[len(scores)//2]
        median = (mid1 + mid2) / 2

    print(f"Mean (average) score: {mean:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Range of scores: {score_range}")
    print(f"Median score: {median}")


def write_results_file(class_name, graded_lines): #Hàm viết file output
    output_file = f"{class_name}_grades.txt"
    header = f"# this is what {output_file} should look like"
    with open(output_file, 'w') as f:
        f.write(header + '\n')
        for line in graded_lines:
            f.write(line + '\n')


def main(): #Hàm chính
    lines, class_name = read_class_file()
    valid_data = analyze_data(lines)
    if not valid_data:
        return
    scores, graded_lines = grade_students(valid_data)
    compute_statistics(scores)
    write_results_file(class_name, graded_lines)


if __name__ == "__main__": # Hàm main() chạy trực tiếp
    main()

