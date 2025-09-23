import json

# Just check the first few lines of the JSON file
print("Reading first 1000 characters of fraud labels...")
with open('train_fraud_labels.json', 'r') as f:
    first_part = f.read(1000)

print("First 1000 characters:")
print(first_part)
print("\n" + "="*50)

# Try to parse just a small sample
print("\nTrying to parse as JSON...")
try:
    with open('train_fraud_labels.json', 'r') as f:
        # Read just the first line to see the structure
        first_line = f.readline()
        print("First line:", first_line[:200])
        
        # Check if it's a single JSON object or array
        f.seek(0)
        first_char = f.read(1)
        print(f"First character: '{first_char}'")
        
        if first_char == '{':
            print("Looks like a JSON object")
        elif first_char == '[':
            print("Looks like a JSON array")
        else:
            print("Unknown format")
            
except Exception as e:
    print(f"Error: {e}")
