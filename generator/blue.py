import random
from PIL import Image
import os
try:
    from generator.base import LicensePlateGenerator
except Exception as e:
    from .base import LicensePlateGenerator


class BluePlate(LicensePlateGenerator):

    def __init__(self):
        super(BluePlate, self).__init__()
        self.length = 5

    def random_number(self):
        area = random.choice(self.areas)
        chars = ''
        for _ in range(self.length):
            chars += random.choice(self.letters)
        return area+chars

    def generate(self):
        plate = self.random_number()
        image = Image.new('RGBA', (440, 140), color=(0, 0, 0, 0))
        for index, char in enumerate(list(plate)):
            char_image = Image.open(os.path.join(
                'generator', 'images', 'black', f'{char}.png')).convert('RGBA')
            char_image = char_image.resize((45, 90), Image.ANTIALIAS)
            x = 0
            y = 25
            if index == 0:
                index = 15
            elif index == 1:
                x = 15 + 45 * index + 12 * index
            else:
                x = 15 + 45 * index + 12 * (index + 1) + 10
            image.paste(char_image, (x, y))
        canvas_image = Image.new("RGBA", image.size, "BLUE")
        canvas_image.paste(image, mask=image)
        return canvas_image.convert("RGB"), plate


if __name__ == '__main__':
    from matplotlib import pyplot as plt

    generator = BluePlate()
    image, plate = generator.generate()
    # image.save(f'output/blue_{plate}.png')

    plt.imshow(image)
    plt.show()
