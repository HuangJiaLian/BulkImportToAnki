import re
with open('7000_sentences_bak.txt','r') as myfile:
    data = myfile.read()

print(data)
li = re.split('[0-9]+\.',data)[1:]
counter = 1

# c = 0
# for a in li:
#     c = c+1
#     print(c, '\n')
#     print(a)


pairs_list = []
for i in range(len(li)):
    # print(sentence[i])
    if i%2 == 1:
        # pairs_list.append((li[i-1].replace('\n',''),li[i].replace('\n','')))
        pairs_list.append((li[i-1],li[i]))
    counter +=1 
# print(li)

# print(pairs_list)
for pair in pairs_list:
    print(pair,'\n')


# print(pair[0])
# make CSV file 
import numpy as np 
import pandas as pd 
df = pd.DataFrame(pairs_list,columns=['Front','Back'])
# print(df)
df.to_csv('DataFrame.csv', encoding='utf-8')


