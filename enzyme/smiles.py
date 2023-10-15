import re
import subprocess
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Define the text containing chemical reactions
text = "vinylacetyl-CoA = (E)-but-2-enoyl-CoA"


# Use ChemSpot to extract chemical entities
def extract_chemical_entities(text):
    # Run ChemSpot on the input text
    cmd = f'echo "{text}" | java -jar chemspot.jar --web'
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    chemspot_output = result.stdout

    # Parse the ChemSpot output to extract recognized chemical entities
    entities = re.findall(r"\[.*?\]", chemspot_output)
    return entities


# Use PubChem to retrieve SMILES notation for chemical entities
def get_smiles_from_pubchem(entity):
    # Construct the PubChem URL for the entity
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/compound/{entity}"
    try:
        # Retrieve the PubChem page and parse it
        with urlopen(pubchem_url) as response:
            pubchem_page = response.read()
            soup = BeautifulSoup(pubchem_page, "html.parser")

            # Find the SMILES notation on the page
            smiles_tag = soup.find("div", {"class": "smiles"})
            if smiles_tag:
                return smiles_tag.text.strip()
    except Exception as e:
        print(f"Error: {str(e)}")
    return None


# Extract chemical entities from the text
chemical_entities = extract_chemical_entities(text)

# Look up SMILES notation for each entity
smiles_dict = {}
for entity in chemical_entities:
    entity = entity[1:-1]  # Remove square brackets
    smiles = get_smiles_from_pubchem(entity)
    if smiles:
        smiles_dict[entity] = smiles
    else:
        print(f"SMILES notation not found for: {entity}")

# Print the results
for entity, smiles in smiles_dict.items():
    print(f"{entity}: {smiles}")
