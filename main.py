#ищем средний возраст пассажиров "Титаника"
with open("data.csv") as file:
    s = 0
    n = 0
    for line in file:
        data = line.split(',')
        if data[6] == 'SibSp' or data[6] == '':
            continue
        s += float(data[6])
        n += 1
print(s/n)