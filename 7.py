import csv

with open('products.csv') as file:
    reader = csv.DictReader(file)
    products = list(reader)

eng_qimmat = products[0]

for p in products:
    narx = int(p['narx'])
    miqdor = int(p['miqdor'])
    
    print(p['nom'], narx * miqdor)
    
    if narx > int(eng_qimmat['narx']):
        eng_qimmat = p

print("Eng qimmat:", eng_qimmat['nom'])
