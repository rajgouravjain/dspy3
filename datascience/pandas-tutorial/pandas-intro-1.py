import pandas as pd
import numpy as np

### From numpy ndarray
df1 = pd.DataFrame(np.random.rand(3,5),columns= ["c1","c2","c3","c4","c5"])
print df1

#Method 2 (Most frequently use case)
s1 = pd.Series(["mango", "apple","banana","orange"])
s2 = pd.Series(np.random.randn(4))
df2 = pd.DataFrame(data=[s1,s2], index=["s1", "s2"]).transpose()
print df2

##Method 3
df3 = pd.DataFrame(data={"C1": range(10), "C2" : range(5,15) })
print df3

##Method4
whether_data = [("Rainy",32),("Snow",26),("Windy",28)]
df4 = pd.DataFrame(data=whether_data, columns=["Event", "Temprature"])
print df4

##Method 5
whether_data = [{"Event": "Rainy", "Temprature": 29},{"Event": "Snow", "Temprature": 25}, {"Event": "Sunny", "Temprature": 32}]
df5 = pd.DataFrame(data=whether_data)
print df5

### Method 6 (Rare case)
list_of_series = [pd.Series([1,2,3],index=['a','b','c']), pd.Series([3,4,6],index=['a','c','d'])]
df6 = pd.concat(list_of_series, axis=1).transpose()
print df6

print df6.ix[:,["a","b","c","d"]]


## Method 7
##Using CSV

# Method 8
#Using Excel