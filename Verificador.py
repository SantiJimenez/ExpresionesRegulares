import re

patronVariable = re.compile('^[a-z][A-Za-z0-9\_]*$')
patronOperador = re.compile('^[/|+|=|*|-]{1}$')
patronValor = re.compile('[+-]?\d+(\.\d+)?')


def verificarToken(token):

    if patronVariable.match(token):
            print "variable valido " + token
            return True
    elif patronOperador.match(token):
            print "operador valido " + token
            return True
    elif patronValor.match(token):
            print "valor valido " + token
            return True
    else:
    	return False