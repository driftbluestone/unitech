import discord, io, random
import numpy as np  
import matplotlib.pyplot as plt
from discord import app_commands
from discord.ext import commands
from PIL import Image
from pathlib import Path
DIR = Path(__file__).parent.absolute()

phi = (((5 ** 0.5) + 1) / (4*np.pi))
def graph_spiral():
    img = Image.new("RGBA", (2000, 2000), color=(0, 0, 0))
    im = Image.new("RGBA", (2000, 2000), color=(0, 0, 0, 0))
    for i in range(4):
        theta = np.linspace(i*(np.pi/2), (4*np.pi)+(i*(np.pi/2)))
        r = (np.e ** (phi * theta))
        fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
        ax.spines['polar'].set_color((0, 0, 0, 0))
        ax.patch.set_alpha(0)
        ax.grid(False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.plot(theta, r, color = (1, 1, 1), linewidth = 2)
        buffer = io.BytesIO()
        fig.savefig(buffer, dpi = 300, transparent=True)
        plt.close()
        plot = Image.open(buffer)
        im.paste(plot, (0, 0), plot)
    
    im = im.crop(im.getbbox()).resize((2000, 2000))
    img.paste(im, (0, 0), im)
    image = io.BytesIO()
    img.save(image, "PNG")
    image.seek(0)
    return image

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UniTech(bot=bot))
random.seed(0)

star_data = {
    "yellow": {
        "color": (255, 255, 0),
        "size": 8
    },
    "blue": {
        "color": (0, 0, 255),
        "size": 13
    },
    "red": {
        "color": (255, 0, 0),
        "size": 18
    }
}    
class UniTech(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="starmap", description="starmap? maybe!")
    async def starmap(self, interaction: discord.Interaction):
        await interaction.response.send_message(file=discord.File(fp=graph_spiral(), filename="dn.png"))
