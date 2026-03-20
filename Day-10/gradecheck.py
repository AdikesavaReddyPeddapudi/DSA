
name=input("Enter The Student Name : ")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['django']
        avg=sum/3
        if avg > 90:
            print(f'Congrats {name},You got First Class')
        elif avg >= 75:
            print(f'Good {name}, Wish you All the Best')
        elif avg >= 50:
            print(f'{name},need improvement')
        elif avg >= 35:
            print(f'{name}, work hard next time ')
        else:
            print(f'{name},you have failed in the exam, bring your paarents')
    else:
        print(f'{name},iis Absent for the Exam ')
else:
    print(f'{name},data not found')
