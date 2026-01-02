choice = int(input("Enter 1 to write to file or 2 to read the students.txt file: "))

match(choice):
    case 1:
        n = int(input("Enter total number of students you would like to store: "))
        students = []
        student = {}
        for i in range(n):
            name = input(f"Enter {i+1} student's name: ")
            dept = input(f"Enter {i+1} student's department: ")
            rnum = input(f"Enter {i+1} student's rollnumber: ")
            student = {"Name" : name, "Department": dept, "Rollnumber": rnum}
            students.append(student)

        for s in students:
            print(f"{s['Name']} with rollnumber {s['Rollnumber']} is in {s['Department']}.")

        with open("students.txt","a") as file:
            for s in students:
                file.write(f"{s['Rollnumber']}, {s['Name']}, {s['Department']}\n")
    case 2:
        with open("students.txt") as rfile:
            for line in rfile:
                print(f'{line.rstrip().split(",")[0]} - {line.rstrip().split(",")[1]} is in {line.rstrip().split(",")[2]} Department.')