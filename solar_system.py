import random, math
from PIL import Image, ImageDraw
try:
    from . import consts
except:
    import consts

def solar_system(star, planet_count):
    img = Image.new("RGBA", (2000, 2000), (0, 0, 0))
    im = ImageDraw.Draw(img)
    star = consts.star_data[star]
    center = (img.width // 2, img.height // 2)
    last_radius = star["size"] * 20
    im.circle(center, last_radius, tuple(star["color"]))
    
    for i in range(planet_count):
        last_radius += random.randint(100, 300)
        im.circle(center, last_radius, None, (255, 255, 255))
        rotation = random.random() * math.pi * 2
        planet = (center[0] + (last_radius * math.cos(rotation)), center[1] + (last_radius * math.sin(rotation)))
        im.circle(planet, random.randint(20, 50), (92, 67, 39))
        math.pi
    return img

if __name__ == "__main__":
    solar_system("yellow", 4).show()