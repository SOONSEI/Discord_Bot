import discord
from discord.ext import commands
from commands.base_command import BaseCommand
from random import randint
import urllib
from urllib.request import Request, urlopen

class Status(BaseCommand):
    
    def __init__(self):
        description = "roblox status"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        req = Request('https://api.upload.systems/pastes/Ev9wucN960mx/raw', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()


        for line in webpage:
            decoded_line = webpage.decode("utf-8")
            msg = decoded_line

            info_board = discord.Embed(
            title=msg,
            description=message.author.mention,
            colour=discord.Colour.red()
        )
        info_board.set_footer(text="Bot Person")

        
        await message.channel.send(embed=info_board)



