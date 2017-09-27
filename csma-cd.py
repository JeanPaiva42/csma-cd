import random as rand


class Falantes:
    name = None
    randInt = None
    fala = None

    def setName(self, n):
        self.name = n
    def setRandInt(self):
        self.randInt = rand.randint(0,100)
    def setFala(self, f):
        self.fala = f
    def getName(self):
        return self.name
    def getRandInt(self):
        return self.randInt
    def getFala(self):
        return self.fala


def auxCsmaCd(vetorzin):
    a=None
    proxVets = vetorzin
    if proxVets[0]:
        if(len(proxVets[0])>0):
            a = rand.randint(0, len(proxVets[0])-1)
        else:
            a = rand.randint(0,0)
            print proxVets
        print str(a) + ' '+ str(len(proxVets[0]))
        print proxVets
        print 'Falador diz.... iiadia ' + proxVets[0][a].getName()
        proxVets[0].pop(a)
    for i in range(0, len(proxVets)):
    #add vetor de vetor e etc
        c = []
        proxVets.append(c)
    print 'vetor acrescido '
    print proxVets
    for j in proxVets[0]:
        randVec = rand.randint(1, len(proxVets)-1)
        proxVets[randVec].append(j)
    print 'antes '
    print proxVets
    proxVets.pop(0)
    print 'dps '
    print proxVets
    return proxVets





def csmaCd():
    colisoes = [[]]
    nomes = ['romario','ronaldin','pele','cloud']
    falador = []
    for i in range(0,3):
        o = Falantes()
        o.setName(nomes[i])
        falador.append(o)

    for p in range(0, 100):
        for f in falador:
            f.setRandInt()
        for f in falador:   
            if(f.getRandInt() <= 30):
                colisoes[0].append(f)
        #if(len(colisoes[0]) == 1):
            #print 'Falador diz.... ' + colisoes[0][0].getName()
            #sinal = True
        colisoes = auxCsmaCd(colisoes)     
            
       
       
    print colisoes
    print 'Finalizando protocolo...'


print 'Iniciando protocolo...'
csmaCd()
    
    
