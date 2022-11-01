# Actual learning model using the data from "Output12.npy" 
# To make predictions of human randomness.

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn. model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from HuRa import randomLister

choice = list(np.linspace(1, 100, num = 20))
dataGen = randomLister(4)
dataGen.takeinputs(choice, 10)
dataGen.save()
_hold = np.logical_or(np.logical_or(dataGen.data == "yes", dataGen.data == "no"), dataGen.data== "nho")
tags = np.reshape(np.extract(_hold, dataGen.data), [-1, 1])
data = np.extract(np.logical_not(_hold), dataGen.data)
data2 = []

for i in data:
    data2.append(np.array(i))

tags[tags == "yes"] = 1
tags[tags == "no"] = 0
tags[tags == "nho"] = 0
tags = tags.astype("int")

model = MLPClassifier(hidden_layer_sizes=(100, 100, 10), max_iter=100)

model.fit(data2, tags.ravel())
for i in range(5):
    new_data = dataGen.createarraynoin(choice, 1)
    for i in model.predict(new_data):
        if i == 1:
            print("Looks humanly random")
        elif i == 0:
            print("Doesn't look humanly random")
