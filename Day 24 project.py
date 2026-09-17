import requests
try:
    
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    print(data["fact"])

except requests.exceptions.RequestException:
    print("Sorry! Couldn't connect to the API's server")


