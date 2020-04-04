import csv

call = 0
sms = 0

# Чтение из файла
FILENAME = "data.csv"
with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)


# Подсчет общей длительности звонков и общего количества СМС 
    for row in reader:
        if row[1] == '915642913':
            call += float(row[3])
            sms += float(row[4])
        if row[2] == '915642913':
            call += float(row[3])
            
# Тарификация
call_cost = call*1;

if sms > 10: sms_cost = 5*0 + 5*1 + (sms-10)*2 
elif sms in range(5,10): sms_cost = 5*0 + (sms-5)*1   
else: sms_cost = 0

cost = call_cost + sms_cost

print('Итоговая стоимость: {:.2f}'.format(cost))
