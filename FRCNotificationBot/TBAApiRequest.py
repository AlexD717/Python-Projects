import requests # type: ignore

# Define the API endpoint and any parameters
url = "https://www.thebluealliance.com/api/v3"  # Replace with the actual API URL
params = {
    "X-TBA-Auth-Key": "vuKa1Oef0QiLsJg64lygiZsLY51u65Kx3DYRLS601oVJBcartJpF16d8N4kRzhwD",  # Replace with actual query parameters
}
TEAM_KEY = "frc2898" # TODO change to actual team id
EVENT_KEY = "2025orore" # TODO change to actual event id

matchesAnalyzed = []

with open('data.txt', 'r') as file:
    print("Loading previous data")
    for line in file.readlines():  
        matchesAnalyzed.append(line.strip())
    print(matchesAnalyzed)

def SaveMatchesAnalyzed():
    with open ("data.txt", "w") as file:
        for match in matchesAnalyzed:
            file.write(f"{match}\n")

def CheckData():
    print("")
    print("Requesting Data")

    # Make a GET request to the API
    response = requests.get(url+f"/team/{TEAM_KEY}/event/{EVENT_KEY}/matches", params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()
        newMatches = []
        i = False
        for matchData in data:
            if (matchData["alliances"]["red"]["score"] == -1):
                matchHappened = False
            else:
                matchHappened = True
            if (matchHappened):
                try:
                    if ((str(matchData["match_number"])+matchData["comp_level"]) not in matchesAnalyzed):
                        if TEAM_KEY in matchData["alliances"]["red"]["team_keys"]:
                            teamColor = "red"
                            oppositeColor = "blue"
                        else:
                            teamColor = "blue"
                            oppositeColor = "red"
                        if matchData["winning_alliance"] == teamColor:
                            won = True
                        else:
                            won = False
                        matchesAnalyzed.append(str(matchData["match_number"])+matchData["comp_level"])
                        newMatches.append([won, teamColor, matchData["alliances"][teamColor]["score"], matchData["alliances"][oppositeColor]["score"], matchData["match_number"]])
                except:
                    print("ERROR ANALYIZING DATA")
        SaveMatchesAnalyzed()
        if (len(newMatches) > 0):
            print("Data Analized With No Errors")
            return newMatches
        else:
            return None   
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    
#print(CheckData())