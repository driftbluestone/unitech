import discord, io, random
from discord import app_commands
from discord.ext import commands
from . import galaxy, solar_system, consts
from pathlib import Path
DIR = Path(__file__).parent.absolute()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UniTech(bot=bot))


class UniTech(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="starmap", description="starmap? maybe!")
    async def starmap(self, interaction: discord.Interaction, seed: int):
        random.seed(seed)
        await interaction.response.defer()
        im = galaxy.place_stars(galaxy.graph_spiral(4, 0.8), 4000)
        image = io.BytesIO()
        im.save(image, "PNG")
        image.seek(0)
        await interaction.followup.send(file=discord.File(fp=image, filename="dn.png"))
    
    @app_commands.command(name="solar_system", description="solar system? maybe!")
    async def solar_system(self, interaction: discord.Interaction, seed: int):
        random.seed(seed)
        await interaction.response.defer()
        im = solar_system.solar_system(random.choice(list(consts.star_data.keys())), 4)
        image = io.BytesIO()
        im.save(image, "PNG")
        image.seek(0)
        await interaction.followup.send(file=discord.File(fp=image, filename="dn.png"))

if __name__ == "__main__":
    random.seed(0)
    galaxy.place_stars(galaxy.graph_spiral(4, 0.8), 4000).show()