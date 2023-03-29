import numpy as np
class NeuronaMP:
    def __init__(self):
       self.threshold=None
    def Model(self,x):
        return  sum(x) >= self.threshold
    def Predict(self,x):
        Y=[]
        for y in x:
            result=self.Model(y)
            Y.append(result)
        return np.array(Y)    
        
if __name__ == "__main__":

  neurona=NeuronaMP()
  neurona.threshold=3
  resultado=neurona.Predict([[1,0,0,1],[0,0,0,1],[0,1,1,1]])
  print(resultado)