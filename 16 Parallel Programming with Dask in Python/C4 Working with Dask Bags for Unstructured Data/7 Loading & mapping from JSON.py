"""Loading & mapping from JSON
A collection of JSON files for Congressional bills have been downloaded from GovTrack.us. All bills presented during each congressional session from 1973 - 2017 are provided in separate files.

Your job is to read the bills*.json files into a Dask Bag. You'll then use the JSON module to map the text of each file into Python dictionaries. You'll then inspect the first element of the Dask Bag."""

# Call db.read_text with congress/bills*.json: bills_text
bills_text = db.read_text('congress/bills*.json')

# Map the json.loads function over all elements: bills_dicts
bills_dicts = bills_text.map(json.loads)

# Extract the first element with .take(1) and index to the first position: first_bill
first_bill = bills_dicts.take(1)[0]

# Print the keys of first_bill
print(first_bill.keys())
