from PtgQst.eng import *
from PtgQst.eng import logger
from data import *

thaeron=piece("Thaeron Forsyth",0,0)
displog=True
game=True

logger.register("main")

def log(msg,lvl=0):
	"""wraper for the logger library"""
	logger.inlog(msg=msg,lvl=lvl,src="main")
	if displog==True:
		print(logger.outlog("main"))
	else:
		pass


def InputProcessor(inp,plr=thaeron):
	inp=inp.lower()
	if inp == "look":
		return plr.look()
	elif inp == "north":
		if plr.goto(plr.x,plr.y+1):
			return
		else:
			return "You can't go that way"
	elif inp == "east":
		if plr.goto(plr.x+1,plr.y):
			return
		else:
			return "You can't go that way"
	elif inp == "south":
		if plr.goto(plr.x,plr.y-1):
			return
		else:
			return "You can't go that way"
	elif inp == "west":
		if plr.goto(plr.x-1,plr.y):
			return
		else:
			return "You can't go that way"
	elif inp == "help":
		print("Currently only one word commands are supported.")
		print("Commands include: look,north,south,east,and west."
piecetoboard(thaeron)

if __name__=="__main__":
	while game==True:
		command=input(": ")
		output=InputProcessor(command)
		if output != None:
			print(output)

