# pip install opencv-python
# pip install mediapipe
import csv
import json

csv_file = 'movie_metadata.csv'
json_file = 'data.json'

data = {}

with open(csv_file, encoding='utf-8') as file:
    csvReader = csv.DictReader(file)
    for rows in csvReader:
        # print(row)
        data_id = rows['movie_title']

        data[data_id] = rows
# for i in data.items():
#     print(i)
# with open(json_file, "a") as json_file_data:
#     json_file_data.write(json.dumps(data, indent=4)) 
