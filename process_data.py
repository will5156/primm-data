"""
PRIMM: Python Data Processing
In this PRIMM Activity, you'll learn how to process a 
CSV file and complete some basic extraction techniques.

name - date
"""

import csv
from typing import Union

record = dict[str, Union[str, int, float]]

def get_records(data_filename: str) -> list[dict[str, Union[str, int]]]:
  """
  Gets records from a csv data file.
  Parameters:
    data_filename(str): The location and name of the csv file that contains the data
  Returns:
    list[dict[str, Union[int, str]]]: a list of records where each 
        record is a dictionary where the keys are strings 
        and the values can be int or str
  """
  records: list[dict[str,Union[str, int]]] = []
  with open(data_filename, "r", encoding='utf-8-sig') as data_file:
    reader: csv.DictReader = csv.DictReader(data_file)
    for record in reader:      
      records.append(record)

  return records

def convert_fields(records: list[record]) -> None:
  for record in records:
    record["REPORTYEAR"] = int(record["REPORTYEAR"])
    record["PropValue"] = float(record["PropValue"])

def sumarize_by_month(records: list[record]) -> dict[str, int]:
  summary: dict[str, int] = {}

  for r in records:
    month: str = r["REPORTDATE"][5:7] #grab month
    if month in summary:
      summary[month] += 1
    else:
      summary[month] = 1
  
  return summary
def sumarize_by_year(records: list[record]) -> dict[str, int]:
  summary: dict[str, int] = {}

  for r in records:
    month: str = r["REPORTYEAR"][5:7] #grab month
    if month in summary:
      summary[month] += 1
    else:
      summary[month] = 1
  
  return summary


def main() -> None:
  data_filename: str = "resources/stolen_bikes.csv"
  records: list[dict[str, Union[str, int]]] = get_records(data_filename)
  convert_fields(records)

  summary: dict[str, int] = sumarize_by_month(records)
  print(f"{len(records)} records read in.")
  for month in summary.keys():
    print(f"{month}: {summary[month]}")


if __name__ == "__main__":
  main()