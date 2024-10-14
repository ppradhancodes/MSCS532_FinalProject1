import time
import random

class LinearSearch:
    def __init__(self, data):
        self.data = data
    
    def search(self, key):
        for item in self.data:
            if item == key:
                return True
        return False

class HashTable:
    def __init__(self, data):
        self.data = set(data)
    
    def search(self, key):
        return key in self.data

def generate_data(size):
    return [random.randint(1, 1000000) for _ in range(size)]

def benchmark(structure, search_keys):
    start_time = time.time()
    for key in search_keys:
        structure.search(key)
    end_time = time.time()
    return end_time - start_time

# Test parameters
data_size = 1000000
search_size = 10000

# Generate data and search keys
data = generate_data(data_size)
search_keys = generate_data(search_size)

# Create data structures
linear_search = LinearSearch(data)
hash_table = HashTable(data)

# Benchmark
linear_time = benchmark(linear_search, search_keys)
hash_time = benchmark(hash_table, search_keys)

print(f"Linear Search Time: {linear_time:.4f} seconds")
print(f"Hash Table Time: {hash_time:.4f} seconds")
print(f"Speedup: {linear_time / hash_time:.2f}x")