import logger

"""logging"""
 
#logging setup
logger.register("eng") #I'm an actual idiot
displogs=False #Enable/Disable to start/stop debug messages

def log(msg,lvl=0):
	"""wraper for the logger library"""
	logger.inlog(msg=msg,lvl=lvl,src="eng")
	if displogs==True:
		print(logger.outlog("eng"))
	else:
		pass


log("hello")

"""error class"""
class InvalidCoords(BaseException):
	pass
class FailedToAddManager(BaseException):
	pass

"""classes"""
class board(): 
	def __init__(self,name): 
		tiles=[] 
		pieces=[]
		self.name=name
		self.tiles=tiles
		self.pieces=pieces
	def addtile(self,til): 
		if isinstance(til,tile): 
			self.pieces.append(til) 
		return isinstance(til,tile) 
		
	def addpiece(self,pce): 
		if isinstance(pce,piece): 
			if pce.addManager(self) == True:
				 self.pieces.append(pce)
				 log("ORIGIN: "+str(self)+" (name: "+str(self.name)+" in method: addpiece,MSG: added piece: "+str(pce)+" (name: "+str(pce.name)+")")
			else:
				raise FailedToAddManager

		return isinstance(pce,piece) 
		
	def coords_exist(self,x,y): 
		for piece in self.pieces: 
			if (x,y) == (piece.x,piece.y): 
				return True
		return False 
		 
	def gattr(self,ix,iy,attr):
		for piece in self.pieces:
			#log((place),(place.x),(place.y))
			if (ix,iy)==(piece.x,piece.y):
				try:
					if attr=="descrip":
						log(piece.descrip)
						return piece.descrip
				except:
					pass
				 
class tile(): 
	def __init__(self,name,x,y,descrip=None): 
		self.name=name 
		self.y=y 
		self.x=x 
		self.y=y 
		self.descrip=descrip 

		

	
class piece(): 
	def __init__(self,name,x,y): 
		mgeng=None
		self.name=name 
		self.x=x 
		self.y=y 
		self.mgeng=mgeng
	
	def addManager(self,MgEng):
		if isinstance(MgEng,board):
			self.mgeng=MgEng
			return True
		else:
			return False
	def goto(self,x,y): 
		if self.mgeng.coords_exist(x,y): 
			self.x=x 
			self.y=y
			return True
		else:
			log("no such coord: "+str((x,y))+" in mg. eng. : "+str(self.mgeng))
		return False
	def look(self):
		return self.mgeng.gattr(self.x,self.y,"descrip")

class item():
	def __init__(self,name,descrip=None):
		holder=None#container is more logical but to avoid conflicts its holder
		self.name=name
		self.descrip=descrip
		self.holder=holder
	def setHolder(self,newholder):
		#TODO:flesh out/more security
		if isinstance(newholder, container):
			self.holder=newholder

class container():
	def __init__(self,name,descrip=None):
		inventory=[]
		self.name=name
		self.descrip=descrip
		self.inventory=inventory
	def TransferItem(self,itm,newcontainer):
		#Verifies existence of new container, iniate RecieveItem for recipient, and finally removes item from self upon confirmation by recipient
		if isinstance(newcontainer,container):
			log("ORIGIN: "+str(self)+" (name: "+str(self.name)+") in method: TransferItem, MSG: "+"Target: "+str(newcontainer)+" (name: "+str(newcontainer.name)+") is an instance of container")
			if newcontainer.RecieveItem(itm,self):
				self.inventory.remove(itm)
				log("ORIGIN: "+str(self)+" (name: "+str(self.name)+") in method: TransferItem, MSG: Validated and transfered item: "+str(itm)+" (name: "+str(itm.name)+") to container: "+str(newcontainer)+" (name: "+str(newcontainer.name)+")")
			else:
				pass
	def RecieveItem(self,itm,src):
		#Reciever of items from TransferItem,must confirm reception of item before finalization.
		#TODO: Add default security/auth for item reception.
		if isinstance(src,container):
			log("ORIGIN: "+str(self)+" (name: "+str(self.name)+") in method: RecieveItem, MSG: "+"src: "+str(src)+" (name: "+str(src.name)+") is an instance of container")
			try:
				self.inventory.append(itm)
				itm.setHolder(self)
				log("ORIGIN: "+str(self)+" (name: "+str(self.name)+") in method: RecieveItem,MSG: Recieved item: "+str(itm)+" (name: "+str(itm.name)+")")
				return True
			except:
				return False
			
	def _InitItem(self,itm):
		#Only to be used for initial setup!
		#Similair in functionality as Recieve item,but explicitly and only for the initial population of a container by a board/manager.
		if isinstance(itm, item):
			try:
				self.inventory.append(itm)
				itm.setHolder(self)
				og("ORIGIN: "+str(self)+" (name: "+str(self.name)+") in method: _InitItem, MSG: Initiated item: "+str(itm)+" (name: "+str(itm.name)+")")
				return True
			except:
				return False
				#for added security,if strict was enabled raise error for unauthorized item moving: possible cheating
