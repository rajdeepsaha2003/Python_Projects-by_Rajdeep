# User input for array creation
size = int(input("Enter the size of the array: "))

# Create an empty array
my_array = []

# Iterate over the range of the array size and prompt for each element
for i in range(size):
    element = int(input("Enter element at index {}: ".format(i)))
    my_array.append(element)

my_array.sort()

# Print the created array
print("The created array is:", my_array)

for i in range (size):
    temp=my_array[i]
    j=i+1
    for (j) in range (i+1,size):
        if(temp==my_array[j]):
            print(True,my_array[j])
            t1=True
            break
        
if(t1!=True):
    print(False)