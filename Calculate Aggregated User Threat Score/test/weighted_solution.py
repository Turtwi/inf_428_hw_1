import numpy as np

MAX_SCORE = 90

def calculate_department_score(users, importance):
    """
    Weighted score calculation for a department.
    """
    return np.mean(users) * importance


def calculate_aggregated_score(department_scores, importance_weights):
    """
    Aggregates department scores weighted by their respective importance scores.
    Ensures the result is in the range [0, 90].
    """
    total_score = sum(department_scores)
    total_importance = sum(importance_weights)

    if total_importance == 0:
        return 0

    aggregated_score = total_score / total_importance

    return min(max(aggregated_score, 0), MAX_SCORE)