import json, random, io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from . import consts
from pathlib import Path
DIR = Path(__file__).parent.absolute()

def graph_spiral(spirals: int, size): 
    img = Image.new("RGBA", (2000, 2000), color=(0, 0, 0))
    plot_white= Image.new("RGBA", (2000, 2000), color=(0, 0, 0, 0))
    for i in range(spirals):
        theta = np.linspace(i*(2 * (np.pi) / spirals), (2*np.pi)+(i*(2 * (np.pi) / spirals)), 1000)
        r = (np.e ** (consts.phi * theta))
        fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
        
        ax.spines['polar'].set_color((0, 0, 0, 0))
        ax.patch.set_alpha(0)
        ax.grid(False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.plot(theta, r, color = (1, 1, 1), linewidth = 80 // spirals)
        buffer = io.BytesIO()
        fig.savefig(buffer, dpi = 300, transparent=True)
        plot = Image.open(buffer)
        plot_white.paste(plot, (0, 0), plot)
        
        plt.close()
    
    plot_white = plot_white.crop(plot_white.getbbox()).resize((2000, 2000))
    plot_white = zoom(plot_white, size)
    img.paste(plot_white, (0, 0), plot_white)

    return img

def place_stars(img: Image.Image, count):
    stars = []
    width, height = img.size
    width -= 1
    height -= 1
    image = Image.new("RGBA", (2000, 2000), color=(0, 0, 0))
    im = ImageDraw.Draw(image)
    for i in range(count):
        coords = (random.randint(1, width), random.randint(1, height))
        color = img.getpixel(coords)
        if color <= (0.1, 0.1, 0.1):
            continue
        star = random.choice(list(consts.star_data.keys()))
        im.circle(coords, consts.star_data[star]["size"], tuple(consts.star_data[star]["color"]))
        stars.append({"type": star, "position": list(coords)})
    
    with open(f"{DIR}/starmap.json", "w") as file:
        json.dump(stars, file, indent=2)
    return image

def zoom(image: Image.Image, scale: float) -> Image.Image:
    width, height = image.size
    image = image.resize((int(width * scale), int(height * scale)))
    crop = ((image.width - width) // 2, (image.height - height) // 2, (image.width + width) // 2, (image.height + height) // 2)
    image = image.crop(crop)
    return image

if __name__ == "__main__":
    random.seed(0)
    place_stars(graph_spiral(4, 0.8), 4000).show()