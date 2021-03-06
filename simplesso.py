import numpy as np
#-----------------Inserimento dei coefficienti della F.O-------------------
def inserimentoC(n):
    print("------INSERIMENTO vettore c ------------------")
    c = [];
    for i in range(0,n):
        get = input("inserisci");
        
        c.append(int(get));
    return(c);
def inserimentob(m):
    print("------INSERIMENTO vettore b ------------------")
    b = [];
    for i in range(0,m):
        get = input("inserisci");
        
        b.append(int(get));
    b = np.array(b);
    return(b);
#--------------------------------------------------------------------------
def inserimentoA():
    stop=False;
    alert=0;
    A=[];
    while stop==False:
        if alert>=2:
            stop=True;
            break;
        get = input("inserire nuova riga");
        if(get==''):
            alert=alert+1;
        Ax=[];
        stop2=False
        while stop2==False:
            get = input("inserisci");
            if(get==''):
                alert=alert+1;
                stop2=True;
                continue;
            else:
                alert=0;
                Ax.append(int(get));
        if(alert<2):
            A.append(Ax)
    A=np.matrix(A)
    print(A);
    return(A);

def inserimentoIndiciBasici(m):  
    print("------INSERIMENTO INDICI VARIABILI BASICHE ------------------")
    xb = [];
    for i in range(0,m):
        get = input("inserisci l'indice della variabile in base");
        xb.append(int(get));
    return(xb);
def getRedCost(xb,A,c,b):
    B=[];
    cb=[];
    D=[];
    cd=[];
    n=np.shape(A)[1];
    for i in range(0,n):
        if i in xb:
            cb.append(c[i]);
            B.append(A[:,i].flatten().tolist()[0])
        else:
            cd.append(c[i]);
            D.append(A[:,i].flatten().tolist()[0])

    cb=np.array(cb);
    cd=np.array(cd);
    B=np.transpose(np.matrix(B));
    D=np.transpose(np.matrix(D));

    print("-----A-----\n")
    print(A)        
    print("\n-----B-----")

    print(B)
    print("\n cb=",cb)
    print("-----D-----")
    print(D)
    print("\n cd=",cd)

    print("------------------------------")
    xb=np.array(xb)[np.newaxis].T;
    b=b[np.newaxis].T;
    soluzione = np.linalg.inv(B)*b;
    print ("-------SOLUZIONE---------")
    
    if(np.amin(soluzione)<0):
        print("inammissibile")
        print(soluzione);
        return 1
    print(soluzione);
    redCost=cd-(cb*(np.linalg.inv(B)*D));
    print("-------------------------- \n COEFFICIENTI DI COSTO RIDOTTO:",redCost);
    return(redCost);

A=inserimentoA();
m,n=np.shape(A);
c=inserimentoC(n);
b=inserimentob(m);
while(True):
    print("\n intervallo indici: [0,"+str(np.shape(A)[1]-1)+"]")
    xb=inserimentoIndiciBasici(np.shape(A)[0]);
    redCost=getRedCost(xb,A,c,b);
    if(np.amax(redCost)<=0):
        print("SOLUZIONE OTTIMALE, xb = ",xb);
    print("-------------------------");
