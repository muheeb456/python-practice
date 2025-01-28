import json
import requests
import sys

def searchasong(singer):
    response = requests.get(r"https://itunes.apple.com/search?entity=song&limit=1&term="+singer)
    # print(response.json())
    print(json.dumps(response.json(),indent=2))

def searchsongs(singer,limit):
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={limit}&term="+singer)
    response = response.json()
    for result in response["results"]:
        print(result["trackName"])

def main():
    if len(sys.argv) == 2:
        searchasong(sys.argv[1])
    if len(sys.argv) == 3:
        searchsongs(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()
    