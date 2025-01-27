import requests
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
#from BGG_project.python_code.vars_and_consts import USER
#from BGG_project.python_code.vars_and_consts import PORTFOLIO
from BGG_project.python_code.vars_and_consts import PORTFOLIO


print(PORTFOLIO)
#print(USER)
#variable = requests.get("https://www.boardgamegeek.com/xmlapi2/collection?username=byDracool&subtype=boardgame&own=1")
#SD = variable.text
#print(SD)