from PtgQst.eng import *
from PtgQst.logger import logger

""" 
docs and details:

Thershan: Local region

"""

thershan=board("Vale of Thershan")


"""Vale of Thershan"""
#tiles

#thershan proper
tavern=tile("Tavern",0,1,"A buzzing tavern, everything that happens in this town happens here.")
plaza=tile("Plaza",0,0,"A busy plaza in the center of town.")
blacksmith=tile("Blacksmith",-1,0,"A blisteringly hot blacksmith, a fine source of quality weapons.")
stable=tile("Stable",1,0,"Sawdust and hay fill the air in this old stable.")
avenue=tile("Avenue",0,-1,"The central avenue, bustling with people and commerce")
#highway
junction=tile("Junction",0,-2,"The  throughfare meets the great highway at a T shaped junction.")
westroad=tile("East Road",-1,-2,"The highway continues a distance,largely devoid of traffic")
westturn=tile("East  Turn",-2,-2,"The road turns to the south near the edge of a dark wood")
southwestroad=tile("Southern Road",-2,-3,"Splitting the dark wood to the west and the steppe to the west, the highway continues on as far as the eye can see")
#Gateway of the great woods
gateway=tile("Gateway of the Dark Wood",-3,-2,"An ancient ruin, vaguely in the shape  of an arch, seemingly beckoning to the old forest beyond")
#steppe
northweststeppe=tile("Western Steppe",-1,-3,"An empty and rolling steppe, plains as far as the eye can see.")
northsteppe=tile("Northern Steppe",0,-3,"A lone hill overlooking the junction and the surrounding steppe,the remains of a fire indicate infrequent usage")

#init

#thershan proper
thershan.addtile(tavern)
thershan.addtile(plaza)
thershan.addtile(blacksmith)
thershan.addtile(stable)
thershan.addtile(avenue)
#highway
thershan.addtile(junction)
thershan.addtile(westroad)
thershan.addtile(westturn)
thershan.addtile(southwestroad)
#steppe
thershan.addtile(northweststeppe)
thershan.addtile(northsteppe)
#gateway
thershan.addtile(gateway)


def piecetoboard(pce):
	thershan.addpiece(pce)


if __name__ == "__main__":
    print(thaeron.look())
