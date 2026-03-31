# Spam Email Classifier

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "email": [
        "Win money now", "Limited time offer", "Claim your free prize",
        "Congratulations you won lottery", "Get cash instantly",
        "Free entry in contest", "Earn cash fast", "Exclusive deal just for you",
        "Hello how are you", "Let's meet tomorrow",
        "Project submission deadline", "Can we study together",
        "Lunch at 2 pm", "Call me when free",
        "Assignment is due today", "Meeting at 5 pm",
        "Urgent your account is blocked", "Verify your bank details now",
        "You have won a gift card", "Click link to claim reward"
    ],
    "label": [
        1,1,1,1,1,1,1,1,
        0,0,0,0,0,0,0,0,
        1,1,1,1
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Text Cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

df["email"] = df["email"].apply(clean_text)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X = vectorizer.fit_transform(df["email"])
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Test emails
test_emails = [
    "Win a free iPhone now",
    "Let's meet for project discussion",
    "Urgent: update your bank details",
    "Let's meet tomorrow"
]

print("\nPredictions:")
for email in test_emails:
    email_clean = clean_text(email)
    test_data = vectorizer.transform([email_clean])
    prediction = model.predict(test_data)

    if prediction[0] == 1:
        print(f"{email} --> Spam")
    else:
        print(f"{email} --> Not Spam")