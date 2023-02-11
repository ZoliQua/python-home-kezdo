# Python Test Project File
# Written by Zoltan Dul (2021)
#
# synthetic classification dataset - fixed version without sklearn dependency
import numpy as np
from matplotlib import pyplot

def make_classification_custom(n_samples=1000, n_features=4, n_informative=2, 
                             n_classes=4, n_clusters_per_class=1, random_state=4):
    """
    Create a synthetic classification dataset without sklearn dependency
    """
    np.random.seed(random_state)
    
    # Generate base features
    X = np.random.randn(n_samples, n_features)
    
    # Create informative features by adding class-specific patterns
    y = np.random.randint(0, n_classes, n_samples)
    
    # Add class separation to informative features
    for class_idx in range(n_classes):
        class_mask = (y == class_idx)
        n_class_samples = np.sum(class_mask)
        
        if n_class_samples > 0:
            # Create cluster centers for this class
            for cluster_idx in range(n_clusters_per_class):
                cluster_center = np.random.randn(n_informative) * 3
                
                # Assign samples to this cluster
                start_idx = cluster_idx * (n_class_samples // n_clusters_per_class)
                end_idx = (cluster_idx + 1) * (n_class_samples // n_clusters_per_class)
                if cluster_idx == n_clusters_per_class - 1:
                    end_idx = n_class_samples
                
                class_indices = np.where(class_mask)[0]
                cluster_indices = class_indices[start_idx:end_idx]
                
                # Add class-specific pattern to informative features
                for i in range(n_informative):
                    X[cluster_indices, i] += cluster_center[i]
    
    return X, y

# Generate synthetic dataset
X, y = make_classification_custom(n_samples=1000, n_features=4, n_informative=2, 
                                n_classes=4, n_clusters_per_class=1, random_state=4)

# Create scatter plot for samples from each class
colors = ['red', 'blue', 'green', 'orange']
for class_value in range(4):
    # Get row indexes for samples with this class
    row_ix = np.where(y == class_value)
    # Create scatter of these samples
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1], 
                  c=colors[class_value], label=f'Class {class_value}', alpha=0.6)

# Add legend and labels
pyplot.legend()
pyplot.xlabel('Feature 1')
pyplot.ylabel('Feature 2')
pyplot.title('Synthetic Classification Dataset')

# Show the plot
pyplot.show()
print("Dataset shape:", X.shape)
print("Number of samples:", len(X))
print("Classes distribution:", np.bincount(y))