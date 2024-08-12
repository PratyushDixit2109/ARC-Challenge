import numpy as np
import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Color mapping, assuming that '5' is the gray color
color_mapping = {
    0: "black",
    1: "blue",
    2: "red",
    3: "green",
    4: "yellow",
    5: "gray",
}
color_to_num = {color: num for num, color in color_mapping.items()}

def load_data_from_json(json_path):
    # Load JSON data from a file
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def fill_columns_on_gray(grid, gray_value=5, color_sequence=("blue", "red", "green", "yellow")):
    H, W = grid.shape
    
    # Get the color numbers from the color sequence
    color_nums = [color_to_num[color] for color in color_sequence]
    colors_idx = 0
    
    # Create a copy of the grid to work on
    output_grid = grid.copy()
    
    # Traverse row by row
    for yy in range(H):
        for xx in range(W):
            if output_grid[yy, xx] == gray_value:
                # Fill the column from this point to the bottom with the current color
                for y_ in range(yy, H):
                    output_grid[y_, xx] = color_nums[colors_idx % len(color_sequence)]
                # Move to the next color in the sequence
                colors_idx += 1
    
    return output_grid


color_mapping = {
    0: "black",
    1: "blue",
    2: "red",
    3: "green",
    4: "yellow",
    5: "gray",
}
color_to_num = {color: num for num, color in color_mapping.items()}

# Create a custom color map for plotting
cmap = mcolors.ListedColormap([color_mapping[i] for i in range(6)])
norm = mcolors.Normalize(vmin=0, vmax=5)

def plot_grids(original_grid, transformed_grid):
    # Create subplots to plot both the original and transformed grids
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(original_grid, cmap=cmap, norm=norm)
    axs[0].set_title("Original Grid")
    axs[0].axis('off')  # Hide the axes for a cleaner plot

    axs[1].imshow(transformed_grid, cmap=cmap, norm=norm)
    axs[1].set_title("Transformed Grid")
    axs[1].axis('off')  # Hide the axes for a cleaner plot

    plt.show()  # Display the plots

# Load the data from JSON file
json_file_path = Path("TASK.json")  # Modify with your actual file path
data = load_data_from_json(json_file_path)

# Loop through each training example and apply the transformation
for example in data["train"]:
    input_grid = np.array(example["input"])
    
    # Apply the fill_columns_on_gray function
    output_grid = fill_columns_on_gray(input_grid)
    
    # Plot the original and transformed grids
    plot_grids(input_grid, output_grid)