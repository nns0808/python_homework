import pandas as pd
import json

data = [
    {'Title': 'Real-World Spanish: The Conversation Learning System', 'Author': 'John Doe', 'Format-Year': 'Paperback 2020'},
    {'Title': 'Learning Spanish-beginner I', 'Author': 'Jane Smith', 'Format-Year': 'Ebook 2019'},
    {'Title': '100 Facts About Learning Spanish', 'Author': 'Mary Johnson', 'Format-Year': 'Hardcover 2021'},
    {'Title': '100 Facts About Learning Spanish', 'Author': 'Robert Brown', 'Format-Year': 'Paperback 2022'},
    {'Title': 'The Ultimate Learning Spanish Blueprint - 10 Essential Steps', 'Author': 'Alice White', 'Format-Year': 'Ebook 2018'}
]


df = pd.DataFrame(data)


csv_file_path = 'assignment9/get_books.csv'
df.to_csv(csv_file_path, index=False)

json_file_path = 'assignment9/get_books.json'
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"DataFrame written to {csv_file_path}")
print(f"Results written to {json_file_path}")
