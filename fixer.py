import csv

# Open your CSV file in read mode
with open('csv_files/PostHistory.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Prepare a list to hold the cleaned data
cleaned_data = []

# Iterate over the data and quote any "Text" fields that contain newlines
for row in data:
    if row.count('"') % 2 == 0:  # Check if the number of quotes in the row is even
        cleaned_data.append(row)
    """ else:
        print(row) """

# Open your CSV file in write mode
with open('csv_files/Cleaned_PostHistory.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';', escapechar='"', quotechar='"')
    writer.writerows(cleaned_data)