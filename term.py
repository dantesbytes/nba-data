import pandas as pd
import os
import unidecode
from dotenv import load_dotenv


load_dotenv()

term = os.getenv('term')

term_df = pd.read_csv(term)

print(term_df.info())


def assign_category(term):
    first_letter = term[0].upper()
    if first_letter in 'ABCDEF':
        return 'Category 1: A-F'
    elif first_letter in 'GHIJKL':
        return 'Category 2: G-L'
    elif first_letter in 'MNOPQR':
        return 'Category 3: M-R'
    else:
        return 'Category 4: S-Z'

# Add the new 'Category' column
term_df['Category'] = term_df['Terms'].apply(assign_category)

# Print all terms, their meanings, and categories
for index, row in term_df.iterrows():
    term = row['Terms']
    meaning = row['Term_Meaning']
    category = row['Category']
    print(f"Term: {term}")
    print(f"Meaning: {meaning}")
    print(f"Category: {category}")
    print("-" * 50)  # Print a separator line

# Optionally, save the updated DataFrame to a new CSV file
term_df.to_csv('terms_meanings_categories.csv', index=False)
print("Updated CSV file 'terms_meanings_categories.csv' has been created.")


# dandruff_row = term_df[term_df['Terms'] == 'Dandruff']

# # Check if 'Dandruff' was found
# if not dandruff_row.empty:
#     term = dandruff_row['Terms'].values[0]
#     meaning = dandruff_row['Term_Meaning'].values[0]
#     print(f"Term: {term}")
#     print(f"Meaning: {meaning}")
# else:
#     print("The term 'Dandruff' was not found in the CSV file.")



# for index, row in term_df.iterrows():
#     term = row['Terms']
#     meaning = row['Term_Meaning']
#     print(f"Term: {term}")
#     print(f"Meaning: {meaning}")
#     print("-" * 50)  