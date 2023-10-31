#%%
#* Importing packages

import pandas as pd
from pathlib import Path 
import os

#%%
#* Specifying path 

directory_path = Path('..') # goes back to the previous folder
print(os.listdir(directory_path))

TSPpath = (
    directory_path
    /'data'
    /'raw'
    /'TSP_raw_data'
    /'CLRTAP.csv'
)

#%%
#* Import the full CLRTAP data as pandas.DataFrame and explore the data
Rawdata_df=pd.read_table(TSPpath)

Rawdata_df.head()

#TODO Try to explore more the dataset and see some interesting functions such as shape...
# %%
#* Filtering the air pollutants dataset to the one that is your own project topic
TSP_data=Rawdata_df[Rawdata_df["Pollutant_name"]=="TSP"]
TSP_data.head()
#TODO before to export the file should be great to explore the dataset and clean it










#%%
#* 
#Processed_data_path = (directory_path
#                       /'data'
#                      /'processed')
#TSP_data.to_csv(f"{Processed_data_path}\\TSP_data.csv", index=False, sep=',')

