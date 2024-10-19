import requests
from rich.console import Console
from rich.table import Table
from collections import defaultdict

def get_formats():
    # Endpoint for formats
    url = 'https://api.magicthegathering.io/v1/formats'
    console = Console()

    try:
        # Sending a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if the request failed

        # Parse the JSON response
        data = response.json()

        # Get the list of formats
        formats = data.get('formats', [])
        if not formats:
            console.print("[bold red]No formats found.[/bold red]")
            return

        # Categorize formats alphabetically
        categorized_formats = defaultdict(list)
        for format in formats:
            first_letter = format[0].upper()  # Get the first letter for categorization
            categorized_formats[first_letter].append(format)

        # Create a table to display the formats
        table = Table(title="Magic: The Gathering Formats")
        table.add_column("Letter", justify="center", style="bold cyan")
        table.add_column("Formats", justify="left", style="bold green")

        # Populate the table with categorized formats
        for letter, format_list in sorted(categorized_formats.items()):
            format_names = "\n".join(format_list)
            table.add_row(letter, format_names)

        # Print the table
        console.print(table)
    
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error accessing the API:[/bold red] {e}")

if __name__ == '__main__':
    get_formats()
