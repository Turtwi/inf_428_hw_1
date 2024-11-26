import os
import csv
import unittest

import numpy as np

MAX_SCORE = 90

def generate_test_data(mean, variance, num_samples, seed):
    np.random.seed(seed)
    return np.random.randint(
        max(mean - variance, 0),
        min(mean + variance + 1, MAX_SCORE),
        num_samples
    )

os.makedirs("data", exist_ok=True)

test_cases = [
    # Test Case 1: Uniform Departments
    {
        "file_name": "data/test_case_1.csv",
        "departments": [
            {"name": "Engineering", "mean": 50, "variance": 10, "users": 100, "importance": 3},
            {"name": "Marketing", "mean": 50, "variance": 10, "users": 100, "importance": 3},
            {"name": "Finance", "mean": 50, "variance": 10, "users": 100, "importance": 3},
            {"name": "Science", "mean": 50, "variance": 10, "users": 100, "importance": 3},
        ]
    },
    # Test Case 2: Unequal Importance
    {
        "file_name": "data/test_case_2.csv",
        "departments": [
            {"name": "Engineering", "mean": 40, "variance": 5, "users": 80, "importance": 5},
            {"name": "Marketing", "mean": 30, "variance": 10, "users": 50, "importance": 2},
            {"name": "Finance", "mean": 60, "variance": 20, "users": 100, "importance": 4},
            {"name": "HR", "mean": 20, "variance": 5, "users": 30, "importance": 1},
        ]
    },
    # Test Case 3: Outliers in Data
    {
        "file_name": "data/test_case_3.csv",
        "departments": [
            {"name": "Engineering", "mean": 70, "variance": 20, "users": 100, "importance": 4},
            {"name": "Marketing", "mean": 85, "variance": 10, "users": 200, "importance": 1},
            {"name": "Finance", "mean": 50, "variance": 5, "users": 80, "importance": 3},
            {"name": "Science", "mean": 40, "variance": 15, "users": 60, "importance": 2},
        ]
    },
    # Test Case 4: Large Differences in Department Sizes
    {
        "file_name": "data/test_case_4.csv",
        "departments": [
            {"name": "Engineering", "mean": 60, "variance": 10, "users": 200, "importance": 4},
            {"name": "Marketing", "mean": 40, "variance": 15, "users": 50, "importance": 2},
            {"name": "Finance", "mean": 70, "variance": 5, "users": 300, "importance": 5},
            {"name": "HR", "mean": 30, "variance": 20, "users": 20, "importance": 1},
        ]
    },
]

for case in test_cases:
    with open(case["file_name"], mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Department", "Threat Score", "Importance"])
        for dept in case["departments"]:
            data = generate_test_data(dept["mean"], dept["variance"], dept["users"], seed=42)
            for score in data:
                writer.writerow([dept["name"], score, dept["importance"]])



