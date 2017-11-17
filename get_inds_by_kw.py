import pickle
import numpy as np
import pandas as pd
import nltk
from nltk.util import ngrams

path = "poverty_clustering/"
ind_file = "june_inds_all.pkl"
output_file_name = path+"june_inds_poverty_by_kw"

pkl_file = open(ind_file, "rb")
inds = pickle.load(pkl_file)
pkl_file.close()

keywords = [
    ["малоимущий_ADJ", "попечение_NOUN", "прожиточный_ADJ", "безработица_NOUN", "малообеспеченный_ADJ"],
    ["денежный_ADJ помощь_NOUN", "материальный_ADJ помощь_NOUN"],
    []
    ]

exclude = [
    [],
    []
    ]

output = []

for ind in inds:
    if len(ind[2]) > 0:
        bigrm = list(nltk.bigrams(ind[2]))
        bigrm = [" ".join(b) for b in bigrm]
        #trigram = ngrams(ind[2], 3)
        #trigram = [" ".join(t) for t in trigram]
        if ( 
            (
                any(word in ind[2] for word in keywords[0])
                or any(b in bigrm for b in keywords[1])
                #or any(t in trigram for t in keywords[2])
            )
            #and not any(word in ind[2] for word in exclude[0])
            #and not any(b in bigrm for b in exclude[1])
            ):
            output.append(ind)
print(len(output))
output_file = open(output_file_name+".pkl", "wb")
pickle.dump(output, output_file)
output_file.close()

df = pd.DataFrame(output)
df.to_csv(output_file_name+".csv", index=False, header=True, encoding = "utf-8")    

