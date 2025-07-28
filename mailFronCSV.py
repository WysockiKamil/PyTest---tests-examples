import csv

from emailValidator import validate_email_format

def load_emails_from_csv():
    with open("emails.csv", newline="") as f:
        reader = csv.DictReader(f)
        return [(row["email"], row["expected"].lower() == "true") for row in reader]
    