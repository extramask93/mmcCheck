import re
import json

def checkParam(line,ommitUnknown=False,lNumber='0'):
    #extract key
    mo=re.search(r'^\w{2,5}',line)
    if(mo==None):         
        print('Error(line: '+lNumber+'): Cannot find function footprint')
        return 1
    key=mo.group(0);
    #load database as dictionary
    database = open('database.txt','r')
    database_str = database.read()
    data=json.loads(database_str)
    if((key not in data)):
        if(ommitUnknown):
            return 0
        else:
            print('Error(line: '+lNumber+'): Unknown command')
            return 1
    reg = re.compile(r'^'+key+r'\s+'+data[key]+r'\s*$|\'')
    mo=reg.search(line)
    if(mo!=None):
        print(mo.group(0))
    else:
        print('Error(line: '+lNumber+'): Parameters not matching function footprint')
##############################################
def checkFile(filename):
    file=open(filename,'r')
    counter = 1
    for line in file.readlines():
        counter+=1
        line=line.strip()
        if(line[0]=='!' or line[0]=='\''):
            continue
        else:
            wholemo=re.search(r'^\w{2,5}\s+[0-9A-Za-z,]*($|[^\'])',line)
            if(wholemo==None):
                print('Error(line: '+str(counter)+'): Unknown format')
                continue
            checkParam(wholemo.group(0),True,str(counter-1))
checkFile('foo2.txt')
