# -*- coding: utf-8 -*-
"""
Created on Wed May 02 18:00:33 2018
@author: sky
"""
"""
题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。每段的绳子的长度记为
k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘积是多少？例如当绳子的长度是8时，我们把它
剪成长度分别为2、3、3的三段，此时得到最大的乘积18。
时间复杂度：O(n)
类型：动态规划
"""

"""
总结：
动态规划四个特点：
1. 求一个问题的最优解
2. 整个问题的最优解是依赖各个子问题的最优解
3. 把大问题分解成若干个小问题，这些小问题之间还有相互重叠的更小的子问题
4. 从上往下分析问题，从下往上求解问题
从剪绳子问题出发，首先他要求解剪出每段绳子的最大乘积，即求最优解；
求一段绳子剪完最大乘积，每剪一刀，得出来的结果最优解依赖于剪出来的绳子的最优解，以此递推；
对剪出来的绳子（子问题）求解时，还能再分解；
从上往下分析：先定义函数f(n)为把长度为n的绳子剪成若干段乘积最大值，当剪一刀时，有n-1种选择(1,2,...n-1)因此f(n)=max{f(i)*f(n-i)}(0<i<n)
从下往上求解：上式是一个从上往下递归公式，会有大量重复子问题的计算，所以更好的方法是从下往上计算，先得到f(2),f(3)，再根据f(2),f(3)得到f(4)...
"""

def maxProductAfterCutting(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    #创建一个长度为length的空数组来保存子问题最优解
    dp = [None for i in range(length+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    max_length = 0
    for i in range(4, length+1):
        for j in range(1, i//2+1):
            temp = dp[j] * dp[i-j]
            if temp > max_length:
                max_length = temp
        dp[i] = max_length
    return dp[length]
