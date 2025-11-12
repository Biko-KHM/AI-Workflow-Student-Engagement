"""
Model evaluation utilities.
"""

from sklearn.metrics import confusion_matrix, precision_score, recall_score

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds)
    precision = precision_score(y_test, preds)
    recall = recall_score(y_test, preds)
    print("Confusion Matrix:\n", cm)
    print(f"Precision: {precision:.2f}, Recall: {recall:.2f}")
