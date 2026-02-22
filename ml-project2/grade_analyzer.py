def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages
def classify_grades(averages):
    classified = {}
    A_THRESHOLD = 90
    B_THRESHOLD = 75
    C_THRESHOLD = 60
   
    for name, avg in averages.items():
        if avg >= A_THRESHOLD:
            grade = "A"
        elif avg >= B_THRESHOLD:
            grade = "B"
        elif avg >= C_THRESHOLD:
            grade = "C"
        else:
            grade = "F"
        
        classified[name] = (avg, grade)
    
    return classified

def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    passed = 0
    total = len(classified)
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1
        
        print(f"{name:<10} | Avg: {avg:<6} | Grade: {grade} | Status: {status}")
    
    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {total - passed}")
    
    return passed
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 98, 96]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
