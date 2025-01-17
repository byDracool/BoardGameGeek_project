import reflex as rx
from enum import Enum

#Constants

#Sizes
class Size(Enum):
    EXTRA_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "1em"
    DEFAULT = "2em"
    LARGE = "3em"
    BIG = "4em"

#Styles
BASE_STYLE = {
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

pretitle_style = dict(
    size="9",
    padding_top=Size.SMALL.value
)

title_style = dict(
    size="13",
    padding_top=Size.EXTRA_SMALL.value
)