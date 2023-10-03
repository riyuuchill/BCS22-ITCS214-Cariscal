pasado = 0
bagsak = 0
record = [["Name", "Q1", "Q2", "Q3", "Class Participation", "Final Exam", "Grade", "Status"]]


while True:
    name = input("Enter Student's Name: ")
    q1 = int(input("Enter 1st Quarter Grade: "))
    q2 = int(input("Enter 2nd Quarter Grade: "))
    q3 = int(input("Enter 3rd Quarter Grade: "))
    cp = int(input("Enter Class Participation: "))
    finals = int(input("Enter Final Exam Grade: "))

    quizzes = (q1 + q2 + q3)/3
    total = (quizzes * .40) + (cp * .20) + (finals * .40)

    if total >= 70:
        status = "Passed"
    else:
        status = "Failed"

    grade = f"{total:.1f}"

    records = [name, q1, q2, q3, cp, finals, grade, status]

    record.append(records)

    new = input("Do you want to enter another student (Yes or No): ").lower()

    if new == "yes":
        continue
    elif new == "no":
        break
    else:
        print("Invalid Input")

for column in range(len(record)):
    display = "| {0:^5} | {1:^5} | {2:^5} | {3:^5} | {4:^20} | {5:^10} | {6:^7} | {7:^7}"
    print(display.format((record[column][0]), (record[column][1]), (record[column][2]), (record[column][3]), (record[column][4]), (record[column][5]), (record[column][6]), (record[column][7])))

for column in range(len(record)):
    if record[column][7].lower() == "passed":
        pasado += 1
    elif record[column][7].lower() == "failed":
        bagsak += 1
    else:
        continue    

print(f"There are {pasado} students who passed the Midterm Period")
print(f"There are {bagsak} students who failed the Midterm Period")
