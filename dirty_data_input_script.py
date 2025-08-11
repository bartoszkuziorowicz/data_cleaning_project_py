import pandas as pd

# Step 1: Load data
while True:
    filename = input("Enter the name of the file you want to clean: ")

    try:
        df = pd.read_csv(filename)
        print("Valid file!")
        break
    except FileNotFoundError:
        print("Invalid file!")

print("=== FIRST LOOK AT DATA ===")
print(df.head(), "\n")

# Step 2: Check missing values
print("=== MISSING VALUES BEFORE CLEANING ===")
print(df.isnull().sum(), "\n")

print("=== STATISTICAL SUMMARY BEFORE CLEANING ===")
print(df.describe(), "\n")

# Step 3: Remove completely empty rows
rows_before = len(df)
df = df.dropna(how="all")
rows_after = len(df)
 
result = (rows_before - rows_after)
if result == 1:
  print("Deleted" , result, "completely empty row.\n")
else:
  print("Deleted" , result, "completely empty rows.\n")


# Step 4: Fill missing values in text columns
df["Region"] = df["Region"].fillna("Not specified")
print("Filled missing values in 'Region' column.\n")

df["Category"] = df["Category"].fillna("Other")
print("Filled missing values in 'Category' column.\n")

# Step 5: Fill missing values in Age with the average
avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)
print("Filled missing values in 'Age' column with the average.\n")

# Step 6: Add a new column 'Total'
df["Total"] = df["Quantity"] * df["UnitPrice"]
print("Added new column 'Total' = Quantity * UnitPrice.\n")

# Step 7: Check after cleaning
print("=== MISSING VALUES AFTER CLEANING ===")
print(df.isnull().sum(), "\n")

print("=== STATISTICAL SUMMARY AFTER CLEANING ===")
print(df.describe(), "\n")

# Step 8: Sort by Total and display top 5
df = df.sort_values(by="Total", ascending=False)
print(df.head(), "\n")

# Step 9: Overall income
print("Total revenue for all customers:", df["Total"].sum(), "\n")

# Step 10: Save cleaned data
output_name = "clean_" + filename
df.to_csv(output_name, index=False)
print("The cleaned file has been saved!")
