
# Webpage: https://plot.ly


# THIS STEP IS EXECUTED ONLY ONCE
# import plotly
# plotly.tools.set_credentials_file(username='david.kuchelmeister', api_key='bm8uYBd56ekPOB39dLnv')
# plotly.tools.set_config_file(world_readable=True,sharing='public')

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in(username='david.kuchelmeister', api_key='9R4BOHtv4vk2KQGxQXJ7')

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.plot(data, filename = 'basic-line')