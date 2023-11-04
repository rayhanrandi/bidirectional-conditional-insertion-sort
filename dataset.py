import os
import random


# value range of elements in dataset
MIN_VALUE = 0
MAX_VALUE = 50000

# dataset input size/length
KECIL = 500
SEDANG = 5000
BESAR = 50000

# current path
BASE_DIR = os.getcwd()


def write_to_file(filename: str, content: str) -> None:
    """
    writes dataset to .txt file, overwrites if file is already present in path
    """
    f = open(os.path.join(BASE_DIR, 'analysis_datasets', filename), "w")
    f.write(content + '\n')
    f.close()

def generate_sorted(size: int) -> list[int]:
    return sorted(generate_randomized(size))

def generate_randomized(size: int) -> list[int]:
    return list(random.randint(MIN_VALUE, MAX_VALUE) for _ in range(size))

def generate_reversed(size: int) -> list[int]:
    return generate_sorted(size)[::-1]


def generate() -> dict:
    return {
        'kecil_sorted': generate_sorted(KECIL),
        'kecil_randomized': generate_randomized(KECIL),
        'kecil_reversed': generate_reversed(KECIL),
        'sedang_sorted': generate_sorted(SEDANG),
        'sedang_randomized': generate_randomized(SEDANG),
        'sedang_reversed': generate_reversed(SEDANG),
        'besar_sorted': generate_sorted(BESAR),
        'besar_randomized': generate_randomized(BESAR),
        'besar_reversed': generate_reversed(BESAR),
    }
