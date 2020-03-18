from CalculadoraComplejos import *
def ExperimentoCanicas(vectorEstado,canicas,nclicks):
    for i in range(nclicks):
        vectorEstado = vectorxmatrizReales(vectorEstado,canicas)
    return vectorEstado
def ExperimentoRendijasProb(nrendijas,resultado,inicio,vectorEstado):
    for i in range(nrendijas):
            inicio = producto_matricesReales(inicio,inicio)
    respuesta=vectorxmatrizReales(vectorEstado,inicio)
        return respuesta
"La funcion es la misma para cuantico y probabilistico ya que la funcion sirve para n rendijas"
