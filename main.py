import discord, io, random
import numpy as np  
import matplotlib.pyplot as plt
from discord import app_commands
from discord.ext import commands
from PIL import Image, ImageDraw
from pathlib import Path
DIR = Path(__file__).parent.absolute()

random.seed(0)
phi = (((5 ** 0.5) + 1) / (2*np.pi))
def graph_spiral(spirals: int): 
    img = Image.new("RGBA", (2000, 2000), color=(0, 0, 0))
    plot_gray = Image.new("RGBA", (2000, 2000), color=(0, 0, 0, 0))
    plot_white= Image.new("RGBA", (2000, 2000), color=(0, 0, 0, 0))
    for i in range(spirals):
        theta = np.linspace(i*(2 * (np.pi) / spirals), (2*np.pi)+(i*(2 * (np.pi) / spirals)), 1000)
        r = (np.e ** (phi * theta))
        fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
        
        ax.spines['polar'].set_color((0, 0, 0, 0))
        ax.patch.set_alpha(0)
        ax.grid(False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.plot(theta, r, color = (1, 1, 1), linewidth = 20)
        buffer = io.BytesIO()
        fig.savefig(buffer, dpi = 300, transparent=True)
        plot = Image.open(buffer)
        plot_white.paste(plot, (0, 0), plot)

        ax.plot(theta, r, color = (0.5, 0.5, 0.5), linewidth = 40)
        buffer = io.BytesIO()
        fig.savefig(buffer, dpi = 300, transparent=True)
        plot = Image.open(buffer)
        plot_gray.paste(plot, (0, 0), plot)
        
        plt.close()
    
    plot_gray = plot_gray.crop(plot_gray.getbbox()).resize((2000, 2000))
    plot_white = plot_white.crop(plot_white.getbbox()).resize((2000, 2000))
    
    img.paste(plot_gray, (0, 0), plot_gray)
    img.paste(plot_white, (0, 0), plot_white)

    image = io.BytesIO()
    img.save(image, "PNG")
    image.seek(0)
    return image

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UniTech(bot=bot))

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
    async def starmap(self, interaction: discord.Interaction, arms: int):
        await interaction.response.defer()
        await interaction.followup.send(file=discord.File(fp=graph_spiral(arms), filename="dn.png"))

if __name__ == "__main__":
    image = Image.open(graph_spiral(4))
    image.show()