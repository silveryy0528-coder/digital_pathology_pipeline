import openslide
from PIL import Image


def open_slide(path):
    return openslide.OpenSlide(path)


def get_thumbnail(slide, size=(1024, 1024)):
    return slide.get_thumbnail(size)


def read_region(slide, location, level, size):
    img = slide.read_region(
        location=location,
        level=level,
        size=size
    )
    return img.convert("RGB")


def print_slide_info(slide):
    slide_props = slide.properties
    print('Pixel size of X in um: ', slide_props['openslide.mpp-x'])
    print('Pixel size of Y in um: ', slide_props['openslide.mpp-y'])
    print('Slide dimensions: ', slide.level_dimensions)
    print('Level downsample factors: ', slide.level_downsamples)