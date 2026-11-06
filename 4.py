import json

yangi_narx = int(input("Yangi narxni kiriting: "))
with open('phone.json', 'r') as file:
    data = json.load(file)
    
print(f"Model: {data['model']}")


data['narx'] = yangi_narx


with open('phone.json', 'w') as file:
    json.dump(data, file, indent=4)
    
print("Narx muvaffaqiyatli o'zgartirildi! ")
