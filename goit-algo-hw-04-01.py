def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            except ValueError:
                print(f"Incorrect row format: {line.strip()}")

    average = total / count if count > 0 else 0
    return total, average

total, average = total_salary("D:/Python/GoIT/path.txt")
print(f"Total amount of salary: {total}, Average salary: {average}")
