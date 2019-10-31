import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
from matplotlib import pyplot as plt

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

9205,
9452,
8287,
9623,
10027,
10801,
8742,
5379,
4178,
3887,
3523,
3844,
4023,


]

plt.plot(date_x, closing_y)

plt.xlabel('Date')
plt.ylabel('Closing Stock')

plt.title('Bincoin Historical Data Chart')

plt.tight_layout()
plt.savefig('Bincoin.png')
plt.show()