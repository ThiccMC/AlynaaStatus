import discord

class EmbedBuilder:
    def __init__(self, description, title=None, color=discord.Color.default(), fields=None, thumbnail=None, author=None, footer=None):
        self.title = title
        self.description = description
        self.color = color
        self.fields = fields
        self.thumbnail = thumbnail
        self.author = author
        self.footer = footer

    def build(self):
        if self.title is not None:
            embed = discord.Embed (
                title = self.title,
                description = self.description,
                color = self.color
            )
            if self.fields is not None:
                for field in self.fields:
                    embed.add_field(name=field[0], value=field[1], inline=field[2])
            if self.thumbnail is not None:
                embed.set_thumbnail(url=self.thumbnail)
            if self.author is not None:
                if len(self.author) == 1:
                    embed.set_author(name=self.author[0])
                elif len(self.author) == 2:
                    embed.set_author(name=self.author[0], icon_url=self.author[1])
                elif len(self.author) == 3:
                    embed.set_author(name=self.author[0], icon_url=self.author[1], url=self.author[2])
            if self.footer is not None:
                if len(self.footer) == 1:
                    embed.set_footer(text=self.footer[0])
                elif len(self.footer) == 2:
                    embed.set_footer(text=self.footer[0], icon_url=self.footer[1])
            return embed
        elif self.title is None:
            embed = discord.Embed (
                description = self.description,
                color = self.color
            )
            if self.fields is not None:
                for field in self.fields:
                    embed.add_field(name=field[0], value=field[1], inline=field[2])
            return embed
