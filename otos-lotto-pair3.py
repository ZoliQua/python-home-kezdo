# This program is part of a series of programs for the Hungarian public lucky game (Ötöslottó) to test Python
# This game is a national-wide lottery:
# 	-- There are 5 draws from 90 numbers (01-90)
# 	-- There is one draw in each week
# 	-- Game began in 1957 back in the communist era
#	-- We have the data from all the draws.
#
#
# Written by Zoltan Dul (2021)
#

from typing import Dict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import sys
import os

# Check if the file exists before trying to read it
file_path = "data/lotto/source/otos.csv"
if not os.path.exists(file_path):
    print(f"Error: The file {file_path} does not exist.")
    print("Please make sure the data file is in the correct location.")
    sys.exit(1)

# First read the header to see what columns are available
try:
    # Read just the header row to check available columns
    header = pd.read_csv(file_path, sep=";", nrows=0)
    available_columns = header.columns.tolist()
    
    # Define the columns we want
    desired_columns = ["Year", "Week", "Nr1", "Nr2", "Nr3", "Nr4", "Nr5"]
    
    # Filter to only use columns that actually exist in the file
    usable_columns = [col for col in desired_columns if col in available_columns]
    
    if len(usable_columns) < len(desired_columns):
        missing = set(desired_columns) - set(usable_columns)
        print(f"Warning: Some columns are missing in the CSV: {missing}")
        print(f"Available columns are: {available_columns}")

    print("Using columns:", usable_columns)
    # Now read the actual data with only the columns that exist
    otos = pd.read_csv(file_path, sep=";", usecols=usable_columns)
    
except Exception as e:
    print(f"Error reading CSV file: {e}")
    print("Available columns in the CSV file might not match what the program expects.")
    sys.exit(1)

# Calculate all the options for 3 triplets
pair3_alloptions = {}
counter = 0
for i in range(1, 89):  # Changed from 90 to 89 to allow room for triplets
    for j in range(i + 1, 90):
        for k in range(j + 1, 91):
            option = str(i).zfill(2) + "_" + str(j).zfill(2) + "_" + str(k).zfill(2)
            pair3_alloptions[option] = 0
            counter += 1

print(f"Parser have found {counter} 3 triplet options between 1-90 numbers.")

# Retrieve and calculate all the occurred options
pair3_array = {}

for i in range(1, 4):  # Changed from 5 to 4 to allow for triplets
    for j in range(i + 1, 5):  # Changed from 6 to 5
        for k in range(j + 1, 6):  # New loop for the third number
            this_nr1 = "Nr" + str(i)
            this_nr2 = "Nr" + str(j)
            this_nr3 = "Nr" + str(k)
            
            # Check if all three columns exist in the dataframe
            if this_nr1 in otos.columns and this_nr2 in otos.columns and this_nr3 in otos.columns:
                this_triplet = otos.groupby([this_nr1, this_nr2, this_nr3]).size()

                for iterit in this_triplet.items():
                    pair3_key = str(iterit[0][0]).zfill(2) + "_" + str(iterit[0][1]).zfill(2) + "_" + str(iterit[0][2]).zfill(2)
                    pair3_num = int(iterit[1])

                    if pair3_key in pair3_array:
                        pair3_array[pair3_key] += pair3_num
                    else:
                        pair3_array[pair3_key] = pair3_num

print(pair3_array)

# Show top 10 most frequent triplets
print("\nTop 10 most frequent triplets:")
sorted_triplets = sorted(pair3_array.items(), key=lambda x: x[1], reverse=True)
for i, (triplet, count) in enumerate(sorted_triplets[:10], 1):
    print(f"{i:2d}. {triplet} : {count} times")

# Show bottom 20 least frequent triplets
print("\nBottom 20 least frequent triplets:")
for i, (triplet, count) in enumerate(sorted_triplets[-20:], 1):
    print(f"{i:2d}. {triplet} : {count} times")