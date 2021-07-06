#!/anacanda/python
# -*- coding: utf-8 -*-
import pandas as pd


def bayesian(data):
    # 读取数据
    df = pd.read_csv('C:/Users/lenovo/Desktop/Professional internship/train.csv')

    comment = df['评语'].values.tolist()  # 转换成list格式

    # 数据预处理
    from data_pre_processing import data_pre_processing
    comments, stopwords, comments_clean, all_words = data_pre_processing(comment)

    # 数据化
    df_train = pd.DataFrame({'comments_clean': comments_clean, 'label': df['种类']})
    df_train.label.unique()
    label_mapping = {"优点": 1, "缺点": 0}
    df_train['label'] = df_train['label'].map(label_mapping)



    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(df_train['comments_clean'].values, df_train['label'].values,random_state=1)
    # 训练集处理
    words = []
    for line_index in range(len(x_train)):
        try:
            words.append(' '.join(x_train[line_index]))
        except:
            print(line_index, word_index)
    # 训练集向量的生成
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer(analyzer='word', max_features=4000, lowercase=False)
    vec.fit(words)
    # 贝叶斯分类器的生成
    from sklearn.naive_bayes import MultinomialNB
    classifier1 = MultinomialNB()
    classifier1.fit(vec.transform(words), y_train)

    test_words = []
    for line_index in range(len(x_test)):
        try:
            test_words.append(' '.join(x_test[line_index]))
        except:
            print(line_index, word_index)
    # 测试集处理1
    #print(classifier1.score(vec.transform(test_words), y_test))

    # from sklearn.feature_extraction.text import TfidfVectorizer
    # vectorizer = TfidfVectorizer(analyzer='word', max_features=4000, lowercase=False)
    # vectorizer.fit(words)
    # from sklearn.naive_bayes import MultinomialNB
    # classifier2 = MultinomialNB()
    # classifier2.fit(vectorizer.transform(words), y_train)
    # # 测试集处理2
    # print(classifier2.score(vectorizer.transform(test_words), y_test))

    # 验证
    try_words = []
    for line_index in range(len(data)):
        try:
            try_words.append(' '.join(data[line_index]))
        except:
            print(line_index, word_index)
    return classifier1.predict(vec.transform(try_words)), len(data)
