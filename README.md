# The Best of Both Worlds: Retrieval Augmented Generation for Robust Summarisation of Dialogue

This project investigates the lack of generalisation abilities of trained models for query-based summarisation and compares different retrieval paradigms through the lenses of a new test set in the Financial domain. 
The aim is to answer the following research question:

*What is the best combination of efficient trained models with expensive but
performant LLMs for robust query-based meeting summarisation?*

## Repository structure

Here we provide a breakdown of the folders in this repo, and what they each contain:

- ```‎data processing```‎: contains the scripts used to convert the Aveni test set to the format used in the QMSum dataset and to get statistics about the data structure.
- ```‎Data```‎: contains .txt file with output from the DYLE model (used in ```DYLE+GPT``` model). Aveni dataset removed from public version.
- ```‎LangChain+GPT```‎: contains the Python notebooks to run and evaluate the ```‎LangChain+GPT``` model with the Aveni dataset or with the Product dataset from QMSum.
- ```‎GPT end-to-end```‎: contains the Python notebooks to run and evaluate the ```‎GPT end-to-end``` model configuration with the Aveni dataset or with the Product dataset from QMSum.
- ```‎DYLE```‎: contains the code to train and test ```‎DYLE```‎ with Aveni or QMSum data in in-domain ad out-of-domain settings.
- ```‎DYLE+GPT```‎: contains the Python notebooks to run and evaluate the ```‎DYLE+GPT``` model with the Aveni dataset or with the Product dataset from QMSum.
- The script ```‎human_eval_plots.py``` provides the code used to generate plots with the results from the human evaluation of the summaries.‎
  
## Data and DYLE checkpoints

The QMSum dataset, with the added extractive oracle files generated through DYLE, and some model checkpoints for DYLE can be found at the following link:

https://uoe-my.sharepoint.com/:f:/g/personal/s2087805_ed_ac_uk/Em-fv8NK2ZpHp5PG2QORViYBPVM2lr2hYwAXltpP4ZzZBA?e=S40eTC

To run DYLE using these files, place the ```QMSum``` folder inside ```DYLE/data``` and the ```saved_model``` folder inside ```DYLE/outputs```.
To run the other models using the Product dataset or any of the data in ```QMSum```, place the folder inside ```Data```.

## Changes to DYLE model

To use DYLE for our experiments, these are the scripts that we added:

- The ```dataloaders```:
  -  ```aveni.py```,
  -  ```academic.py```,
  - ```product.py```,
  - ```committee.py```.
- The ```oracle``` files:
  - ```aveni_oracle.py```,
  - ```create_aveni_jsonl.py```,
  - ```academic_oracle.py```,
  - ```create_academic_jsonl.py```,
  - ```product_oracle.py```,
  - ```create_product_jsonl.py```,
  - ```committee_oracle.py```,
  - ```create_committee_jsonl.py```.

These are the scripts that we modified:

- ```Experiment.py```
- ```config.py```

### Resources

QMSum dataset (Zhong et al. 2021): https://github.com/Yale-LILY/QMSum

DYLE model (Mao et al. 2022): https://github.com/Yale-LILY/DYLE
