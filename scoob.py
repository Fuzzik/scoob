import discord
import random
import sys
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print(f"Scoob is up and running.\nScoob's user ID is {client.user.id}.")

@client.event
async def on_member_join(member):
	print(f"{member} has joined the server.")

@client.event
async def on_member_remove(member):
	print(f"{member} has left the server.")

@client.command()
async def ping(ctx):
	await ctx.send(f"{ctx.message.author.mention} Pong! Bot latency is {round(client.latency * 1000)}ms.")

@client.command(aliases = ["8ball"])
async def _8ball(ctx):
	responses = ["It is certain.",
				 "It is decidedly so.",
				 "Without a doubt.",
				 "Yes - definitely.",
				 "You may rely on it.",
				 "As I see it, yes.",
				 "Most likely.",
				 "Outlook good.",
				 "Yes.",
				 "Signs point to yes.",
				 "Reply hazy, try again.",
				 "Ask again later.",
				 "Better not tell you now.",
				 "Cannot predict now.",
				 "Concentrate and ask again.",
				 "Don't count on it.",
				 "My reply is no.",
				 "My sources say no.",
				 "Outlook not so good.",
				 "Very doubtful."]
				 
	await ctx.send(f"{ctx.message.author.mention} {random.choice(responses)}")

@client.command()
async def closebot(ctx):
	if ctx.message.author.id == 000000000000000000:
		await ctx.send(f"{ctx.message.author.mention} Going offline.")
		await client.logout()
		await sys.exit()
	else:
		await ctx.send(f"{ctx.message.author.mention} Permission denied.")

client.run("YOUR_TOKEN_HERE")
