import discord
import asyncio
import json
import time
from discord.ext import commands
from discord.ext.commands import Bot

class cog_example(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(cog_example(client))
