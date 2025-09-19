import os
REPO = "content/drive/MyDrive/00-github/sentence-embedding-sensitivity"
DATA = os.path.join(REPO,"Data")
DATASETS = os.path.join(DATA,"datasets")
SICK_DATA = os.path.join(DATA,"sick_dataset")
SR_DATA = os.path.join(DATA,"sr_dataset")
VISLA_DATA = os.path.join(DATA,"VISLA")

model_dict = {
    "par_dis_roberta": "paraphrase-distilroberta-base-v1",
    "roberta_base_v3": "msmarco-roberta-base-v3",
    "par_mpnet": "paraphrase-mpnet-base-v2",
    "par_xlm_r": "paraphrase-xlm-r-multilingual-v1",
    "labse": "LaBSE",
    "e5_base": "intfloat/e5-base-v2",
    "gte_base": "thenlper/gte-base",
    "bge_base_v15": "BAAI/bge-base-en-v1.5"
}

benchmark_datasets = {
    "MRPC": ("glue", "mrpc"),
    "QQP": ("glue", "qqp"),
    "PAWS": ("paws", "labeled_final"),
    "STS-B": ("glue", "stsb"),
    "SICK": f"{SICK_DATA}",
    "SR": f"{SR_DATA}"
}

