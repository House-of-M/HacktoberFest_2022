# Discord Bot
This is a simple and plain Discord bot that you can use as it is as a demo or customize it to learn how to build Discord bots.
- Try adding more input and responses in `responses.py`
- Try add more interaction types by adding a feature for the bot to prompt gifs when using specific commands... etc

To run the demo bot:
`python main.py`

Before testing out this bot, threre are some steps to follow first;

## Setup instructions
- install discord.py package: `pip install discord.py`
- Create a discord server

### Discord Developer Portal: 
Go to: https://discord.com/developers/applications
This is where you need 

### OAuth2
#### General
Default Authorization :
- In-app Authorization

Scopes:
- Bot

Bot Permissions:
- Check whatever permision boxes you wish for the bot to have (advice; avoid admin perms.)

#### URL Generator
- check the same previous perms
- Copy the generated URL; it serves as the invite for your Bot to a server (use it with your test server)

#### Privileged Gateway Intents
-Presence Intent: on
-Server Members Intent: on
-Message Content Intent: on

### Bot
#### Build-A-Bot
- Click on: "Add Bot"
- Click on "Reset Token"

NOTE: The token is unique to you, don't share it with anyone. Keep it in a separate file because it won't be visible again on that page unless you reset it.

## Preview
![discord-bot-demo-preview](https://www.pixenli.com/image/jYLT-t3F)