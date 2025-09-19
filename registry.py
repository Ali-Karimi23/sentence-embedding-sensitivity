model_dict = {
    "paraphrase_distilroberta": "paraphrase-distilroberta-base-v1",
    "msmarco_roberta_base_v3": "msmarco-roberta-base-v3",
    "paraphrase_mpnet": "paraphrase-mpnet-base-v2",
    "paraphrase_xlm_r": "paraphrase-xlm-r-multilingual-v1",
    "labse": "LaBSE",
    "e5_base": "intfloat/e5-base-v2",
    "gte_base": "thenlper/gte-base",
    "bge_base_v15": "BAAI/bge-base-en-v1.5"
}

binary_datasets = {
    "MRPC": ("glue", "mrpc"),
    "QQP": ("glue", "qqp"),
    "PAWS": ("paws", "labeled_final"),
}

five_class_datasets = {
    "STS-B": ("glue", "stsb"),
    "SICK": ("sick", None),
}
