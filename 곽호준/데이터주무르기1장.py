import pandas as pd
import numpy as np

local = 'C:/Users/incom/OneDrive/바탕 화면/파이썬COP2/Mission/곽호준/CCTV_in_Seoul.CSV'
local2 = 'C:/Users/incom/OneDrive/바탕 화면/파이썬COP2/Mission/곽호준/population_in_Seoul.xls'

# CCTV_Seoul = pd.read_csv(local, encoding='utf-8')
# print(CCTV_Seoul.head())

# print(CCTV_Seoul.columns)

# CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)

# print(CCTV_Seoul.head())

# pop_seoul = pd.read_excel(local2, encoding='utf-8')
# print(pop_seoul.head())

# pop_seoul = pd.read_excel(local2, header =2, usecols = 'B, D, G, J, N', encoding='utf-8')
# print(pop_seoul.head())

# pop_seoul.rename(columns = {pop_seoul.columns[0] : '구별',
#                            pop_seoul.columns[1] : '인구수',
#                            pop_seoul.columns[2] : '한국인',
#                            pop_seoul.columns[3] : '외국인',
#                            pop_seoul.columns[4] : '고령자'}, inplace=True)

# print(pop_seoul.head())

# s = pd.Series([1,3,5,np.nan,6,8])
# dates = pd.date_range('20200415', periods=6)
# s = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(s)
# print(s.head(3))
# print(s.head())
# print(s.index)
# print(s.columns)
# print(s.values)
# print(s.info())
# print(s.describe())
# print(s.sort_values(by='B', ascending=False))
# print(s['B'])
# print(s[0:3])
# print(s.loc[dates[0]])
# print(s.loc[:,['A','B']])
# print(s.loc[dates[0:1],['A','B']])

# print(s.iloc[:1, :1])
# print(s[s > 0])
