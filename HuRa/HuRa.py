

import numpy as np
import random as rn
import matplotlib.pyplot as plt
import math




class randomLister():
    def __init__(self, n):
        self.figure = plt.figure()
        self.n = n
        self.data = np.load("HuRa\Output12.npy", allow_pickle= True)
    
    def takeinputs(self, lis, times):
        for g in range(times):
            datalist = []
            for i in range(self.n**2):
                datalist.append(rn.choice(lis))
            plt.imshow(np.reshape(np.array(datalist), (self.n,-1)))
            plt.show(block = False)

            self.data = np.append(self.data, [datalist, input("Does this look random? \n")])
    def createarraynoin(self, lis, times):
        datacreated = []
        for g in range(times):
            datalist = []
            for i in range(self.n**2):
                datalist.append(rn.choice(lis))
            plt.imshow(np.reshape(np.array(datalist), (self.n,-1)))
            
            datacreated.append(datalist)

            plt.show()
        return datacreated


        
    def save(self):
        np.save("HuRa\Output12.npy", np.array(self.data, dtype=object))
        print(f" check {np.shape(self.data)}")