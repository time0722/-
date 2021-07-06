#!/anacanda/python
# -*- coding: utf-8 -*-

#数据预处理（分词、删除停用词）
def data_pre_processing(comment):
    import jieba
    import pandas as pd
    comment_S = []
    for line in comment:
        current_segment = jieba.lcut(line)
        if len(current_segment) > 1 and current_segment != '\r\n':
            comment_S.append(current_segment)
    df_comment = pd.DataFrame({'comment_S': comment_S})

    # 删除停用词
    stopwords = pd.read_csv('C:/Users/lenovo/Desktop/Professional internship/stopwords.txt', index_col=False, sep="\t",
                            quoting=3, names=['stopword'], encoding='utf-8')

    def drop_stopwords(comments, stopwords):
        comments_clean = []
        all_words = []
        for line in comments:
            line_clean = []
            for word in line:
                if word in stopwords:
                    continue
                line_clean.append(word)
                all_words.append(str(word))
            comments_clean.append(line_clean)
        return comments_clean, all_words

    comments = df_comment.comment_S.values.tolist()
    stopwords = stopwords.stopword.values.tolist()
    comments_clean, all_words = drop_stopwords(comments, stopwords)
    return comments, stopwords, comments_clean, all_words