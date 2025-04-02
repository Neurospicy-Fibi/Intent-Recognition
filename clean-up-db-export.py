import json
from datetime import datetime

def clean_json_data(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Clean each record
    cleaned_data = []
    for record in data:
        # Create a new record without the specified fields
        cleaned_record = {
            'intent': record['intent'],
            'likelyOtherIntents': record['likelyOtherIntents'],
            'model': record['model'],
            'text': record['text']
        }
        
        # Convert createdAt from MongoDB format to ISO format
        if 'createdAt' in record:
            # Extract the date string from the MongoDB format
            date_str = record['createdAt']['$date']
            # Convert to datetime object
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            # Add to cleaned record
            cleaned_record['createdAt'] = date_obj.isoformat()
        
        cleaned_data.append(cleaned_record)
    
    # Write the cleaned data to output file
    with open(output_file, 'w') as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    input_file = "data/db_export.json"
    output_file = "data/recognized_intents.json"
    clean_json_data(input_file, output_file)
    print(f"Cleaned data has been written to {output_file}") 