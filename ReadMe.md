# Phonetic Word Similarity

A novel method to compare the phonetic similarity between words based on phonetic features.

- [Phonetic Word Similarity](#phonetic-word-similarity)
  - [Preparing dataset and environment](#preparing-dataset-and-environment)
    - [Download datasets](#download-datasets)
    - [Preparing dataset](#preparing-dataset)
  - [Algorithm results](#algorithm-results)
  - [Train embedding](#train-embedding)
  - [Embedding results](#embedding-results)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

---

## Preparing dataset and environment

### Download datasets

Download [The CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) in the data directory.

```
wget -P data http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b
```

Download SOTA model vocab from [NLP for Hindi git repo](https://github.com/goru001/nlp-for-hindi).

```
wget -O data/hindi_lm_large.vocab https://drive.google.com/uc?export=download&id=1P6r8UBcegvVmr1kBDjqcYppmt_WgnbNt
```

### Preparing dataset

Add missing words to cmu dictionary

```
cat data/cmudict-0.7b res/cmudict_missing_words >> data/cmudict-0.7b-with-vitz-nonce
```

Generate hindi dictionary from LM vocab

```
python src/preprocess/vocab2dict.py res/hindi_phones.csv data/hindi_lm_large.vocab data/dict_hindi
```

---

## Algorithm results

[results_method.ipynb](src/results_method.ipynb) contains results for the algorithm. The result includes:

Comparision between unigram, bigram and bigram with penalty.
![01](docs/img/01_unigram_vs_bigram.png)

How we obtained the penalty of 2.5.
![02](docs/img/02_penalty.png)

Comparision between Vitz method, and the effect of vowel weight.
![03](docs/img/03_vowel_weight.png)

---

## Train embedding

---

## Embedding results

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
