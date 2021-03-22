from PtgQst.eng import *
from PtgQst.logger import logger

""" 
docs and details:

Thershan: Local region

"""

thershan=board("Thershan")

#pieces
thaeron=piece("Thaeron Forsyth",0,0)

#tiles
tavern=tile("Tavern",0,1,"")
plaza=tile("Plaza",0,0,"A busy plaza in the center of town.")
blacksmith=tile("Blacksmith",-1,0,"A blisteringly hot blacksmith, a fine source of quality weapons.")
stable=tile("Stable",1,0,"Sawdust and hay fill the air in this old stable.")

#init
thershan.addtile(tavern)
thershan.addtile(plaza)
thershan.addtile(blacksmith)
thershan.addtile(stable)

thershan.addpiece(thaeron)


if __name__ == "__main__":
    print(thaeron.look())
