import numpy as np
from pprint import pprint
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='ALPHAVANTAGE_API_KEY', output_format='pandas')
data, meta_data = ts.get_weekly(symbol='MSFT')
#pprint(data.head(2))
print(data)

