import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

json_matn = json.dumps(talaba)
print(json_matn)

qayta_dict = json.loads(json_matn)
print(qayta_dict["ism"])
