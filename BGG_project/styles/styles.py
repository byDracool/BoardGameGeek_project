import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

#Sizes
class Size(Enum):
    EXTRA_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "1em"
    MEDIUM_PLUS = "1.5em"
    DEFAULT = "2em"
    LARGE = "3em"
    BIG = "4em"
    EXTRA_BIG = "8em"

#Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color":Color.BACKGROUND.value,
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}



navbar_style = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM_PLUS.value
)

header_style = dict(
    font_family=Font.TITLE.value,
    color=TextColor.HEADER.value
)

finder_style = dict(
    font_family=Font.DEFAULT.value,
    color=TextColor.BODY.value,
    font_size=Size.MEDIUM_PLUS.value
)

footer_style = dict(
    font_family=Font.FOOTER.value,
    color=TextColor.FOOTER.value
)

game_description_style = dict(
    font_family=Font.DESCRIPTION.value,
    font_weight=FontWeight.EXTRA_LIGHT.value,
    font_style="italic",
    color=TextColor.BODY.value,
    font_size=Size.MEDIUM.value,
)

game_title_style = dict(
    font_family=Font.TITLE.value,
    color=TextColor.HEADER.value,
    font_style="italic",
)