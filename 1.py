import json

with open('user.json', 'r') as file:
    data = json.load(file)
    
print(f"Ism: {data['ism']}")
print(f"Yosh: {data['yosh']}")
