import pandas as pd

# File paths for the two Excel files
file1_path = 'data/sample_articles.xlsx'  # File containing articles in ColA
file2_path = 'data/replacement_sheet.xlsx'  # File containing strings to replace and their target values

# Load both Excel files into DataFrames
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)

# Drop NaN values``
df2.dropna(inplace = True)
# Create a dictionary from File 2 for the string replacements (String to Replace -> Target String)
replacements = dict(zip(df2['Str1'], df2['Str2']))  # Assuming 'ColA' has the strings to be replaced, 'ColB' has the target strings

print(replacements)

# Function to perform string replacement on each article
def replace_strings(article, replacements_dict):
    for old_str, new_str in replacements_dict.items():
        article = article.replace(old_str, new_str)
    return article

# Apply the replacement function to each article in File 1 (ColA)
df1['Updated_Articles'] = df1['Articles'].apply(lambda x: replace_strings(str(x), replacements))

# Save the modified articles back to a new Excel file
output_file = 'data/updated_articles.xlsx'
df1.to_excel(output_file, index=False)

print(f"String replacement complete! Output saved to '{output_file}'.")
