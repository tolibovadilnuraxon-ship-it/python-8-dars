import json

with open('product.json', 'r') as file:
    data = json.load(file)
    
sum = data['narx']*data['miqdor']
print(f"Umumiy qiymat: {sum}")
 
