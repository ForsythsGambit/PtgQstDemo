from PtgQst.eng import *
from PtgQst.eng import logger
from data import *

thaeron=piece("Thaeron Forsyth",0,0)
piecetoboard(thaeron)
displog=True

logger.register("main")
def log(msg,lvl=0):
	"""wraper for the logger library"""
	logger.inlog(msg=msg,lvl=lvl,src="main")
	if displog==True:
		print(logger.outlog("main"))
	else:
		pass

if __name__=="__main__":
	while True:
		pass
