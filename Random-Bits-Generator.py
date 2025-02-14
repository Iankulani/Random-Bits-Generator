# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 05:49:25 2025

@author: IAN CARTER KULANI

"""

import random

# Function to generate random bits
def generate_random_bits(length):
    bits = ''.join(random.choice('01') for _ in range(length))
    return bits

# Main function
def main():
    print("==================== Random Bits Generator Tool ====================")
    try:
        length = int(input("Enter the number of bits you want to generate:"))
        if length <= 0:
            print("Please enter a positive integer for the bit length.")
            return
        random_bits = generate_random_bits(length)
        print(f"Generated {length} random bits: {random_bits}")
    except ValueError:
        print("Invalid input! Please enter a valid integer for the bit length.")

if __name__ == "__main__":
    main()
