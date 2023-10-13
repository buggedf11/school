import itertools
import time
from tqdm import tqdm

# Define the set of letters and numbers
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

# Generate all combinations of 3 letters followed by 2 numbers
combinations = list(itertools.product(letters, repeat=3))  # All possible 3-letter combinations
combinations = [''.join(combination) for combination in combinations]  # Convert to strings

# Add 2 numbers to each combination
combinations_with_numbers = []
for combination in combinations:
    for num1 in numbers:
        for num2 in numbers:
            combinations_with_numbers.append(combination + num1 + num2)

# Calculate the total number of combinations
total_combinations = len(combinations_with_numbers)

# Create a progress bar
progress_bar = tqdm(total=total_combinations, unit="combination")

# Print all combinations and measure time
start_time = time.time()
for combo in combinations_with_numbers:
    # Process the combination
    # You can replace this line with your specific processing logic
    time.sleep(0.01)
    progress_bar.update(1)  # Update the progress bar
progress_bar.close()
end_time = time.time()

# Calculate the time it took to go through all combinations
elapsed_time = end_time - start_time
print(f"Total time elapsed: {elapsed_time:.2f} seconds")
