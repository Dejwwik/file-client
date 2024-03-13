import os
from urllib.parse import urlparse

def is_valid_url(url) -> bool:
    """ Check if a URL is valid."""
    try:
        result = urlparse(url)

        # Check if the URL has both scheme and netloc, and the scheme is either 'http' or 'https'
        return all([result.scheme, result.netloc]) and result.scheme in ['http', 'https']
    except ValueError:
        return False

def save_file(filename, content) -> None:
    """Save content to a file."""
    
    try:
        # Check if the file already exists
        if os.path.isfile(filename):
            # Ask user if they want to overwrite the existing file
            if input(f"File with name {filename} already exists!!! Type \"y\" for overwrite ").lower() != "y":
                print("File content was not been saved. Try again with different filename or overwrite existing file!")
                return 

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Write content to file
        with open(file=filename, mode="wb") as file:
            file.write(content)

        print(f"Content was saved into file {filename}")
            
    except Exception as e:
        print(f"Error while saving the file. Error content:\n{e}")