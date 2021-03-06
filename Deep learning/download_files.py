import requests, json
from pandas.io.json import json_normalize
import pandas as pd
import wget
import os
import gzip


if os.path.exists('./files'):
    os.chdir('./files')
else:
    os.mkdir('./files')
    os.chdir('./files')

# Get the project as a json and dump it into a dataframe:
response = requests.get('https://www.ebi.ac.uk/pride/ws/archive/file/list/project/PXD010000')
response = json.loads(response.text)
df = pd.DataFrame(json_normalize(response['list']))

# get only .mzid and .mzML files
filtered = df.loc[df.fileName.str.contains('.mzid|.mzML')]
dls = filtered.downloadLink

# sort, such that .mzid + .mzML come in pairs according to the same sample.
sorted_index = filtered.fileName
sorted_index = sorted_index.sort_values()
dls = dls.loc[sorted_index.index]

# Download files:
list(map(lambda x: wget.download(x),dls))

# Unzip, in case files are zipped 
os.system('gunzip *.gz')

