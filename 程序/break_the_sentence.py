#!/anacanda/python
# -*- coding: utf-8 -*-

#断句
def break_the_sentence(content):
    # 结束符号，包含中文和英文的
    comment_cut = []
    comment_cut_mumber = 0
    for line in content:
        import re
        pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
        result_list = re.split(pattern, line)
        comment_cut.extend(result_list)
    comment_cut_mumber = len(comment_cut)
    return comment_cut, comment_cut_mumber