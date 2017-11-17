import pickle
import pandas as pd

category = "trade"
path = category+"_clustering/"
ind_file = "june_inds_all.pkl"
output_file_name = path+"june_inds_"+category
in_file = path+"June_"+category+".xlsx"

pkl_file = open(ind_file, "rb")
inds = pickle.load(pkl_file)
pkl_file.close()

xl_file = pd.ExcelFile(in_file)
ds = xl_file.parse("Лист1")
id_list = ds.IND_ID.tolist()

output = []
i = 1
for ind in inds:
    if ind[0] in id_list:
        output.append(ind)
        print(i)
        i += 1

output_file = open(output_file_name+".pkl", "wb")
pickle.dump(output, output_file)
output_file.close()
