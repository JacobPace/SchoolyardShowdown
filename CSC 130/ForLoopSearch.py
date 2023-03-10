# search for the largest value
from random import randint
numbers = []
while len(numbers) < 10:
    num = randint(1, 50)
    numbers.append(num)
print(numbers)

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest =number
print(largest)
# or max(largest)

# sequential search
#smallest = numbers[0]
#for index in range(len(numbers)):
#    if (numbers[index] < smallest):
#        smallest = numbers(index)
#print(smallest)
#or
# min(smallest)

#selection sort
n = len(numbers)
for i in range(0, n - 1):
    min = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min]:
            min = j
    temp = numbers[i]
    numbers[i] = numbers[min]
    numbers[min] = temp
print(numbers)
# or sorted(numbers)