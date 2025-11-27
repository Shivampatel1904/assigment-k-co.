import pandas as pd

aws = pd.read_csv("./aws_line_items_12mo.csv")
gcp = pd.read_csv ("./gcp_billing_12mo.csv")

aws.head()
gcp.head()

print("AWS rows:", len(aws))
print("GCP rows:", len(gcp)) #for rows

print("AWS nulls:\n", aws.isnull().sum())
print("GCP nulls:\n", gcp.isnull().sum()) #for null values

print("AWS duplicates:", aws.duplicated().sum())
print("GCP duplicates:", gcp.duplicated().sum())# for duplicates

print("AWS date range:", aws['date'].min(), aws['date'].max())
print("GCP date range:", gcp['date'].min(), gcp['date'].max()) # date range

print("AWS env values:", aws['env'].unique())
print("GCP env values:", gcp['env'].unique())

print("AWS top services:", aws['service'].value_counts().head())
print("GCP top services:", gcp['service'].value_counts().head())


