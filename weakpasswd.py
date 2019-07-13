# /usr/bin/env python3
# -*-coding:utf8-*-
# author: Sexisnull
# explain: 根据常见词及常用后缀组合生成密码
#   common_suffix：常见后缀列表，可自行扩展
#   common_conjunction：常见连接符
#   word1和word2：输入要生成的相关信息

common_suffix = ['@123', '@123456', '@12345678', '@123456789', '@1234567890', '@0.123', '@0.123456', '@0.123456789',
                 '.123', '.123456', '.123456789',
                 '1', '111', '123456', '123456789', '666', '888',
                 '!', '!@#', '!@#$%^', '!@#$',
                 'qwer', 'qwerty']

common_conjunction = ['@', '.', '!']

input_word1 = ['zhangsan']
input_word2 = ['github.com']

# 首字母大写转换

def str_capitalize(word):
    n_word = []
    for w in word:
        w = w.lower()
        n_word.append(w)
        w = w.capitalize()
        n_word.append(w)

    return n_word

# 排列组合

def str_Permutation(nword1,nword2):
    # 2字符中间添加连接符随意组合
    one_group = []
    for c in common_conjunction:
        for n1 in nword1:
            for n2 in nword2:
                one_group.append(n1+c+n2)
                one_group.append(n2+c+n1)

    # 单字符添加后缀
    two_group = []
    for n1 in nword1:
        for s in common_suffix:
            two_group.append(n1+s)
    for n2 in nword2:
        for s in common_suffix:
            two_group.append(n2+s)

    # 随机组合加后缀
    three_group = []
    for i in one_group:
        for s in common_suffix:
            three_group.append(i+s)

    return one_group+two_group+three_group


if __name__ == '__main__':
    n1 = str_capitalize(input_word1)
    n2 = str_capitalize(input_word2)
    weak_list = str_Permutation(n1,n2)
    with open('weakpasswd.txt','w', encoding='utf-8') as f:
        for i in weak_list:
            f.write(i)
            f.write('\n')