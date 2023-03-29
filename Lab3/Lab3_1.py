import glob
import os

files = glob.glob("zadanie1/*")

for file in files:
    try:
        os.rename(file, (file.split("zadanie1/")[1])[0] + "/" + file.split("zadanie1/")[1])
    except FileNotFoundError:
        os.makedirs((file.split("zadanie1/")[1])[0], exist_ok=False)
        os.rename(file, (file.split("zadanie1/")[1])[0] + "/" + file.split("zadanie1/")[1])
