import os

import matplotlib
from matplotlib import font_manager

FONTS_DIR = 'fonts'
FONT_NAME = "IPAexGothic"
FONT_TTF = 'ipaexg.ttf'


def japanize() -> None:
    font_dir_path = get_font_path()
    font_dirs = [font_dir_path]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    if hasattr(font_manager.fontManager, 'addfont'):
        for fpath in font_files:
            font_manager.fontManager.addfont(fpath)
    else:
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
    matplotlib.rc('font', family=FONT_NAME)


def get_font_ttf_path() -> str:
    return os.path.join(get_font_path(), FONT_TTF)


def get_font_path() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), FONTS_DIR))


japanize()
