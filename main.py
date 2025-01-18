#ищем средний возраст пассажиров "Титаника"
import csv

def calculate_average(filename: str) -> float:
    total = 0.0
    count = 0
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            if row[6].strip():
                try:
                    value = float(row[6])
                    total += value
                    count += 1
                except ValueError:
                    continue
    return total / count if count != 0 else 0

if __name__ == "__main__":
    average_value = calculate_average("data.csv")
    print("Среднее значение:", average_value)