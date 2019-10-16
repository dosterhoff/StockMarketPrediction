import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer

engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format('username', 'password', 'host:port', 'database'))
con = engine.connect()

df.to_sql(name='test', con=con, if_exists='append', index=False)

df = pd.DataFrame([['a', 1, 1, 2.0, datetime.now(), True]], 
                  columns=['str', 'int', 'float', 'datetime', 'boolean'])
print(df.dtypes)

from sqlalchemy.types import NVARCHAR, Float, Integer
dtypedict = {
  'str': NVARCHAR(length=255),
  'int': Integer(),
  'float' Float()
}

df.to_sql(name='test', con=con, if_exists='append', index=False, dtype=dtypedict)

dtypedict = {
  'str': NVARCHAR(length=255),
  'int': Integer(),
  'float' Float()
}
df.to_sql(name='test', con=con, if_exists='append', index=False, dtype=dtypedict)

def mapping_df_types(df):
    dtypedict = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            dtypedict.update({i: NVARCHAR(length=255)})
        if "float" in str(j):
            dtypedict.update({i: Float(precision=2, asdecimal=True)})
        if "int" in str(j):
            dtypedict.update({i: Integer()})
    return dtypedict

 df = pd.DataFrame([['a', 1, 1, 2.0, datetime.now(), True]], 
                  columns=['str', 'int', 'float', 'datetime', 'boolean'])
dtypedict = mapping_df_types(df)
df.to_sql(name='test', con=con, if_exists='append', index=False, dtype=dtypedict)
