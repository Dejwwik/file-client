import requests

# REST Client

def rest_stat(uuid, base_url):

    # Constructs the URL for the stat endpoint
    url = f"{base_url.rstrip('/')}/file/{uuid}/stat/"

    response = requests.get(url)
    if response.status_code == 200:

        # If the request was successful, parse the JSON response
        data = response.json()
        create_datetime = data.get("create_datetime")
        size = data.get("size")
        mimetype = data.get("mimetype")
        name = data.get("name")

        # Check if all required data is present
        if create_datetime and size and mimetype and name:
            print(data)
        else:
            raise ValueError("Data was not fully received.")
        
    elif response.status_code == 404:
        print("File not found.")

    else:
        # Handle other error cases
        print(f"Error code: {response.status_code}\nError content: {response.content}")

def rest_read(uuid, base_url):
    
    url = f"{base_url.rstrip('/')}/file/{uuid}/read/"
    response = requests.get(url)

    # Process the response based on the status code
    if response.status_code == 200:
        return response.content
    
    elif response.status_code == 404:
        print("File not found.")
        return None
    else:
        print(f"Error code: {response.status_code}\nError content: {response.content}")
        return None

