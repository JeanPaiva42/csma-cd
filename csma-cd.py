import random as rand
import matplotlib.pyplot as plt

class Falantes:
    name = None
    randInt = None
    fala = None

    def setName(self, n):
        self.name = n
    def setRandInt(self, r):
        self.randInt = rand.randint(0,r)
    def setFala(self, f):
        self.fala = f
    def getName(self):
        return self.name
    def getRandInt(self):
        return self.randInt
    def getFala(self):
        return self.fala


def auxCsmaCd(vetorzin, vaiFalar):
    a = None
    add=0
    proxVets = vetorzin
    queroFalar = vaiFalar
    if proxVets[0]:
        if(len(proxVets[0])>0):
            a = rand.randint(0, len(proxVets[0])-1)
        else:
            a = rand.randint(0,0)
        print 'Falador diz.... ' + proxVets[0][a].getName()
        if proxVets[0][a] in queroFalar:
            print proxVets[0][a].getName() + ' finalmente falou!!'
            add+=1
        proxVets[0].pop(a)
    for i in range(0, len(proxVets)):
    #add vetor de vetor e etc
        c = []
        proxVets.append(c)
    for j in proxVets[0]:
        randVec = rand.randint(1, len(proxVets)-1)
        proxVets[randVec].append(j)
    return [proxVets, queroFalar, add]





def csmaCd(canal, chances):
    #A simulacao poderia ser um pouco mais leve, mas estou tentando fazer com que as coisas se visualizem melhor
    colisoes = [[]]
    vaiFalar = []
    numFalante=0
    numTentouFalar=0
    nomes = ['mario','Tifa','MegaMan','Cloud', 'Lightning', 'Squall', 'Zidane', 'Vivi', 'Barret', 'Terra']
    for i in range(0, chances):
        a = rand.randint(0, 9)
        nomes.append(nomes[a]+str(i))
    falador = []
    for i in range(0, len(nomes)):
        o = Falantes()
        o.setName(nomes[i])
        falador.append(o)

    for p in range(0, chances):
        
            
        for f in falador:
            f.setRandInt(chances)
            if(f.getRandInt() <= canal):
                colisoes[0].append(f)
                vaiFalar.append(f)
            
                print f.getName()+ " quer falar..."
                numTentouFalar+=1
        vets = auxCsmaCd(colisoes, vaiFalar)
        colisoes = vets[0]
        vaiFalar = vets[1]
        numFalante+= vets[2]
       
       
    print 'Finalizando protocolo...'
    print str(numTentouFalar)+" "+ str(numFalante)
    return [numTentouFalar, numFalante]

print 'Iniciando protocolo...'
pl = csmaCd(1, 100)
labels = ['Tentaram Falar', 'Conseguiram Falar']
sizes = [pl[0],pl[1]]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
plt.ylabel('colisoes atraves do tempo')

    
