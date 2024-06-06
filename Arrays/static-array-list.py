### assist 1
# create a list with a fixed size of 5, initialized with ones
numbers = [1] * 5
# printing all values of the list
print("Assist 1")
for number in numbers:
    print(number)

### assist 2
# create a list with a fixed size of 5, initialized with zeros
numbers = [0] * 5
# assign values to the array using a for loop
for i in range(len(numbers)):
    # assign multiples of 10
    numbers[i] = i * 10  
# printing all values of the list
print("Assist 2")
for number in numbers:
    print(number)
    
### assist 3
# create a list with a fixed size of 5, initialized with fives
numbers = [5] * 5
# assign values to the array using a for loop
for i in range(len(numbers)):
    # assign multiples of 50
    numbers[i] = i * 50
# printing all values of the list
print("Assist 3")
for number in numbers:
    print(number)

### assist 4
# create a list with specific values
numbers = [100, 200, 300, 400, 500]
# printing all values of the list
print("Assist 4")
for number in numbers:
    print(number)

### assist 5
# create a list with specific values
numbers = [1000, 2000, 3000, 4000, 5000]
# update specific elements using index
numbers[0] = 1
numbers[2] = 3
# printing all values of the list
print("Assist 5")
for number in numbers:
    print(number)