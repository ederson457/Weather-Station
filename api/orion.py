



import os
import requests
import requests.exceptions

def get_data():
  print("::: SOLAR SYSTEM INFORMATION")
  url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"


  try:
    #OK
    #Request to API

    res = requests.get(url)
    res.raise_for_status()

    #convert answer to JSON (JS object Notation)
    data = res.json() 
  except requests.exceptions.RequestException as e:
    print(f"API error: {e}")


get_data()


os.system('clear')
