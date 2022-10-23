import csv
import pandas as pd


dataset_1 = []
dataset_2 = []
with open("bright_stars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    dataset_1.append(row)

print(dataset_1)
with open("bright_stars2.csv", "r") as f:
   csvreader = csv.reader(f)
   for row in csvreader:
    dataset_2.append(row)

    
headers_1 = dataset_1[0]
stars_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
stars_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
stars_data = []



for index , data_row in enumerate(stars_data_1):
  stars_data.append(stars_data_1[index] + stars_data_2[index])


with open("total_stars.csv", "a") as f:
  csvwriter = csv.writer(f)
  csvwriter.writerow(headers)
  csvwriter.writerows(stars_data)

df=pd.read_csv('total_stars.csv')

df.tail(8)
