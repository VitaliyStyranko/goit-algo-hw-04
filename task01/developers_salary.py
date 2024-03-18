
def total_salary(path):
    total_salary = 0
    developers = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                developer, salary = line.split(',')
                total_salary += int(salary)
                developers += 1
            average_salary = total_salary // developers

    except FileNotFoundError as e:
        print(f"File '{path}' not found: {e}")
        return None, None
    except ValueError as e:
        print(f"An error occurred while reading the file {path}. Error: {e}")
        return None, None

    return total_salary, average_salary


path = 'salary.txt'
total, average = total_salary(path)
print(f"Total salary: {total}, Average salary: {average}")
