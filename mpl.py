import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

date_x = [datetime(2019, 10, 30),
datetime(2019, 10, 1),
datetime(2019, 9, 1),
datetime(2019, 8, 1),
datetime(2019, 7, 1),
datetime(2019, 6, 1),
datetime(2019, 5, 1),
datetime(2019, 4, 1),
datetime(2019, 3, 1),
datetime(2019, 2, 1),
datetime(2019, 1, 1),
datetime(2018, 12, 1),
datetime(2018, 11, 1),

]

closing_y = [

139.2,
138.68,
134.49,
130.63,
129.5,
123.99,
117.58,
123.6,
118.2,
121.4,
123.17,
116.8,
121.48,


]

plt.plot(date_x, closing_y)

plt.xlabel('Date')
plt.ylabel('Closing Stock')

plt.title('Toyota Historical Data Chart')

plt.tight_layout()
plt.show()



