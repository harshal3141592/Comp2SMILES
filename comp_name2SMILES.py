import pandas as pd
import requests

# Read the Excel file
df = pd.read_excel('Input.xlsx')

# Extract compound names
compound_names = df['Compound Name'].tolist()

# Convert compound names to Canonical SMILES
canonical_smiles = []
for name in compound_names:
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/CanonicalSMILES/txt'
    response = requests.get(url)
    if response.status_code == 200:
        canonical_smiles.append(response.text.strip())
    else:
        canonical_smiles.append('Invalid SMILES')

# Create a new DataFrame with compound names and Canonical SMILES
result_df = pd.DataFrame({'Compound Name': compound_names, 'Canonical SMILES': canonical_smiles})

# Save the result to a new Excel file
result_df.to_excel('output_file.xlsx', index=False)
