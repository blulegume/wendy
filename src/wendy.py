import discord

class Wendy(discord.Client):
    def __init__(self, word_count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_count = word_count
        self.windbag = None

    async def on_ready(self):
        print('Beep boop I have started')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        elif len(message.content.split()) > self.word_count:
            await message.channel.send("Sir this is a Wendy's")
            self.windbag = message.author
            print(f'{message.author} sure is a windbag')
        elif self.windbag and message.author == self.windbag:
            await message.channel.send('We serve food here, sir')
            self.windbag = None
        else:
            self.windbag = None

