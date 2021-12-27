#This is a simple grade calculator. The user enters the Grade cutoffs then inputs their grade my percentage.
#The progam then evals the percentage and calculates the actual grade.

print("Welcome to Grade calculator 3000, Input the minimum grade to get the requested letter, do not input a range")
grad_cut_off_1 = int(input("What is the Cut off for a A grade?"))
grad_cut_off_2 = int(input("What is the cut off for a B grade?"))
grad_cut_off_3 = int(input("What is the cut off for a C grade?"))
grad_cut_off_4 = int(input("What is the cut off fot a D grade?"))
curve = int(input("Is their a curve, and how much percentage points?, in No curve put zero"))
grade = int(input("What is your percentage grade?"))
grade = grade + curve
if grade >= grad_cut_off_1:
    print("YOUR GRADE IS a A, LOOK AT YOU!")
elif grade >= grad_cut_off_2:
    print("YOUR GRADE IS A B, GOOD JOB!")
elif grade >= grad_cut_off_3:
    print("YOUR GRADE IS A C,C'S GET DEGREES!")
elif grade >= grad_cut_off_4:
    print("YOUR GRADE IS A D, WOW!")
else:
    print("YOUR GRADE IS A F, CONGRATS!")
print("Your grade percentage")
print(grade)
