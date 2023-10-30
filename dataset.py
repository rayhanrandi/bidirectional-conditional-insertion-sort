import random


MIN_VALUE = 0
MAX_VALUE = 50000

def generate_sorted(size: int) -> list[int]:
    return sorted(generate_randomized(size))

def generate_randomized(size: int) -> list[int]:
    return list(random.randint(MIN_VALUE, MAX_VALUE) for _ in range(size))

def generate_reversed(size: int) -> list[int]:
    return reversed(generate_sorted(size))

def generate() -> dict:
    return {
        'kecil_sorted': generate_sorted(500),
        'kecil_randomized': generate_randomized(500),
        'kecil_reversed': generate_reversed(500),
        'sedang_sorted': generate_sorted(5000),
        'sedang_randomized': generate_randomized(5000),
        'sedang_reversed': generate_reversed(5000),
        'besar_sorted': generate_sorted(50000),
        'besar_randomized': generate_randomized(50000),
        'besar_reversed': generate_reversed(50000),
    }