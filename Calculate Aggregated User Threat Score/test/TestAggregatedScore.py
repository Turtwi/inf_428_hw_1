import unittest
import csv
import os
from weighted_solution import calculate_department_score, calculate_aggregated_score, MAX_SCORE


def load_csv_data(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
    file_path = os.path.join(base_path, "..", file_name)  # Navigate to the parent folder and data folder
    department_data = {}
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dept, score, importance = row[0], int(row[1]), int(row[2])
            if dept not in department_data:
                department_data[dept] = {"scores": [], "importance": importance}
            department_data[dept]["scores"].append(score)
    return department_data


class TestAggregatedScore(unittest.TestCase):
    def test_case_1(self):
        department_data = load_csv_data("data/test_case_1.csv")

        department_scores = []
        importance_weights = []

        for dept, data in department_data.items():
            score = calculate_department_score(data["scores"], data["importance"])
            department_scores.append(score)
            importance_weights.append(data["importance"])

        aggregated_score = calculate_aggregated_score(department_scores, importance_weights)
        print(f"Aggregated Score (Test Case 1): {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= MAX_SCORE)

    def test_case_2(self):
        department_data = load_csv_data("data/test_case_2.csv")

        department_scores = []
        importance_weights = []

        for dept, data in department_data.items():
            score = calculate_department_score(data["scores"], data["importance"])
            department_scores.append(score)
            importance_weights.append(data["importance"])

        aggregated_score = calculate_aggregated_score(department_scores, importance_weights)
        print(f"Aggregated Score (Test Case 2): {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= MAX_SCORE)

    def test_case_3(self):
        department_data = load_csv_data("data/test_case_3.csv")

        department_scores = []
        importance_weights = []

        for dept, data in department_data.items():
            score = calculate_department_score(data["scores"], data["importance"])
            department_scores.append(score)
            importance_weights.append(data["importance"])

        aggregated_score = calculate_aggregated_score(department_scores, importance_weights)
        print(f"Aggregated Score (Test Case 3): {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= MAX_SCORE)

    def test_case_4(self):
        department_data = load_csv_data("data/test_case_4.csv")

        department_scores = []
        importance_weights = []

        for dept, data in department_data.items():
            score = calculate_department_score(data["scores"], data["importance"])
            department_scores.append(score)
            importance_weights.append(data["importance"])

        aggregated_score = calculate_aggregated_score(department_scores, importance_weights)
        print(f"Aggregated Score (Test Case 4): {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= MAX_SCORE)


if __name__ == "__main__":
    unittest.main()
