
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

# Calculate all the options for 2 pairs
pair2_alloptions = {}
counter = 0
for i in range(1, 90):
    start = i + 1
    for j in range(start, 91):
        option = str(i).zfill(2) + "_" + str(j).zfill(2)
        pair2_alloptions[option] = 0
        counter += 1

print(f"Parser have found {counter} 2 pair options between 1-90 numbers.")

# Retrieve and calculate all the occurred options
pair2_array = {}

for i in range(1, 5):
    i2 = i + 1
    for j in range(i2, 6):
        this_nr1 = "Nr" + str(i)
        this_nr2 = "Nr" + str(j)
        
        # Check if both columns exist in the dataframe
        if this_nr1 in otos.columns and this_nr2 in otos.columns:
            this_pair = otos.groupby([this_nr1, this_nr2]).size()

            for iterit in this_pair.items():  # Changed from iteritems() to items()
                pair2_key = str(iterit[0][0]).zfill(2) + "_" + str(iterit[0][1]).zfill(2)
                pair2_num = int(iterit[1])

                if pair2_key in pair2_array:
                    pair2_array[pair2_key] += pair2_num
                else:
                    pair2_array[pair2_key] = pair2_num  # Completed the assignment

print(pair2_array)

# Show top 10 most frequent pairs
print("\nTop 10 most frequent pairs:")
sorted_pairs = sorted(pair2_array.items(), key=lambda x: x[1], reverse=True)
for i, (pair, count) in enumerate(sorted_pairs[:10], 1):
    print(f"{i:2d}. {pair} : {count} times")

