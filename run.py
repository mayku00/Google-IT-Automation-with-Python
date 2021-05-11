#!/usr/bin/env python3
import os

import requests

description_path = "supplier-data/descriptions/"
url = "http://35.194.61.178/fruits/"

files = os.listdir(description_path)

for file in files:
    if file.endswith("txt"):
        with open(description_path + file) as description_file:
            # grab the file name, ex. 001, 002 to use for image file
            fruit_name = os.path.splitext(file)[0]
            fruit_json = {
                "name": description_file.readline().strip(),
                "weight": description_file.readline().replace(" lbs\n",""),
                "description": description_file.readline().strip(),
                "image_name": fruit_name + ".jpeg",
            }
            print(fruit_json)
            response = requests.post(url, json=fruit_json)
            response.raise_for_status()
            if response.status_code != 201:
                print(response.status_code)
                print(response.text)
