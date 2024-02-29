import numpy as np
from pprint import pprint
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='ALPHAVANTAGE_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
#pprint(data.head(2))
print(data.head(2))