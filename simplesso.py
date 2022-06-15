import numpy as np
#-----------------Inserimento dei coefficienti della F.O-------------------
def inserimentoC(n):
    print("------INSERIMENTO vettore c ------------------")
    c = [];
    for i in range(0,n):
        get = input("inserisci");
        
        c.append(int(get));
    return(c);
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
def getRedCost(xb,A,c):
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
    return(cd-(cb*(np.linalg.inv(B)*D)));

A=inserimentoA();
c=inserimentoC(np.shape(A)[1]);
while(True):
    print("\n intervallo indici: [0,"+str(np.shape(A)[1]-1)+"]")
    xb=inserimentoIndiciBasici(np.shape(A)[0]);
    redCost=getRedCost(xb,A,c);
    print("COEFFICIENTI DI COSTO RIDOTTO:",redCost);
    if(np.amax(redCost)<=0):
        print("SOLUZIONE OTTIMALE, xb = ",xb);
    print("-------------------------");
