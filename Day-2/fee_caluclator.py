def fee_calculator(course,marks):
    if course == 'AI':
        fee=50000
    elif course=='WEB':
        fee=30000
    elif course=='Data Analyst':
        fee=40000
    else:
        return None
    
    if marks > 90:
        fee = fee-5000
    return fee

def main():
    course=input("Enter Course : ")
    marks=int(input("Enter Marks : "))

    fee= fee_calculator(course,marks)

    if fee is None:
        print("Invalid Course Selected ")
    else:
        print(" Final fee : ",fee)
    
main()