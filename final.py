#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.types import NVARCHAR, Float, Integer

# 连接设置 连接mysql 用户名ffzs 密码666 地址localhost：3306 database：stock
engine = create_engine('mysql+pymysql://debian-sys-maint:123qwe@localhost:3306/stock')
# 建立连接
con = engine.connect()

df = pd.read_csv('/home/user/Desktop/stock.csv', 
            encoding='gbk',
            
            usecols=[0,1,2,3,4,5,6],
            
            )

# pandas类型和sql类型转换
def map_types(df):
    dtypedict = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            dtypedict.update({i: NVARCHAR(length=255)})
        if "float" in str(j):
            dtypedict.update({i: Float(precision=2, asdecimal=True)})
        if "int" in str(j):
            dtypedict.update({i: Integer()})
    return dtypedict

dtypedict = map_types(df)
# 通过dtype设置类型 为dict格式{“col_name”:type}
df.to_sql(name='test2', con=con, if_exists='replace', index=False, dtype=dtypedict)

