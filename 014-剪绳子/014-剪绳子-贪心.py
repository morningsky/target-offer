# -*- coding: utf-8 -*-
"""
Created on Thu May 03 10:47:29 2018

@author: sky
"""

"""
用贪婪算法实现剪绳子问题
"""
"""
用贪婪算法时，每一步都可以做出一个贪婪选择，基于这个选择，我们能确定的到最优解？同时需要用数学证明这个贪婪选择是对的。
当n>=5时，可证2(n-2)>n且3(n-3)>n，就是说当绳子长度大于等于5时可以切成2或3。另外当n>=5时，3(n-3)>=2(n-2)，因此要竟可能剪出长度为3的段。
当长度为4时2*2>1*3，所以要切成2*2的段
"""

def maxProductAfterCutting(length):
    if length <=1 :
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    #尽可能的分成长度为3的段
    timeOf3 = length // 3 #地板除 保留整数
    #当最后长度为4的时候不能再分车3+1，而是分成2+2
    if length - timeOf3*3 == 1:
        timeOf3 -= 1
    timeOf2 = (length - timeOf3 * 3) // 2
    return (2**timeOf2) * (3**timeOf3)
          
              
    