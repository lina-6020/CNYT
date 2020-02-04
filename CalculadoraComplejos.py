import math 
def sumar(numero1,numero2):
    resul1=numero1[0]+numero2[0]
    resul2=numero1[1]+numero2[1]
    return resul1,resul2
def restar(numero1,numero2):
    resul1=numero1[0]-numero2[0]
    resul2=numero1[1]-numero2[1]
    return resul1,resul2
def multiplicar(numero1,numero2):
    a=numero1[0]*numero2[0]
    b=numero1[0]*numero2[1]
    c=numero1[1]*numero2[0]
    d=numero1[1]*numero2[1]
    e=b+c
    f=a+d*-1
    return f,e
def conjugado(numero1):
    return numero1[0]*-1,numero1[1]*-1
def modulo(numero1):
    return (numero1[0]**2+numero1[1]**2)**0.5
def dividir(numero1,numero2):
    numero3=[]
    numero3=[numero2[0],numero2[1]*-1]
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
    resultado=(f/l,e/l)
    return resultado

def polar_cartesiano(numero1):
    r=numero1[0]
    angulo=numero1[1]*(math.pi/180)
    x=r*math.cos(angulo)
    y=r*math.sin(angulo)
    return x,y
    
def cartesiano_polar(numero1):
    r=((numero1[0]**2)+(numero1[1]**2))**0.5
    angulo=math.atan2(numero1[1],numero1[0])
    return r,(angulo*(180/math.pi))
def fase(numero1):
    fase=math.atan2(numero1[1],numero1[0])
    return fase
