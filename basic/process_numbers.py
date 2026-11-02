string_to_process = "  18,27,35,20  "
cleaned = string_to_process.strip()
parts = cleaned.split(",")

num1 = int(parts[0])
num2 = int(parts[1])
num3 = int(parts[2])
num4 = int(parts[3])

total = num1 + num2 + num3 + num4
average = total / len(parts)

print("Total:", total)
print("Average:", average)

# Expected Output:
# "Total: 100"
# "Average: 25.0"