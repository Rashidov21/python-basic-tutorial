import json
import pandas as pd

df = pd.read_excel("phones.xlsx", skiprows=2)
data = []
for i in df.values:
    temp = {
        "id":i[0],
        "phone":"+998"+str(i[4]).replace(" ", "").replace("-", "").replace(".","")
    }
    data.append(temp)

# with open("phone_data.json","w+", encoding="utf-8") as file:
#     json.dump(data ,file)
with open("number.txt", "w+", encoding='utf-8') as f:
    for i in data:
        f.write(f"{i.get('phone')}, ")