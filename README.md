# Unsupervised Audio-to-Audio Translation

**Please note:** This repository is actively being worked on. Throughout the course of working on this repository, we changed how we preprocess the data. Also, there were several bugs that were found in earlier notebooks that have been removed going forward. This is a good moment to refactor the work. You can find old code on the (experiments branch)[https://github.com/earthspecies/unsupervised-audio-translation/tree/experiments].

This is the main repository for the [Implementing and extending unsupervised human-human text/audio translation](https://github.com/orgs/earthspecies/projects/4) project.

How does this fit into the ESP roadmap towards translating animal communication? Unsupervised audio-to-audio translation requires learning how to create useful semantic embeddings directly from audio, which allows for coorelation with other behavioral models or comparison across species.

## Project overview

**Goal: achieving unsupervised audio to audio translation**

1. Build text embeddings and demonstrate translation without rosetta stone
    * Good opportunity to test and demonstrate [embedding alignment](https://arxiv.org/abs/1805.06297) (this technique is what we will want to leverage once we obtain audio embeddings).
    * Findings can lend themselves well to clarifying our approach and also to sharing the efficacy of embeddings with a broader public
2. Implement [Audio Word2Vec](https://arxiv.org/abs/1603.00982) - train acoustic embeddings using a denoising AE architecture
    * Good opportunity to get acquainted with the LibriSpeech dataset
    * These embeddings could lend themselves well to comparison against semantic embeddings
3. [Speech2Vec: A Sequence-to-Sequence Framework for Learning Word Embeddings from Speech](https://arxiv.org/abs/1803.08976) - train semantic embeddings using an RNN encoder-decoder architecture
    * This architecture, or one of similar capability, is one we want to leverage for unsupervised audio to audio translation
4. Reproduce #3 with a transformer architecture (tentative)
    * Transformers offer an ease of training, they can be trained efficiently on vast amounts of data
5. Obtain or [synthesize](https://research.google.com/pubs/archive/42543.pdf) a bilingual dataset of speech, train semantic word embeddings (using #3 or #4) and perform unsupervised translation (using #1).

For an overview of papers and other resources that inspire us and that we feel are instrumental to this work, please take a look at our bookshelf for this project [here](https://github.com/earthspecies/audio_embeddings/blob/master/bookshelf.md).
