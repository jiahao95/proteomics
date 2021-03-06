# KNN similary Search

## Step 6 : Unique peptide list
Retrieve the list of unique peptides from the [small.fasta](https://owncloud.hpi.de/s/fa0aV3lp4Mu8Upq)
```
python filtered_unique_peptides.py
```

## Step 7 : spectra embeddings
the following python script generates the spectra embeddings for the knn search (spectra downloaded and prepared in step 5), the model is stored in this [folder](https://github.com/jiahao95/project_lab-ss2020/tree/master/Deep%20learning/_model_relu_32)
```
python spectra_embedder.py
```

## Step 8 : Peptide embeddings
run following script to create the peptide embeddings as database for the knn similarity search, model stored in this [folder](https://github.com/jiahao95/project_lab-ss2020/tree/master/Deep%20learning/_model_relu_32)
```
python sequence_embedder.py
```

## Step 9 : Knn similarity search
```
python faiss_unique_indexing_k50.py
```
This returns a csv file with identified peptides, thus, it can be compared with the output from the X!Tandem.
