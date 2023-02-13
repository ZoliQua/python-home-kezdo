# Python Test Project File
# Written by Zoltan Dul (2021)
#
# synthetic classification dataset

# Handle the numpy/scipy compatibility issue gracefully
import sys
import warnings


def safe_import_scientific_packages():
    """Safely import scientific packages with fallback options"""
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np

        # Try importing seaborn with error handling for binary incompatibility
        try:
            import seaborn as sns
            return pd, plt, np, sns, True
        except (ValueError, ImportError) as e:
            if "numpy.dtype size changed" in str(e) or "binary incompatibility" in str(e):
                print("WARNING: Seaborn/SciPy binary compatibility issue detected.")
                print("Falling back to matplotlib-only visualization...")
                return pd, plt, np, None, False
            else:
                raise e

    except ImportError as e:
        print(f"Import error: {e}")
        print("Please update your conda environment:")
        print("conda update numpy scipy pandas matplotlib seaborn")
        sys.exit(1)


# Import packages with fallback
pd, plt, np, sns, has_seaborn = safe_import_scientific_packages()

# Set up plotting style
if has_seaborn:
    sns.set_theme(color_codes=True)
else:
    plt.style.use('default')

# Data loading with fallback
try:
    go_data = pd.read_csv("data/cluster_source_202202_mod_extract.csv", sep=",",
                          usecols=["GO_ID", "SPECIES", "local_cc_10", "edges_10"])
except FileNotFoundError:
    print("Data file not found. Creating sample data for demonstration...")
    # Create sample data
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

# Filter data
go_data2 = go_data[(go_data.SPECIES == "SP") | (go_data.SPECIES == "SC") |
                   (go_data.SPECIES == "AT") | (go_data.SPECIES == "HS") |
                   (go_data.SPECIES == "DM") | (go_data.SPECIES == "DR") |
                   (go_data.SPECIES == "CE")]
print("Filtered data shape:", go_data2.shape)
print(go_data2.head())

# Create pivot table
try:
    go_data_pivot = go_data2.pivot("GO_ID", "SPECIES", "edges_10")
    go_data_pivot = go_data_pivot.fillna(0)

    if has_seaborn:
        # Try seaborn clustermap
        try:
            print("Creating seaborn clustermap...")
            g = sns.clustermap(go_data_pivot, figsize=(10, 10), annot=True,
                               cmap="YlGnBu", mask=(go_data_pivot == 0),
                               standard_scale=1, method='average')

            print("Clustermap created successfully!")
            print("Available attributes:", [attr for attr in dir(g) if not attr.startswith('_')])

            # Export data
            try:
                g.data2d.T.to_excel("edges_10_annotation_normal_scale_20220901b.xlsx")
                print("Data exported to Excel successfully")
            except Exception as e:
                print(f"Could not export to Excel: {e}")
                g.data2d.T.to_csv("edges_10_annotation_normal_scale_20220901b.csv")
                print("Data exported to CSV instead")

        except Exception as e:
            print(f"Seaborn clustermap failed: {e}")
            has_seaborn = False  # Fall back to matplotlib

    # Fallback to matplotlib heatmap if seaborn fails
    if not has_seaborn:
        print("Using matplotlib fallback visualization...")


        # Simple hierarchical clustering using built-in Python functions
        def simple_clustering_order(data_matrix):
            """Simple clustering based on correlation"""
            try:
                # Calculate correlation matrix
                corr_matrix = np.corrcoef(data_matrix)

                # Simple ordering based on correlation strength
                # This is a simplified version - not as sophisticated as scipy's clustering
                n = len(corr_matrix)
                order = list(range(n))

                # Sort by average correlation with others (simple heuristic)
                avg_corr = [np.mean(np.abs(corr_matrix[i])) for i in range(n)]
                order.sort(key=lambda x: avg_corr[x], reverse=True)

                return order
            except:
                # If correlation fails, return original order
                return list(range(len(data_matrix)))


        # Create matplotlib heatmap
        fig, ax = plt.subplots(figsize=(10, 8))

        # Simple ordering (fallback clustering)
        data_array = go_data_pivot.values
        row_order = simple_clustering_order(data_array)
        col_order = simple_clustering_order(data_array.T)

        # Reorder data
        ordered_data = data_array[np.ix_(row_order, col_order)]
        ordered_pivot = pd.DataFrame(
            ordered_data,
            index=go_data_pivot.index[row_order],
            columns=go_data_pivot.columns[col_order]
        )

        # Create heatmap
        im = ax.imshow(ordered_data, cmap='YlGnBu', aspect='auto')

        # Set labels
        ax.set_xticks(range(len(go_data_pivot.columns)))
        ax.set_xticklabels(ordered_pivot.columns, rotation=45, ha='right')
        ax.set_yticks(range(len(go_data_pivot.index)))
        ax.set_yticklabels(ordered_pivot.index)

        # Add colorbar
        plt.colorbar(im, ax=ax, label='edges_10')

        # Add title
        plt.title('Gene Ontology Data Heatmap (matplotlib fallback)')
        plt.tight_layout()

        # Save data
        try:
            ordered_pivot.to_excel("edges_10_annotation_normal_scale_20220901b.xlsx")
            print("Data exported to Excel successfully")
        except Exception as e:
            print(f"Could not export to Excel: {e}")
            ordered_pivot.to_csv("edges_10_annotation_normal_scale_20220901b.csv")
            print("Data exported to CSV instead")

    plt.show()

except Exception as e:
    print(f"Error creating visualization: {e}")
    print("This might be due to data format issues.")

    # Last resort: simple scatter plot
    try:
        plt.figure(figsize=(10, 6))
        for species in go_data2['SPECIES'].unique():
            species_data = go_data2[go_data2['SPECIES'] == species]
            plt.scatter(species_data['local_cc_10'], species_data['edges_10'],
                        label=species, alpha=0.7)

        plt.xlabel('local_cc_10')
        plt.ylabel('edges_10')
        plt.title('GO Data Scatter Plot by Species')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

        print("Created fallback scatter plot successfully")
    except Exception as final_e:
        print(f"Even fallback visualization failed: {final_e}")

print("Script completed.")