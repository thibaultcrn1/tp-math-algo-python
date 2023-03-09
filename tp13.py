import time
import random

# Question 1
def tri_select(L: []):
    for i in range (len(L)-1):
        a=i
        for k in range(i+1, len(L)):
            if L[k] < L[a]:
                a=k;
        L[i], L[a] = L[a], L[i]
    return L;

# Question 2
def tri_bulles(L: []):
    for i in range (len(L)):
        for k in range (0, len(L)-i-1):
            if L[k] > L[k+1]:
                L[k], L[k+1] = L[k+1], L[k];
    return L;

def testTime():
    Lh=[random.randint(1, 100) for i in range(100)]
    tb_debut=time.time();
    tri_bulles(Lh);
    tb_fin=time.time();
    tb_temps=tb_debut-tb_fin;

    ts_debut = time.time();
    tri_select(Lh);
    ts_fin = time.time();
    ts_temps = ts_debut-ts_fin;

    print("tri_bulles a mis ", tb_temps, " milisecondes d'execution.");
    print("tri_select a mis ", ts_temps, " milisecondes d'execution.");
    return;



testTime();