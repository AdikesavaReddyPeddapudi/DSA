student_name=""
student_status=""

def show_menu():
    print("\n ----Attendance Tracker------- ")
    print("1.Add Attendance ")
    print("2.View Attendance ")
    print("3.Exit ")
def add_attendance():
    global student_name
    global student_status

    student_name=input("Enter Student Name : ")
    student_status=input("Enter Student Status (Present or absent) : ")

    print("Attendance Added saucessfully. ")

def view_attendance():
    if student_name ==" ":
        print(" No Record found.")
    else:
        print("\n ------ Attendance Record -------")
        print(student_name," - ",student_status)



def main():
    while True:
        show_menu()
        choice=input("Enter your Choice : ")
        
        if choice == "1":
            add_attendance()
        elif choice =="2":
            view_attendance()
        elif choice =="3":
            print("Exiting the program ")
            break
        else:
            print("Invalid choice , Try Again ")
main()