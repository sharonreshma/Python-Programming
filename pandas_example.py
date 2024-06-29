import numpy as np
import pandas as p
data=np.array(['a','b','c','d'])
s=p.Series(data)
print(s)

obj=p.Series(['math','sci'],index=[1,2])
print(obj)
print(obj.values)
print(obj.index)


newdf = p.Series([1,2,3,4], index=['A','B','C', 'D'])
print(newdf)
myindex =newdf.index
print(myindex)
print(myindex[2])
newdf = p.Series([1,2,3,4], index=['A','B','C', 'D'])
newdf1 = newdf.reindex(['A','B','C','D','F','E','z'])
print(newdf1)


data = [['Roger',10],['Andy',12],['Rafael',13]]
df = p.DataFrame(data,columns=['Name','Age'])
print(df)

