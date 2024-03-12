import os
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and result.scheme in ['http', 'https']
    except ValueError:
        return False

def save_file(filename, content):
    try:
        if os.path.isfile(filename):
            if input(f"File with name {filename} already exists!!! Type \"y\" for overwrite     ").lower() != "y":
                print("File content was not been saved. Try again with different filename or overwrite existing file!")
                return 

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(file=filename, mode="wb") as file:
            file.write(content)

        print(f"Content was saved into file {filename}")
            
    except Exception as e:
        print(f"Error while saving the file. Error content:\n{e}")