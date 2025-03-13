import discord
import asyncio
import TBAApiRequest

UPDATE_DELAY = 600
TEAM_NUMBER = 2898 # TODO set to actual team number

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CHANNEL_ID = 0 # TODO Set to actuall channel ID

async def GetTBAData():
    print("Getting TBA Data")
    newMatches = TBAApiRequest.CheckData()
    if (newMatches != None):
        for match in newMatches:
            print(match)
            if (match[0]):
                message = f"{TEAM_NUMBER} won match {match[4]} on {match[1]} alliance with a score of {match[2]} vs {match[3]}."
            else:
               message = f"{TEAM_NUMBER} lost match {match[4]} on {match[1]} alliance with a score of {match[2]} vs {match[3]}."
            print("Sending message: " + message)
            await channel.send(message)
    else:
       print("No new matches since last analyze")
    
    # Calls this function again with a delay
    print("Awaiting updated data")
    await asyncio.sleep(UPDATE_DELAY)
    asyncio.create_task(GetTBAData())

@client.event
async def on_ready():
  global channel
  print(f"Logged in as {client.user}")
  channel = client.get_channel(CHANNEL_ID)
  await channel.send("Logged in")
  await GetTBAData()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

client.run('TOKEN') # TODO set to actual discord bot token