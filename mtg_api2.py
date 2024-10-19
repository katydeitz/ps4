import requests
from collections import defaultdict

def get_formats():
    # Endpoint for formats
    url = 'https://api.magicthegathering.io/v1/formats'

    try:
        # Sending a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if the request failed

        # Parse the JSON response
        data = response.json()

        # Get the list of formats
        formats = data.get('formats', [])
        if not formats:
            print("No formats found.")
            return

        # Categorize formats alphabetically
        categorized_formats = defaultdict(list)
        for format in formats:
            first_letter = format[0].upper()  # Get the first letter for categorization
            categorized_formats[first_letter].append(format)

        # Display categorized formats
        print("Magic: The Gathering Formats by Category:")
        for letter, format_list in sorted(categorized_formats.items()):
            print(f"\n{letter}:")
            for format_name in format_list:
                print(f"  - {format_name}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the API: {e}")

if __name__ == '__main__':
    get_formats()
