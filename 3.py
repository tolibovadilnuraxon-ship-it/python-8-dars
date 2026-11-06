import json

with open('student.json', 'r') as file:
    data = json.load(file)
    
data['ball'] = 95

with open('student.json', 'w') as file:
    json.dump(data, file, indent=4)
    
print("O'quvchining balli muvaffaqiyatli o'zgartirildi! ")
