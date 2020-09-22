import os
import numpy as np
import pandas as pd
import seaborn as sns
from similarity import Similarity


class Experiment:
    def __init__(self, mapping, dictionary, encoding, words):
        self.filepath = os.path.dirname(__file__)
        mapping = os.path.join(self.filepath, '..', 'res', mapping)
        dictionary = os.path.join(self.filepath, '..', 'data', dictionary)
        self.wsim = Similarity(mapping, dictionary, encoding=encoding)
        self.words = words


    def get_dataset(self):
        self.dataset = pd.concat([self.load_dataset(w) for w in self.words], ignore_index=True)
        # change the scale of Vitz score from 0-1 to 1-0
        self.dataset['vw_predicted'] = 1 - self.dataset['vw_predicted']
        return self.dataset


    def load_dataset(self, word):
        df = pd.read_csv(os.path.join(self.filepath, '..', 'res', f'vitz-1973-experiment-{word}.csv'))
        df['actual'] = word
        df['unigram'] = df.apply(
            lambda row: self.wsim.word_similarity(
                row.word.upper(), word.upper(), bigram=False, vowel=False, penalty=1), axis=1)
        df['bigram'] = df.apply(
            lambda row: self.wsim.word_similarity(
                row.word.upper(), word.upper(), bigram=True, vowel=False, penalty=1), axis=1)
        df['bigram p=2.5'] = df.apply(
            lambda row: self.wsim.word_similarity(
                row.word.upper(), word.upper(), bigram=True, vowel=False, penalty=2.5), axis=1)
        df['bigram p=2.5 VW'] = df.apply(
            lambda row: self.wsim.word_similarity(
                row.word.upper(), word.upper(), bigram=True, vowel=True, penalty=2.5), axis=1)
        return df


    def penalty_analysis(self, words, start, end, divisions, bigram=True, vowel=True):
        columns, indices = {}, np.linspace(start, end, num=divisions)
        avg = np.zeros(len(indices))
        for word in words:
            df = pd.read_csv(os.path.join(self.filepath, '..', 'res', f'vitz-1973-experiment-{word}.csv'))
            values = []
            for penalty in indices:
                obtained = df['obtained'].to_numpy()
                actual = np.array([
                    self.wsim.word_similarity(
                        word.upper(), other.upper(), bigram=bigram, vowel=vowel, penalty=penalty
                    ) for other in df['word'].tolist()
                ])
                values.append(np.corrcoef(obtained, actual)[0, 1])
            columns[word] = values
            avg += np.array(values)
        columns['avg'] = avg / len(words)
        return pd.DataFrame(columns, index=indices)