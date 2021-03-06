# 面试题15：二进制中1的个数
# 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。
# 例如，把9表示成二进制是1001，有2位是1。因此，如果输入9，则该函数
# 输出2。
# a = 0011 1100

# b = 0000 1101
# &	
# 按位与运算符：
# 参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	
# (a & b) 输出结果 12 ，二进制解释： 0000 1100

# |	
# 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	
# (a | b) 输出结果 61 ，二进制解释： 0011 1101

# ^	
# 按位异或运算符：当两对应的二进位相异时，结果为1 	
# (a ^ b) 输出结果 49 ，二进制解释： 0011 0001

# ~	
# 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。
# ~x 类似于 -x-1	(~a ) 输出结果 -61 ，
# 二进制解释： 1100 0011，在一个有符号二进制数的补码形式。

# <<	
# 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	
# a << 2 输出结果 240 ，二进制解释： 1111 0000

# >>	
# 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数 	
# a >> 2 输出结果 15 ，二进制解释： 0000 1111

# 思路，不断右移数字，与1做与运算来判断最后一位是不是1
# 整数右移一位和除以2在数学上是等价的，可以用除法吗？答案是否：因为除法效率比与运算低太多了

# 有问题的解法：（这样出现负数会进入死循环）
# def numberof1(n):
#     count = 0
#     while(n):
#         if (n&1):  # 与运算，判断最后一位是不是1
#             count +=1
#         n = n >> 1 # 右移运算符

#     return count

# print(numberof1(60))


# 常规解法
# 首先把N和1做与运算，判断n的最低位是不是1。接着把1左移，再和n做与运算，就能判断n的
# 次低位是不是。这样反复左移即可

def numberof1(n):
    count = 0
    flag =  1
    for _ in range(len(bin(n)[2:])):
        if n & flag:  #判断低位是不是为1
            count +=1
        flag = flag << 1 # 左移 1的位置不断向左移动
    return count

print(numberof1(9))


# 牛逼算法
# 如果我们把一个数减去1。如果这个整数不等于0，那么该整数的二进制表示中至少有一位是1。
# 先假设最右边一位是1，减1后，最后一位变成0，而其他所有位保持不变。
# 如果最后一位不是1而是0。如果该整数的二进制表示中最右边的1位于第m位，那么减去1时
# 第m位由1变成0，而第m位之后所有0变成1，整数中第m位之前的所有位数都保持不变。
# 接下来我们把一个整数和它减去1的结果做位与运算。相当于把它最右边的1变成0

# 人话：就是不断把最右为变成0，然后不断+1。
def count_one(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count


if __name__ == "__main__":
    print(count_one(n=10))