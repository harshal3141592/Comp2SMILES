# Comp2SMILES

**Convert chemical compound names into SMILES representations using the PubChem database and Python.**

Comp2SMILES is a Python-based tool that automates the retrieval of Canonical SMILES strings for chemical compounds listed in an Excel spreadsheet. It uses the [PubChem PUG REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) to retrieve chemical structure information and exports the results into a new Excel file.

The tool is designed to simplify the process of converting compound names into machine-readable chemical structures, making it useful for preliminary cheminformatics workflows, chemical data preparation, and research applications.

## Features

- **Excel Input:** Reads compound names directly from an `.xlsx` file.
- **Automated Retrieval:** Queries PubChem using its PUG REST API.
- **SMILES Conversion:** Retrieves Canonical SMILES representations for recognised compounds.
- **Excel Output:** Exports compound names alongside their corresponding SMILES strings.
- **Lookup Status:** Identifies unsuccessful lookups using an `Invalid SMILES` placeholder.

## Project Structure

```text
Comp2SMILES/
│
├── Comp2SMILES.py
├── Input.xlsx
├── output_file.xlsx
└── README.md
```

`output_file.xlsx` is generated automatically when the script runs successfully.

## Requirements

- Python 3.x
- Internet connection
- PubChem API access

### Python Libraries

Install the required dependencies using pip:

```bash
pip install pandas requests openpyxl
```

| Library | Purpose |
|---|---|
| pandas | Reading and processing Excel data |
| requests | Sending requests to the PubChem API |
| openpyxl | Reading and writing `.xlsx` files |

## How to Use

### Step 1: Prepare the Input File

Create an Excel spreadsheet containing the compound names you want to convert.

The column header must be named exactly:

`Compound Name`

Example:

| Compound Name |
|---|
| Aspirin |
| Paracetamol |
| Ibuprofen |
| Caffeine |
| Metformin |

Save the spreadsheet as **Input.xlsx**.

### Step 2: Set Up the Project

Place `Input.xlsx` in the same directory as the Python script.

### Step 3: Run the Script

Open a terminal or command prompt in the project directory and execute:

```bash
python Comp2SMILES.py
```

Replace `Comp2SMILES.py` with your actual script filename if it differs.

### Step 4: Retrieve the Output

Once execution is complete, a new Excel file named **output_file.xlsx** will be generated in the same directory.

The output contains two columns:

| Compound Name | Canonical SMILES |
|---|---|
| Aspirin | CC(=O)Oc1ccccc1C(O)=O |
| Paracetamol | CC(=O)Nc1ccc(O)cc1 |
| Caffeine | CN1C(=O)N(C)c2ncn(C)c2C1=O |

*Illustrative output; actual results are retrieved from PubChem.*

## How It Works

Comp2SMILES uses the PubChem Power User Gateway REST API (PUG REST) to retrieve chemical information.

The workflow is:

1. Reads compound names from the input Excel spreadsheet.
2. Extracts the compound names into a Python list.
3. Sends individual name-based queries to PubChem.
4. Retrieves the requested Canonical SMILES property.
5. Stores the results alongside their corresponding compound names.
6. Exports the processed data into a new Excel spreadsheet.

## Limitations and Considerations

- An active internet connection is required for API queries.
- Compound names must be recognised by PubChem.
- Some compound names or synonyms may correspond to multiple PubChem records. Verify the retrieved chemical structure before using it in downstream research.
- Failed HTTP lookups are currently recorded as `Invalid SMILES`. This does not necessarily mean that the compound itself has an invalid structure.
- For larger datasets, follow PubChem's API usage recommendations and avoid excessive request rates.

## Data Source

**PubChem – National Center for Biotechnology Information (NCBI)**

[PubChem PUG REST Documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)

## Future Improvements

Potential extensions to the project include:

- Retrieval of additional chemical descriptors, such as molecular formula and molecular weight.
- Support for multiple SMILES formats and InChI identifiers.
- Improved API error handling and retry mechanisms.
- Batch processing and lookup optimisation for larger datasets.
- Integration with cheminformatics libraries such as RDKit for chemical structure validation and visualisation.

## Author

Developed as a Python learning project exploring API integration, chemical data retrieval, and automation of cheminformatics workflows.

Contributions, suggestions, and improvements are welcome!