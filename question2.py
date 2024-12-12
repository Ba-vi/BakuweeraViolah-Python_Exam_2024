# section B
# question2 i)
def student_details():
    student_name = input("Enter the student name:")
    student_number= int(input("Enter the students number: "))
    programming_mark = int(input("Enter the student programming mark: "))
    data_science_mark =int(input("Enter the student data_science mark: "))
    computer_application_mark =int(input("Enter the student computer_application_mark: "))
    average_mark=(programming_mark+data_science_mark+computer_application_mark)/3
    print(f"The average mark of the student { student_name} with student number {student_number} is: {average_mark}")
student_details()  


# question2
#ii
def milesPerGallons():
    milesDriven=int(input("Enter the number of miles driven: "))
    gallonsOfGasUsed=int(input("Enter the number of gallons of gas used:  "))
    mpg=milesDriven/gallonsOfGasUsed
    print(f"The  value of the car's miles per gallons is : {mpg}")
milesPerGallons()


# question2
#iii
def odd_numbers():
    for num in range (1,101):
        if num %2 !=0:
            print(num)
odd_numbers()

    
