import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import make_classification

# -----------------------
# داده مصنوعی
# -----------------------
def generate_data():
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=6,
        n_classes=2,
        random_state=42
    )
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(X.shape[1])])
    df["label"] = y
    df.to_csv("train.csv", index=False)
    print("✅ train.csv ساخته شد.")

# -----------------------
# اجرای مدل پایه
# -----------------------
def run_baseline():
    data = pd.read_csv("train.csv")
    X, y = data.drop("label", axis=1), data["label"]

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    preds = model.predict(X)

    acc = accuracy_score(y, preds)
    print(f"📊 Baseline Accuracy: {acc:.4f}")
    return acc

# -----------------------
# اجرای مدل بهبودیافته
# -----------------------
def run_improved():
    data = pd.read_csv("train.csv")
    X, y = data.drop("label", axis=1), data["label"]

    # بهبود ساده: وزن‌دهی متفاوت به کلاس‌ها
    model = LogisticRegression(max_iter=200, class_weight="balanced")
    model.fit(X, y)
    preds = model.predict(X)

    acc = accuracy_score(y, preds)
    print(f"🚀 Improved Accuracy: {acc:.4f}")
    return acc

# -----------------------
# main
# -----------------------
if name == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["baseline", "improved"], required=True)
    parser.add_argument("--regen-data", action="store_true")
    args = parser.parse_args()

    if args.regen_data:
        generate_data()

    if args.mode == "baseline":
        run_baseline()
    elif args.mode == "improved":
        run_improved()
