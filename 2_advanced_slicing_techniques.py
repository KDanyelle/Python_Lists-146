#Task 1

temperatures = 72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95,  96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106

#Extract the temperatures for the second week (7 days) of the month .
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week:" , second_week_temperatures)

#Task 2

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperature_above_100 = [temp for temp in temperatures if temp> 100]
print("Temperatures aboove 100:" , temperature_above_100)

#Task 3 

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
reversed_temperatures = temperatures[:-1]
extracted_temperatures = reversed_temperatures[4:10]
print("Temperatures from the 5th to the 10th day of the reversed list:" , extracted_temperatures)

