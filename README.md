# Bi-Lingual Named Entity Recognition Using XLM-R and Language Features
This repository contains the official implementation code of the paper [Bi-Lingual Named Entity Recognition Using XLM-R and Language Features](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11113333), accepted at KCC 2022.

## Data
Check the datasets. Training sets of English and Korean can be found in [this link](https://aclanthology.org/2022.semeval-1.196.pdf).

## Setting up the code environment
```
$ pip install -r requirements.txt
```
## Running
Train a XLM-RoBERTa base model

```
python -m ner_baseline.train_model --train train.txt --dev dev.txt --out_dir . --model_name xlmr_ner --gpus 1 \
                                   --epochs 2 --encoder_model xlm-roberta-base --batch_size 64 --lr 0.0001
```
Evaluate the trained model
```
python -m ner_baseline.evaluate --test test.txt --out_dir . --gpus 1 --encoder_model xlm-roberta-base \
                                --model MODEL_FILE_PATH --prefix xlmr_ner_results

```

## Contact
Should you have any questions, feel free to contact [fomet1277@naver.com](fomet1277@naver.com).

# License 
The code under this repository is licensed under the [Apache 2.0 License](https://github.com/amzn/multiconer-baseline/blob/main/LICENSE).
