from generator import BlackPlate, WhitePlate, YellowPlate, YellowGuaPlate, GreenPlate, BluePlate
import random
from tqdm import tqdm
import os


def main():
    if not os.path.exists('output'):
        os.mkdir('output')
    plates = [
        BlackPlate(),
        WhitePlate(),
        YellowPlate(),
        YellowGuaPlate(),
        GreenPlate(),
        BluePlate()
    ]
    for _ in tqdm(range(10**3)):
        gen = random.choice(plates)
        image, plate = gen.generate()
        # You can enhance the image with https://github.com/aleju/imgaug
        image.save(os.path.join('output', f'{plate}.jpg'))


if __name__:
    main()
