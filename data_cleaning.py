import pandas as pd

df = pd.read_csv(
    "ApexPlanet_DataAnalytics_Dataset.xlsx",
    sep="\t"
)

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df = df.drop_duplicates()

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,25,40,60,100],
    labels=["Young","Adult","Middle Age","Senior"]
)

df["Order_Month"] = df["Order_Date"].dt.month_name()

df.to_excel("Cleaned_Sales_Dataset.xlsx", index=False)

print("Cleaning Complete!")