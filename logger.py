#doc: log lvl: 0=info,1=debug,2=warning,3=error
#doc: logmng inst=logmng, logcli inst=logcli

"""setup"""
mlr=[] #master log record
regclis=[] #registered clients,form: (src,srcoblbl)

class InvalidLogSource(BaseException):
    pass

def register(src):
    """records new clients to setup log inbox"""
    #src should be a CONSISTENT unique identifier
    srcoblblname=str(src)+'_oblbl'
    globals()[srcoblblname]=[]
    regclis.append((src,srcoblblname))

def checksrc(src):
    for cliset in regclis:
        if cliset[0]==src:
            return True
    return False

def inlog(src,lvl,msg):
    """takes new inbound logs"""
    if not checksrc(src):
        register(src)
        if not checksrc(src):
            raise InvalidLogSource
    log=(src,lvl,msg)
    mlr.append(log)
    for cli in regclis:
        eval(cli[1]).append(log)

def outlog(src):
    if not checksrc(src):
        raise InvalidLogSource
    for cliset in regclis:
        if src==cliset[0]:
            templist=eval(cliset[1]).copy()
            eval(cliset[1]).clear()
            return templist

def masterlog():
    return mlr
