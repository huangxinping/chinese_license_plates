import random
from PIL import Image
import os
try:
    from generator.base import LicensePlateGenerator
except Exception as e:
    from .base import LicensePlateGenerator


class YellowPlate(LicensePlateGenerator):

    def __init__(self):
        super(YellowPlate, self).__init__()
        self.length = 5

    def random_number(self):
        area = random.choice(self.areas)
        chars = ''
        for _ in range(self.length):
            chars += random.choice(self.letters)
        return area+chars

    def generate(self):
        plate = self.random_number()
        image = Image.new('RGBA', (440, 220), color=(0, 0, 0, 0))
        for index, char in enumerate(list(plate)):
            x = 0
            y = 0
            if index <= 1:
                char_image = Image.open(os.path.join(
                    'generator', 'images', 'yellow', 'top', f'{char}.png')).convert('RGBA')
                char_image = char_image.resize((80, 60), Image.ANTIALIAS)
                y = 15
                if index == 0:
                    x = 110
                else:
                    x = 110 + 80 + 25 + 10 + 25
            else:
                char_image = Image.open(os.path.join(
                    'generator', 'images', 'yellow', 'bottom', f'{char}.png')).convert('RGBA')
                char_image = char_image.resize((65, 110), Image.ANTIALIAS)
                y = 15 + 60 + 15
                if index == 2:
                    x = 27
                else:
                    x = 27 + 65 * (index - 2) + 15 * (index - 2)
            image.paste(char_image, (x, y))
        canvas_image = Image.new("RGBA", image.size, "YELLOW")
        canvas_image.paste(image, mask=image)
        return canvas_image.convert("RGB"), plate


class YellowGuaPlate(YellowPlate):

    def random_number(self):
        area = random.choice(self.areas)
        chars = ''
        for _ in range(self.length-1):
            chars += random.choice(self.letters)
        chars += '挂'
        return area+chars


if __name__ == '__main__':
    from matplotlib import pyplot as plt

    generator = YellowPlate()
    image, plate = generator.generate()
    # image.save(f'output/yellow_{plate}.png')

    generator = YellowGuaPlate()
    image, plate = generator.generate()
    # image.save(f'output/yellow_gua_{plate}.png')

    plt.imshow(image)
    plt.show()
