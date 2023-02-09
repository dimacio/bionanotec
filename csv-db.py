import csv
from papers_backend import Database

db=Database("app.db")

with open("papers.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        db.insert(row["name"], row["author"], row["year"], row["doi"], row["grafical"], row["abstract"],row["cite"])

