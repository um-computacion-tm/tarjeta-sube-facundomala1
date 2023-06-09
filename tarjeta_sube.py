import unittest


PRECIO_TICKET=70
PRIMARIO='primario'
SECUNDARIO='secundario'
UNIVERSITARIO='universitario'
JUBILADO='jubilado'
ACTIVADO='activado'
DESACTIVADO='desactivado'
PENDIENTE='pendiente'


DESCUENTOS = {
    PRIMARIO: 0.50,
    SECUNDARIO: 0.40,
    UNIVERSITARIO: 0.30,
    JUBILADO: 0.25,
}

class NoHaySaldoException():
    pass

class Sube ():

    def __init__(self):
        self.saldo=0
        self.grupo_beneficiario=None
        self.estado="activado"
    
    def obtener_precio_tickets(self):
        if self.grupo_beneficiario in DESCUENTOS.keys():
            return PRECIO_TICKET * DESCUENTOS.get(self.grupo_beneficiario)
        else:
            return PRECIO_TICKET
   
    def pagar_pasaje(self):
        if self.estado==DESACTIVADO:
            raise UsuarioDesactivadoException('Usuario desactivado')
        else:
            if self.grupo_beneficiario in DESCUENTOS.keys():
                if self.saldo>=PRECIO_TICKET*DESCUENTOS.get(self.grupo_beneficiario):
                    self.saldo-=(PRECIO_TICKET*DESCUENTOS.get(self.grupo_beneficiario))
                else:
                    raise NoHaySaldoException('No tenes saldo')
            else:
                if self.saldo>=PRECIO_TICKET:
                    self.saldo-=PRECIO_TICKET
                else:
                    raise NoHaySaldoException("no tenes saldo")
                
    def cambiar_estado(self,estado):
        if estado==ACTIVADO or estado==DESACTIVADO:
            self.estado=estado
        else:
            raise EstadoNoExistenteException('Estado no existente')
 
class UsuarioDesactivadoException ():
    pass

class EstadoNoExistenteException():
    pass

