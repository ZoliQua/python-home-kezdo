# Python Test Project File
# Written by Zoltan Dul (2021)
#
# synthetic classification dataset
from numpy import where

# Try importing with error handling to provide better user feedback
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
except ImportError as e:
    print(f"Import error: {e}")
    print("Please update your conda environment:")
    print("conda update numpy scipy pandas matplotlib seaborn")
    exit(1)

try:
    go_data = pd.read_csv("data/cluster_source_202202_mod_extract.csv", sep=",", usecols=["GO_ID", "SPECIES", "local_cc_10", "edges_10"])
except FileNotFoundError:
    print("Data file not found. Creating sample data for demonstration...")
    # Create sample data if the original file doesn't exist
    import numpy as np
    np.random.seed(42)
    species_list = ["SP", "SC", "AT", "HS", "DM", "DR", "CE"]
    go_ids = [f"GO:{i:07d}" for i in range(1000, 1050)]
    
    sample_data = []
    for go_id in go_ids:
        for species in species_list:
            if np.random.random() > 0.3:  # 70% chance of having data
                sample_data.append({
                    "GO_ID": go_id,
                    "SPECIES": species,
                    "local_cc_10": np.random.randint(1, 20),
                    "edges_10": np.random.randint(1, 100)
                })
    
    go_data = pd.DataFrame(sample_data)


sns.set_theme(color_codes=True)

# Use built-in datasets as fallback
try:
    iris = sns.load_dataset("iris")
    flights = sns.load_dataset("flights")
    species = iris.pop("species")
    flights = flights.pivot("month", "year", "passengers")
except Exception as e:
    print(f"Could not load seaborn datasets: {e}")
    print("Using sample data instead...")

# Filter data
go_data2 = go_data[(go_data.SPECIES == "SP") | (go_data.SPECIES == "SC") | 
                   (go_data.SPECIES == "AT") | (go_data.SPECIES == "HS") | 
                   (go_data.SPECIES == "DM") | (go_data.SPECIES == "DR") | 
                   (go_data.SPECIES == "CE")]
print(go_data2)

# Create pivot table
try:
    go_data_pivot = go_data2.pivot("GO_ID", "SPECIES", "edges_10")
    
    # Handle missing values
    go_data_pivot = go_data_pivot.fillna(0)
    
    # Create clustermap with error handling
    g = sns.clustermap(go_data_pivot, figsize=(10, 10), annot=True, 
                       cmap="YlGnBu", mask=(go_data_pivot==0), 
                       standard_scale=1, method='average')
    
    print(dir(g))
    print(g.data2d.T)
    
    # Save to Excel with error handling
    try:
        g.data2d.T.to_excel("edges_10_annotation_normal_scale_20220901b.xlsx")
        print("Data exported to Excel successfully")
    except Exception as e:
        print(f"Could not export to Excel: {e}")
        # Save as CSV instead
        g.data2d.T.to_csv("edges_10_annotation_normal_scale_20220901b.csv")
        print("Data exported to CSV instead")
    
    plt.show()
    
except Exception as e:
    print(f"Error creating clustermap: {e}")
    print("This might be due to package compatibility issues.")
    print("Please run: conda update --all")
