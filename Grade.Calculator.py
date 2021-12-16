#This is a simple grade calculator. The user enters the Grade cutoffs then inputs their grade my percentage.
#The progam then evals the percentage and calculates the actual grade.

grad_cut_off_1 = input("What is the Cut off for a A grade?")
grad_cut_off_2 = input("What is the cut off for a B grade?")
grad_cut_off_3 = input("What is the cut off for a C grade?")
grad_cut_off_4 = input("What is the cut off fot a D grade?")
curve = input("Is their a curve, and how much percentage points?, in No curve put zero")
grade = input("What is your percentage grade?")
grade = grade + curve
if grade >= grad_cut_off_1:
    print("YOUR GRADE IS a A, LOOK AT YOU!")
elif grade >= grad_cut_off_2:
    print("YOUR GRADE IS A B, NICE JOB!")
elif grade >= grad_cut_off_3:
    print("YOUR GRADE IS A C, C'S GET DEGREES!")
elif grade >= grad_cut_off_4:
    print("YOUR GRADE IS A D, WOW!")
else:
    print("YOUR GRADE IS A F!,Congrats")
