# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

students = 0
for height in student_heights:
    students += height
#print(students)
i = 0
for punks in student_heights:
    i += 1

average = round(students / i)
print(average)
