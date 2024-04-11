#Task 1 : Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print("Sorted grades in descending order", sorted_grades)

#Task 2 : Calulate the average grade and display

#List of grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average_grade = sum(grades) / len(grades)
print("The average grade is:", average_grade)

#Task 3: Raplace any grade below 80 with the value Failed

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades = ["Failed" if grade < 80 else grade for grade in grades ]
print("Updated grades:", grades)




