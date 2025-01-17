import reflex as rx
from enum import Enum
from .colors import Color as Color

#Constants

#Sizes
class Size(Enum):
    EXTRA_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "1em"
    DEFAULT = "2em"
    LARGE = "3em"
    BIG = "4em"
    EXTRA_BIG = "8em"

#Styles
BASE_STYLE = {
    "background_color":Color.BACKGROUND.value,
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

pretitle_style = dict(
    size=Size.DEFAULT.value,
    padding_top=Size.SMALL.value
)

title_style = dict(
    size=Size.BIG.value,
    padding_top=Size.EXTRA_SMALL.value,
)