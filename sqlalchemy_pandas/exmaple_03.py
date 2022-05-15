from pydoc import describe
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print("df.decribe(")
print(df.describe())

ages = df["Age"]
print(ages)

# Create a series
age_series = pd.Series([22, 35, 58], name="Age")
print(age_series)
