import time
import numpy as np
import math
class Network:
    def __init__(self,inputsize,hLayersize,outputsize):
        self.inputL = []
        self.hLayer = []
        self.output = []
        self.w1 = Network.generatewb(inputsize,hLayersize)
        self.w2 = Network.generatewb(hLayersize,outputsize)
        self.b1 = Network.generatewb(1,hLayersize)
        self.b2 = Network.generatewb(1,outputsize)
        self.inputsize = inputsize
        self.hLayersize  = hLayersize
        self.outputsize = outputsize
    @staticmethod
    def generatewb(iSize,oSize):
        return np.random.random((iSize,oSize))
    @staticmethod
    def sigmoid(x):
        return 1/(1 + np.exp(-x))
    def displaywb(self):
        print("w1")
        print(self.w1)
        time.sleep(5)
        print("w2")
        print(self.w2)
        time.sleep(5)
        print("b1")
        print(self.b1)
        time.sleep(5)
        print("b2")
        print(self.b2)
    


