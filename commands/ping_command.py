from commands.base_command import BaseCommand
from random import randint
import urllib
from urllib.request import Request, urlopen

class Info(BaseCommand):
    
    def __init__(self):
        description = "Information About Us"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        req = Request('https://api.upload.systems/pastes/z9Y4kcSISykC/raw', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        for line in webpage:
        
            decoded_line = webpage.decode("utf-8")
            msg = message.author.mention + "\n" + decoded_line
        
        await message.channel.send(msg)
