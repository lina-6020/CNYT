from CalculadoraComplejos import *
def ExperimentoCanicas(vectorEstado,canicas,nclicks):
    for i in range(nclicks):
        vectorEstado = vectormatrizReal(vectorEstado,canicas)
    return vectorEstado
def ExperimentoRendijasProb(nrendijas,resultado,inicio,vectorEstado):
    for i in range(nrendijas):
            inicio = producto_matrices_reales(inicio,inicio)
    respuesta=vectormatrizReal(vectorEstado,inicio)
    return respuesta
"La funcion es la misma para cuantico y probabilistico ya que la funcion sirve para n rendijas"
