#create a class to encapsulate all the cleaning functions

class Summarizer:
    '''
    This class contains functions to clean the input data provided (ideally a text file)
    '''
    
    
    def __init__(self, text):
        '''
        This is the init constructor function that will initialize the input text data to that particular
        instance of the class.
        
        args:
        
        text = the input string data.
        '''
        
        self.text = text
        
        
    def punctuation_removal(self, sentences):
        '''
        Function to remove punctuation and special characters from the raw data.
        '''
        
        import pandas as pd
        clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
        return clean_sentences
        
        
        
#     def stopword_removal(self, text):
#         '''
#         Function to remove stopwords from the input raw data.
#         '''
        
#         print('able to access stopword_removal function and run it')
        
        
    def tokenize_sentences(self, text):
        '''
        Function to tokenize the given paragraph to sentences.
        '''
        
        from nltk.tokenize import sent_tokenize
        sentences = []
        for s in text:
            sentences.append(sent_tokenize(s))

        sentences = [y for x in sentences for y in x]
        return sentences
        
        
    def extract_feature(self, clean_sentences):
        from sklearn.feature_extraction.text import TfidfVectorizer
        tf_idf_vec = TfidfVectorizer(use_idf=True, 
                        smooth_idf=False,  
                        ngram_range=(1,1),stop_words='english')
        tf_idf_matrix = tf_idf_vec.fit_transform(clean_sentences)
        return tf_idf_matrix

        
    
    
    def cosine_similarity(self, tf_idf_matrix):
        

    
    def page_ranking(self, similarity_matrix):
        print('able to access page_ranking function and run it')
        
        
    def show_summary(self, ranked_sentences):
         print('able to access show_summary function and run it')
        
        
    def run_summarizer(self, text):
        self.tokenize_sentences(text)
        self.punctuation_removal(text)
        self.extract_feature(text)
        self.cosine_similarity(text)
        #self.page_ranking(similarity_matrix)
        #self.show_summary(ranked_sentences)
        print('All functions run finished!')