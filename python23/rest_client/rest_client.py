#rest client
import requests

def rest_stat(uuid, base_url):
    url = f"{base_url.rstrip('/')}/file/{uuid}/stat/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        create_datetime = data.get("create_datetime")
        size = data.get("size")
        mimetype = data.get("mimetype")
        name = data.get("name")

        if create_datetime and size and mimetype and name:
            print({
                "create_datetime": data.get("create_datetime"),
                "size":  data.get("size"),
                "mimetype": data.get("mimetype"),
                "name": data.get("name")
            })
        else:
            raise ValueError("Data was not fully received.")
        
    elif response.status_code == 404:
        print("File not found.")

    else:
        print(f"Error code: {response.status_code}\nError content: {response.content}")


def rest_read(uuid, base_url):
    url = f"{base_url.rstrip('/')}/file/{uuid}/read/"
    response = requests.get(url)


    if response.status_code == 200:
        return response.content
    
    elif response.status_code == 404:
        print("File not found.")
        return None
    else:
        print(f"Error code: {response.status_code}\nError content: {response.content}")
        return None

