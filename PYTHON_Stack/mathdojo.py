import statistics as stats
class Mathdojo:
    def __init__(self):
        self.result=0
        self.results =[]
    
    def add(self, *numbs):
        for x in numbs:
            self.result += x
        print(f"El resultado es {self.result}")
        self.results.append(self.result)
        return self
    
    def substract(self, *numbs):
        for x in numbs:
            self.result -= x
        print(f"El resultado es {self.result}")
        self.results.append(self.result)
        return self

    def stand_desv(self):
        if len(self.results)<2:
            print("No hay suficientes resultados para calcular la desviación estándar")
            return self
        self.vari=stats.stdev(self.results)
        print(f"La desviación estándar de los resultados es {self.vari}")
        return self
    
    def reset(self):
        self.result=0
        self.results= []
        return self

op= Mathdojo()
op.reset() .add(3,4) .add(6,8,3) .add(2,5,7,8,1) .substract(3,5) .substract(15,5) .substract(-10,-30) .stand_desv() .results

