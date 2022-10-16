import os
import discord

from discord import Intents

Intents.message_content = True
client = discord.Client(intents = Intents.all())
token = os.environ["token"]

import time