import numpy as np

class Embeddings():
    def __init__(self, embeddings, index2word):
        '''embeddings - numpy array of embeddings, index2word - list of words corresponding to embeddings'''
        assert len(embeddings) == len(index2word)
        self.vectors = embeddings
        self.i2w = index2word
        self.w2i = {w:i for i, w in enumerate(index2word)}

    def analogy(self, a, b, c, n=5, discard_question_words=True):
        '''
        a is to b as c is to ?

        Performs the following algebraic calculation: result = emb_a - emb_b + emb_c
        Looks up n closest words to result.

        Implements the embedding space math behind the famous word2vec example:
        king - man + woman = queen
        '''
        question_word_indices = [self.w2i[word] for word in [a, b, c]]
        a, b, c = [self.vectors[idx] for idx in question_word_indices]
        result = a - b + c

        if discard_question_words: return self.nn_words_to(result, question_word_indices, n)
        else:                      return self.nn_words_to(result, n=n)

    def nn_words_to(self, vector, skip_indices=[], n=5):
        nn_indices = self.word_idxs_ranked_by_cosine_similarity_to(vector)
        nn_words = []
        for idx in nn_indices:
            if idx in skip_indices: continue
            nn_words.append(self.i2w[idx])
            if len(nn_words) == n: break

        return nn_words

    def word_idxs_ranked_by_cosine_similarity_to(self, vector):
        return np.flip(
            np.argsort(self.vectors @ vector / (self.vectors_lengths() * np.linalg.norm(vector, axis=-1)))
        )

    def vectors_lengths(self):
        if not hasattr(self, 'vectors_length_cache'):
            self.vectors_length_cache = np.linalg.norm(self.vectors, axis=-1)
        return self.vectors_length_cache

    def __getitem__(self, word):
        return self.vectors[self.w2i[word]]

    @classmethod
    def from_txt_file(cls, path_to_txt_file, limit=None):
        '''create embeddings from word2vec embeddings text file'''
        index, vectors = [], []
        with open(path_to_txt_file) as f:
            f.readline() # discarding the header line
            for line in f:
                try:
                    embedding = np.array([float(s) for s in line.split()[1:]])
                    if embedding.shape[0] != 300: continue
                    vectors.append(embedding)
                    index.append(line.split()[0])
                except ValueError: pass # we may have encountered a 2 word embedding, for instance 'New York' or 'w dolinie'
                if limit is not None and len(vectors) == limit: break
        return cls(np.stack(vectors), index)
