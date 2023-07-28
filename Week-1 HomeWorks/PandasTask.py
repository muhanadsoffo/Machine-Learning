import numpy as np
import pandas as pd


columns_name=['Joe','Moneca','Tahani','Jason']
data_values=np.random.randint(low=0, high=101, size=(3, 4))
Mydata=pd.DataFrame(data=data_values, columns=columns_name)
print(Mydata)


print(Mydata['Joe'][2])


Mydata['Ali']=Mydata['Tahani']+Mydata['Jason']
print(Mydata)