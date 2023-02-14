import discord, random
from discord.ext import commands

client = commands.Bot(command_prefix='.')
token = '' #Insert the bot's token here

@client.command()
async def ping(ctx):
    await ctx.reply(embed=discord.Embed(description=f"**PONG!**\nLatency: `{round(client.latency*1000)}ms`", color=ctx.author.color))

@client.event
async def on_ready():
    print("[+] BOT ONLINE")

@client.command(aliases=["d"])
async def draw(ctx, id:int, number:int):
    channel = client.get_channel(id)

    message = await channel.history(limit=number).flatten()
    new_list = [x for x in reversed(message)]
    selectedMessage = random.choice(new_list)
    url = f'https://discord.com/channels/{ctx.guild.id}/{id}/{selectedMessage.id}'

    embed = discord.Embed(colour=ctx.author.color) 
    embed.add_field(name='WINNER DRAWN', value=f'Click [here]({url}) to view the message\nCongratulations <@{selectedMessage.author.id}>!')
    await ctx.send(embed=embed)
@draw.error
async def draw_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(color=ctx.author.color,  description=f"{ctx.author.mention} Follow this pattern to draw a random message:\n`.d <channelId> <messageCount>`"))

client.run(token)
