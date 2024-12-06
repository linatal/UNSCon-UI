# UNSC Conflicts Corpus Demo 


![](UNSCon_DemoUI.gif)

This This app visualizes the our **UN Security Council's Conflicts Corpus (UNSCon)** based on 86 speeches annotated with Conflict annotations.
For more information on the corpus, see our [paper](https://aclanthology.org/2024.lrec-main.716/) and [github repo](https://github.com/linatal/UNSCon).
We build the app using [Streamlit](https://streamlit.io/). We mapped the original more fine-grained annotations to sentence-span annoations to enable better overview.



### Run the demo
To run the demo download the requirements typing in your terminal:  
``pip -r requirements.txt``

Then run the app: ``streamlit run ./app.py``

We tested the demo on python 3.12.4.

### Preprocess conflict annotations file
We preprocessed the original UNSCon dataset from ``data/main_conflicts_sents.csv`` and add some metadata from the ``data/speaker.csv`` file from the [UN Security Council Debates](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KGVSYH) corpus by Schönfeld et al. 2019 ([paper](https://arxiv.org/abs/1906.10969)). 
The preprocessing skript is in ``preprocessing_csv.py``. The output file used for the visualizations is 
