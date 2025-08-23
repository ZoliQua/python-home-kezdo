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

# Calculate all the options for 4 quadruplets
pair4_alloptions = {}
counter = 0
for i in range(1, 88):  # Changed from 89 to 88 to allow room for quadruplets
    for j in range(i + 1, 89):
        for k in range(j + 1, 90):
            for l in range(k + 1, 91):
                option = str(i).zfill(2) + "_" + str(j).zfill(2) + "_" + str(k).zfill(2) + "_" + str(l).zfill(2)
                pair4_alloptions[option] = 0
                counter += 1

print(f"Parser have found {counter} 4 quadruplet options between 1-90 numbers.")

# Retrieve and calculate all the occurred options
pair4_array = {}

for i in range(1, 3):  # Changed from 4 to 3 to allow for quadruplets
    for j in range(i + 1, 4):  # Changed from 5 to 4
        for k in range(j + 1, 5):  # Changed from 6 to 5
            for l in range(k + 1, 6):  # New loop for the fourth number
                this_nr1 = "Nr" + str(i)
                this_nr2 = "Nr" + str(j)
                this_nr3 = "Nr" + str(k)
                this_nr4 = "Nr" + str(l)
                
                # Check if all four columns exist in the dataframe
                if this_nr1 in otos.columns and this_nr2 in otos.columns and this_nr3 in otos.columns and this_nr4 in otos.columns:
                    this_quadruplet = otos.groupby([this_nr1, this_nr2, this_nr3, this_nr4]).size()

                    for iterit in this_quadruplet.items():
                        pair4_key = str(iterit[0][0]).zfill(2) + "_" + str(iterit[0][1]).zfill(2) + "_" + str(iterit[0][2]).zfill(2) + "_" + str(iterit[0][3]).zfill(2)
                        pair4_num = int(iterit[1])

                        if pair4_key in pair4_array:
                            pair4_array[pair4_key] += pair4_num
                        else:
                            pair4_array[pair4_key] = pair4_num

# print(pair4_array)

# Show the top 10 most frequent quadruplets
print("\nTop 10 most frequent quadruplets:")
sorted_quadruplets = sorted(pair4_array.items(), key=lambda x: x[1], reverse=True)
for i, (quadruplet, count) in enumerate(sorted_quadruplets[:10], 1):
    print(f"{i:2d}. {quadruplet} : {count} times")

# Show the bottom 20 least frequent quadruplets
print("\nBottom 20 least frequent quadruplets:")
for i, (quadruplet, count) in enumerate(sorted_quadruplets[-20:], 1):
    print(f"{i:2d}. {quadruplet} : {count} times")

# Check for quadruplets that never occurred (counter = 0)
zero_count_quadruplets = []
for option in pair4_alloptions:
    if option not in pair4_array:
        zero_count_quadruplets.append(option)

if zero_count_quadruplets:
    print(f"\nFound {len(zero_count_quadruplets)} quadruplets that never occurred:")
    # for quadruplet in zero_count_quadruplets:
    #    print(f"  {quadruplet} : 0 times")
else:
    print("\nAll possible quadruplets have occurred at least once.")