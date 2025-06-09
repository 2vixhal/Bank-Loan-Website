# risk_classifier.py

def classify_risk(probability: float) -> str:
    """
    Classify credit risk based on the predicted probability.

    Args:
        probability (float): The predicted probability of loan default (0 to 1).

    Returns:
        str: Risk category ('Low', 'Medium', 'High').
    """
    if probability < 0.33:
        return "Low"
    elif 0.33 <= probability < 0.66:
        return "Medium"
    else:
        return "High"


# Example usage
if __name__ == "__main__":
    # Test the function with sample probabilities
    test_probs = [0.1, 0.5, 0.8]
    for prob in test_probs:
        print(f"Probability: {prob}, Risk: {classify_risk(prob)}")