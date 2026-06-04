import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Training data for age categories
ages = np.array([10, 13, 16, 18, 21, 25, 30, 35, 36, 42, 50]).reshape(-1, 1)
labels = np.array([
    "Teen",
    "Teen",
    "Teen",
    "Young Adult",
    "Young Adult",
    "Young Adult",
    "Young Adult",
    "Young Adult",
    "Adult",
    "Adult",
    "Adult",
])

encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)
model = DecisionTreeClassifier(random_state=42)
model.fit(ages, encoded_labels)


def predict_category(age):
    try:
        encoded = model.predict([[int(age)]])[0]
        return encoder.inverse_transform([encoded])[0]
    except Exception:
        return "Young Adult"
