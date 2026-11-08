import pandas as pd

names = pd.Series(["ali", "John", "Sarah", "Bob", "David"])

data = {
    "Name": names,
    "Maths": [85, 70, 90, 65, 80],
    "Science": [90, 75, 85, None, 70], 
    "English": [80, 85, 75, 70, None]
}

df = pd.DataFrame(data)

print("Student Marks: ")
print(df)

df.to_csv("student_marks.csv")
print("\nData from CSV: ")
print(df)

print("\nData Information: ")
print(df.info())
df = df.fillna(0)

print("Cleaned data: ")
print(df)

df["Total"] = df["Maths"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3

print("\nFinal student results: " )
print(df) 