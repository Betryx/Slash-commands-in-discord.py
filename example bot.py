from typing import Text
from asyncio.base_events import Server
import discord
from discord import message
from discord import member
from discord import colour
from discord import user
from discord import voice_client
from discord import reaction
from discord import guild
from discord import channel
from discord.embeds import Embed 

from discord.ext.commands.errors import MissingPermissions
from discord.role import Role
from discord.user import User #Helps building bots
from discord import Member
import re
import time
from discord.ext import commands#this submodule is required to actually add commands to the bot
from discord_slash import SlashCommand# Thats the module that you have to install and imort as its shown in this file
from discord import message
import discord
bot = commands.Bot(command_prefix="Your prefix here")
slash = SlashCommand(bot, sync_commands=True)#That enables the slash commands 
bot.event
async def on_ready():#the on ready function for message after the successful login of the client
    print("Bot is turned on")
@slash.slash(name="name of the command", description="the description of the command")# an actual slash command
async def function_name(ctx: commands.Context):
    await ctx.send("")
bot.run("Your token")