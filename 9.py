import csv

with open('expenses.csv') as file:
    reader = csv.DictReader(file)
    expenses = list(reader)

jami = 0
eng_katta = expenses[0]

for e in expenses:
    summa = int(e['summa'])
    jami += summa
    
    if summa > int(eng_katta['summa']):
        eng_katta = e

print("Jami summa:", jami)
print("Eng katta xarajat:", eng_katta['nom'], eng_katta['summa'])
print("Xarajatlar soni:", len(expenses))
