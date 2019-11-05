#Exercise 51: Letter Grade to Grade Points

grade = input('What is the letter grade?')
grade = grade.upper()
gpa = 0

while True:
    if grade == 'A+':
        gpa = 4.0
        break
    elif grade == 'A':
        gpa = 4.0
        break
    elif grade == 'A-':
        gpa = 3.7
        break
    elif grade == 'B+':
        gpa = 3.3
        break
    elif grade == 'B':
        gpa = 3.0
        break
    elif grade == 'B-':
        gpa = 2.7
        break
    elif grade == 'C+':
        gpa = 2.3
        break
    elif grade == 'C':
        gpa = 2.0
        break
    elif grade == 'C-':
        gpa = 1.7
        break
    elif grade == 'D+':
        gpa = 1.3
        break
    elif grade == 'D':
        gpa = 1.0
        break
    elif grade == 'F':
        gpa = 0
        break
    else:
        print('Invalid input.')
        grade = input('What is the letter grade?')
        grade = grade.upper()
        gpa = 0 
        
print()
print('Grade points: ', str(gpa))
