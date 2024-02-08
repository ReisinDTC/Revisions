# Output integers from 20 to 25 (inclusive)
start_number = 20
end_number = 25

for i in range(start_number, end_number + 1):
    print(i)

# Calculate and print the sum
numbers = list(range(start_number, end_number + 1))
total_sum = sum(numbers)

print("Sum:", total_sum)
