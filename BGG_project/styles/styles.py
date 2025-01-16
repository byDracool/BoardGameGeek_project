import reflex as rx
from enum import Enum

#Constants

#Sizes
class Size(Enum):
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
