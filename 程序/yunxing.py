#!/anacanda/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy
from bayesian import bayesian
from break_the_sentence import break_the_sentence
from data_pre_processing import data_pre_processing
from bayesian import bayesian


class yunxing_Model:
    def __init__(self, filePath):
        self.data = 0
        self.d = 0
        self.filePath = filePath

    def yunxing(self):
        df = pd.read_csv(self.filePath)
        comment = df['评价'].values.tolist()
        comment_cut, comment_cut_mumber = break_the_sentence(comment)
        comments, stopwords, comments_clean, all_words = data_pre_processing(comment_cut)
        result,long = bayesian(comments_clean)
        return  comments_clean, comment_cut, all_words, comment_cut_mumber, result, long

    def plot(self, all_words):
        df_all_words = pd.DataFrame({'all_words': all_words})
        words_count = df_all_words.groupby(by=['all_words'])['all_words'].agg({"count": numpy.size})
        words_count = words_count.reset_index().sort_values(by=["count"], ascending=False)

        from wordcloud import WordCloud
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

        wordcloud = WordCloud(font_path="./data/simhei.ttf", background_color="white", max_font_size=80)
        word_frequence = {x[0]: x[1] for x in words_count.head(100).values}
        wordcloud = wordcloud.fit_words(word_frequence)
        plt.imshow(wordcloud)


if __name__ == "__main__":
    path = 'C:/Users/lenovo/Desktop/Professional internship/test.csv'
    model = yunxing_Model(path)
    comments_clean, comment_cut, all_words, comment_cut_mumber, result, long = model.yunxing()
    model.plot(all_words)