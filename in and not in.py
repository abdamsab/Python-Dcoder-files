my_list = []
#
# Write your code here.
temp_list =[]

for i in range(8):
    val = int(input("Enter number: "))
    my_list.append(val)
print(my_list)

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)
my_list = temp_list[:]

print("The list with unique elements only:")
print(my_list)
