#8.Program to give feedback on users's score.
score = float(input("Enter your score(0-100):"))

if 90<= score <= 100:
    grade = "A"
elif 80 <= score <= 90:
    grade = "B"  
elif 70<= score <= 80:
    grade = "C"
elif 60<= score <= 70:
    grade = "D" 
elif 0 <= score < 60:
    grade = "F"
else :
    grade = None

if grade:
    print(f"CONGRATULATIONS! Your grade is : {grade}") 
else :
    print ("Invalid score. Please enter the correct number ")                       