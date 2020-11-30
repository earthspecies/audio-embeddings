import os
import pandas as pd
import spacy

def get_alignment_filenames(path_to_alignments_folder):
    '''Get all file names in the annotated word alignments'''
    root_path = 'data/LibriSpeech-Alignments/LibriSpeech_Text_Alignments/'
    folders = ['dev-clean', 'dev-other', 'test-clean', 'test-other', 'train-clean-100', 'train-clean-360', 'train-other-500']
    filenames = dict()
    for folder in folders:
        grab_files = []
        for path, subdirs, files in os.walk(root_path + folder):
            for name in files:
                grab_files.append(os.path.join(path, name))
        filenames[folder] = grab_files
    return filenames # Returns a dictionarty with {subfolder_name:[filenames_in_subfolder]}

def get_text_from_files(filenames_dict):
    '''Will create a dataframe per folder, with all the text combined as the column
    Questions:
    Do we need to keep silence?
    '''
    all_folders_df = pd.DataFrame()
    for folder, filenames in filenames_dict.items():
        folder_df = pd.DataFrame()
        for filename in filenames:
            if filename[-3:] == 'txt':
                file_text = extract_text_single_file(filename)
                folder_text = {'Folder':[folder], 'Filename':[filename], 'Text':[file_text]}
                text_df = pd.DataFrame(folder_text)
                folder_df = folder_df.append(text_df)
        all_folders_df = all_folders_df.append(folder_df)
    return all_folders_df

def extract_text_single_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read().splitlines()
    all_text = ''
    for line in content:
        text = line.split()[1].split(',')
        text = [word for word in text if word.isalnum()]
        all_text += ' '.join(text) + ' '
    return all_text

def main():
    filenames_dict = get_alignment_filenames('data/LibriSpeech-Alignments/LibriSpeech_Text_Alignments')
    df = get_text_from_files(filenames_dict)
    return df

class TextPreprocess():
    def __init__(self):
        self.nlp = spacy.load('en')

    def lemmatize(self, text_chunk):
        text_model = self.nlp(text_chunk)
        new_chunk = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text_model])
        return new_chunk

    def remove_stopwords(self, text_chunk):
        text_model = self.nlp(text_chunk)
        new_chunk = ' '.join([word.text for word in text_model if not word.is_stop ])
        return new_chunk

if __name__ == "__main__":
    main()