name = input("enter your name: ")
homework = int(input("enter your homework marks: "))
assessment = int(input("enter your assessment marks: "))
final_exam = int(input("enter your final exam marks: "))


hw_percentage = (homework/25)*100
a_percentage = (assessment/50)*100
overall_percentage = (hw_percentage + a_percentage + final_exam)/3

if overall_percentage >= 90:
	grade = "a"
elif overall_percentage >=80:
	grade = "b"
elif overall_percentage >= 70:
	grade = "c"
elif overall_percentage >= 60:
	grade = "d"
elif overall_percentage >= 50:
	grade = "e"
else:
	grade = "f"


print(name +", your overall grade is:", grade)