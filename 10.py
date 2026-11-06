import csv

with open('sportchilar.csv') as file:
    reader = csv.DictReader(file)
    sportchilar = list(reader)

eng_yuqori = sportchilar[0]

for s in sportchilar:
    ball = int(s['ball'])
    
    print(s['ism'], s['sport'], ball)
    
    if ball > int(eng_yuqori['ball']):
        eng_yuqori = s

print("\n80 balldan yuqori:")
for s in sportchilar:
    if int(s['ball']) > 80:
        print(s['ism'], s['ball'])

print("\nEng yuqori ball:", eng_yuqori['ism'], eng_yuqori['ball'])
