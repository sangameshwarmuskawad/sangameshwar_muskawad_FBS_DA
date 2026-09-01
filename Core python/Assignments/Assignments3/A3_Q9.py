# take input
marks = []
for i in range(5):
    mark = int(input('enter mark of subject {i + 1}:'))
    marks.append(mark)

# perform operation
total = sum(marks)
percentage = total / 5

# check condition
if(percentage >= 80):
    grade = "first class"
elif(percentage >= 60):
    grade = "second class"
elif(percentage >= 35):
    grade = "pass class" 
else:
    grade = "fail"

# display result
print('total mark:',total)
print('percentage:',percentage)
print('grade:',grade)
