# Excercise 13 Where to hide money
print("Where to hide the money\n")

Table = [['😀', '😀', '😀', '😀', '😀'], ['😀', '😀', '😀', '😀', '😀'], ['😀', '😀', '😀', '😀', '😀']]

print("",Table[0],"\n\n",Table[1],"\n\n",Table[2])
numbers = input("\nEnter the Raw number and Column number:\n")
Raw_Number = int(numbers[0])-1
Column_number = int(numbers[1])-1
Table[Raw_Number][Column_number] = '💲'
print("",Table[0],"\n\n",Table[1],"\n\n",Table[2])