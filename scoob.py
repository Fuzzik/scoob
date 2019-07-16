import discord
import sys

client = discord.Client()
token = "YOUR_TOKEN_HERE"

@client.event
async def on_message(message):
	# We don't want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content == "!hello":
		msg = "Hello {0.author.mention}".format(message)
		await client.send_message(message.channel, msg)

	if message.content == "!closebot" and message.author.id == "SOME_USER_ID":
		msg = "Going offline (takes a few minutes)".format(message)
		await client.send_message(message.channel, msg)
		client.logout()
		sys.exit()

@client.event
async def on_ready():
	print("Scoob is up and running")
	print("Scoob's User ID is:", client.user.id)

client.run(token)
