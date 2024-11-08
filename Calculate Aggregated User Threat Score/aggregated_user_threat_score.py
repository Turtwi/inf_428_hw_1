import unittest
import numpy as np

MAX_SCORE = 90  # Max score for each department's score

def generate_random_data(mean: int, variance: int, num_samples: int) -> np.ndarray:
    """
    Generates random integer data within a range determined by mean and variance.
    Ensures values are within [0, MAX_SCORE] range.
    """
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_score(users: list[int], importance: int) -> float:
    """
    Calculates the department score based on user data and department importance.
    """
    return np.mean(users) * importance

def calculate_aggregated_score(department_scores: list[float], importance_weights: list[int]) -> float:
    """
    Aggregates department scores weighted by their respective importance scores.
    Returns 0 if total importance is zero.
    """
    total_score = sum(department_scores)
    total_importance = sum(importance_weights)
    if total_importance == 0:
        return 0
    return total_score / total_importance


class TestCybersecurityScoreCalculations(unittest.TestCase):

    def test_functional_case(self):
        importance_scores = {
            "Engineering": 4,
            "Marketing": 3,
            "Finance": 5,
            "HR": 1,
            "Science": 2
        }

        departments_data = {
            "Engineering": generate_random_data(90, 2, 200),
            "Marketing": generate_random_data(90, 15, 70),
            "Finance": generate_random_data(90, 10, 80),
            "HR": generate_random_data(90, 20, 40),
            "Science": generate_random_data(90, 1, 100)
        }

        department_scores = {
            department: calculate_department_score(data, importance_scores[department])
            for department, data in departments_data.items()
        }

        scores = list(department_scores.values())
        importance = list(importance_scores.values())

        aggregated_score = calculate_aggregated_score(scores, importance)
        self.assertTrue(0 <= aggregated_score <= MAX_SCORE)

    def test_empty_input(self):
        department_scores = []
        importance_weights = []
        result = calculate_aggregated_score(department_scores, importance_weights)
        self.assertEqual(result, 0)

    def test_single_department(self):
        department_scores = [80]
        importance_weights = [5]
        result = calculate_department_score(department_scores, importance_weights[0])
        expected_result = 400
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()





