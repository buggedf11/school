import itertools
import time
from tqdm import tqdm
import threading

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

# Define the processing function for each combination
def process_combination(combo):
    # Process the combination
    # You can replace this line with your specific processing logic
    time.sleep(0.01)
    progress_bar.update(1)  # Update the progress bar

# Define the worker function for each thread
def worker():
    while True:
        try:
            combo = combinations_with_numbers.pop(0)  # Get the next combination
        except IndexError:
            break  # No more combinations to process
        process_combination(combo)

# Define the number of threads to use
num_threads = 4

# Create and start the threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Close the progress bar
progress_bar.close()

# Calculate the time it took to go through all combinations
elapsed_time = time.time() - start_time
print(f"Total time elapsed: {elapsed_time:.2f} seconds")
