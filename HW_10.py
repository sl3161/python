import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data.whoAmI =='robot',['Robot']]= 1
data.loc[data.whoAmI !='robot',['Robot']]= 0
data.loc[data.whoAmI =='human',['Human']]= 1
data.loc[data.whoAmI !='human',['Human']]= 0
print (data[['Robot','Human']])