# Autor: Giovanny Alexis Reyes Vilchis
# Matricula: 2163031812

class Tape(object):
    B = " "     # Símbolo en blanco
    
    def __init__(self, cinta_string = ""):
        self.cinta = dict((enumerate(cinta_string)))
        # la última línea es equivalente a las siguientes tres líneas:
        # self.cinta = {}
        # for i in range(len(cinta_string)):
        #   self.cinta[i] = input[i]

    def __str__(self):
        s = ""
        min_index = min(self.cinta.keys())
        max_index = max(self.cinta.keys())
        for i in range(min_index, max_index):
            s += self.cinta[i]
        return s

    def __getitem__(self,index):
        if index in self.cinta:
            return self.cinta[index]
        else:
            return Tape.B

    def __setitem__(self, posicion, char):
        self.cinta[posicion] = char


class TuringMachine(object):
    def __init__(self, cinta = "", B = " ", q0 = "", F = None, delta = None):
        self._cinta = Tape(cinta)
        self.cabezal = 0
        self._B = B
        self.estado_actual = q0
        if delta == None:
            self._delta = {}
        else:
            self._delta = delta
        if F == None:
            self._F = set()
        else:
            self._F = set(F)
    
    def get_tape(self): 
        return str(self._cinta)
    
    def step(self):
        casilla = self._cinta[self.cabezal]
        x = (self.estado_actual, casilla)
        if x in self._delta:
            y = self._delta[x]
            self._cinta[self.cabezal] = y[1]
            if y[2] == "R":
                self.cabezal += 1
            elif y[2] == "L":
                self.cabezal -= 1
            self.estado_actual = y[0]

    def final(self):
        if self.estado_actual in self._F:
            return True
        else:
            return False
    

# Usando la clase TuringMachine:

q0 = {"inicio"}    # Estado de inicio
delta = {("inicio","0"):("inicio", "1", "R"),
         ("inicio","1"):("inicio", "0", "R"),
         ("inicio"," "):("final"," ", "N"),
        }    # Función de transicion
F = {"final"}    # Estado final o de aceptación

mt = TuringMachine("010011001 ", 
                  q0 = "inicio",
                  F = F,
                  delta = delta)

print("\nEntrada de la cinta:\n" + mt.get_tape())

while not mt.final():
    mt.step()

print("\nResultado del cálculo de la máquina de Turing:")    
print(mt.get_tape()+"\n")
