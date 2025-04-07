# Algorithm - steps for find the solution of a problem
# Finding Percentages with input statement (Algorithm) 
# 1. Create four input statements 

eng = int(input('Enter English Marks:'))
print('English Marks:',eng)
hin = int(input('Enter Hindi Marks:'))
print('Hindi Marks:',hin)
maths = int(input('Enter maths marks:'))
print('Maths Marks:',maths)
sci = int(input('Enter science marks:'))
print('Science Marks:',sci)

# 2. Then find the total max marks (max marks of each subject is 80)

#Total Max = Marks of each subject(80) x total subjects(4) = 320
total_max = 80*4    
print("total max:",total_max)

# 3. Find the total gained marks
total_gained =  eng+hin+maths+sci
# 4. Multiply total gained marks by 100

mul_100 = total_gained*100

# 5. Divide it by total max marks  

percentage = mul_100/total_max

# 6. Template fstring
#Eng-72, 65,60,66
print(f"""
English Marks: {eng}
Hindi Marks: {hin}
Maths Marks: {maths}
Science Marks: {sci}
Total Marks: {total_gained}
Total Max Marks: {total_max}
Percentage: {percentage} 
""")
