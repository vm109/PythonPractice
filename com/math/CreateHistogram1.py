import numpy as np
import  matplotlib.pyplot as plot

data = np.random.normal(0,10,10000)
plot.hist(data,50)
plot.show()