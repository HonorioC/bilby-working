import matplotlib
#matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

from gwpy.timeseries import TimeSeries
import bilby
import numpy as np
from bilby.core.utils import random


data = TimeSeries.fetch_open_data('L1', 'Sep 14 2015 09:50:29', 'Sep 14 2015 09:51:01')

plot = data.plot()
#plt.show()
plt.savefig("test.png")