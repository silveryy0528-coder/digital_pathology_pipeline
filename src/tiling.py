import numpy as np
from openslide.deepzoom import DeepZoomGenerator


def get_deepzoom_generator(slide, tile_size=512, overlap=0, limit_bounds=False):
    return DeepZoomGenerator(
        slide,
        tile_size=tile_size,
        overlap=overlap,
        limit_bounds=limit_bounds
    )


def extract_tile(tiles, level, row, col):
    return tiles.get_tile(level, (row, col))


def print_tile_info(tiles):
    num_levels = tiles.level_count
    print('Number of levels: ', num_levels)
    print('Level dimensions: ', tiles.level_dimensions)
    for level in range(num_levels):
        rows, cols = tiles.level_tiles[level]
        print(f'Level {level}: Number of tiles: ({rows}, {cols})')

    return level, rows, cols


def is_blank_tile(tile, threshold=220):
    tile_np = np.array(tile)
    return np.mean(tile_np) > threshold
