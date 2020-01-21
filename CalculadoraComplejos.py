from sys import stdin
def sumar(numero1,numero2):
    resul1=numero1[0]+numero2[0]
    resul2=numero1[1]+numero2[1]
    return resul1,resul2
def restar(numero1,numero2):
    resul1=numero1[0]-numero2[0]
    resul2=numero1[1]-numero2[1]
    print(resul1,resul2)
def multiplicar(numero1,numero2):
    a=numero1[0]*numero2[0]
    b=numero1[0]*numero2[1]
    c=numero1[1]*numero2[0]
    d=numero1[1]*numero2[1]
    e=b+c
    f=a+d*-1
    print(f,e)
def conjugado(numero1):
    return numero1[0]*-1,numero1[1]*-1
def dividir(numero1,numero2):
    numero3=conjugado(numero2)
    a=numero1[0]*numero3[0]
    b=numero1[0]*numero3[1]
    c=numero1[1]*numero3[0]
    d=numero1[1]*numero3[1]
    e=b+c
    f=a+d*-1
    g=numero2[0]*numero3[0]
    h=numero2[0]*numero3[1]
    i=numero2[1]*numero3[0]
    j=numero2[1]*numero3[1]
    k=h+i
    l=g+j*-1
    print(e,f)
    print(k,l)
def sumavector(vector1,vector2):
    vectorfinal=[]
    if len(vector1)==len(vector2):
        for i in range (len(vector1)):
            vectorfinal.append(sumar(vector1[i],vector2[i]))
    return vectorfinal
def inversovector(vector1):
    vectorfinal=[]
    for i in range (len(vector1)):
        vectorfinal.append(conjugado(vector1[i]))
    print(vectorfinal)
    


def main():
    vector1=[[-2.0, 3.0], [4.0, -5.0]]
    vector2=[[6.0, 7.0], [8.0, 9.0]]
##    numero1=([float(x) for x in stdin.readline().split(",")])
##    numero2=([float(x) for x in stdin.readline().split(",")])
##    sumar(vector1,vector2)
##    restar(numero1,numero2)
##    multiplicar(numero1,numero2)
##    conjugado(numero1)
##    dividir(numero1,numero2)
    sumavector(vector1,vector2)
    inversovector(vector1)
main()
