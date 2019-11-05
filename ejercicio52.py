#Exercise 52: Grade Points to Letter Grade

correct = int(input('Enter the number of problems you got correct:'))

if correct > 0 :
    print ('Got it!')

total = int(input('Enter the total number of problems on the test:'))

if correct > 0 :
    print ('Got it!')
    
percent = correct / total * 100

if percent < 65 :
  letter = 'F'
  
if percent > 65 and percent < 70 :
  letter = 'D'

if percent > 69 and percent < 80 :
  letter = 'C'

if percent >= 80 and percent < 90 :
  letter = 'B'

if percent >= 90 :
  letter = 'A'

print ('Your percent correct is:', percent )

print ('Your letter grade is:', letter)
