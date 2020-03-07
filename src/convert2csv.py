import pdftotext

# Load your PDF
with open("100_sentences.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
pages = ''
for page in pdf:
    # Remove page number
    page = page[:-10]
    # Remove all '\n' and extra space
    page = page.replace('\n', '').strip()
    pages += page

print(pages)

import re 
text = re.split('[0-9]+\.', pages)[1:]
print(text)


pairs_list = []
counter = 0
for i in range(len(text)):
    # print(sentence[i])
    if i%2 == 1:
        # pairs_list.append((li[i-1].replace('\n',''),li[i].replace('\n','')))
        pairs_list.append((text[i-1],text[i]))
    counter +=1 

for pair in pairs_list:
    print(pair,'\n')

import pandas as pd 
df = pd.DataFrame(pairs_list,columns=['Front','Back'])

# print(df)
df.to_csv('DataExportToAnki.csv', encoding='utf-8')
# It's not elegant I knew, but it worked for me.
