'''
题目: 输入IP地址和子网掩码，判断其是否合法，并输出所属类别
'''
'''
A类地址1.0.0.0~126.255.255.255;
B类地址128.0.0.0~191.255.255.255;
C类地址192.0.0.0~223.255.255.255;
D类地址224.0.0.0~239.255.255.255;
E类地址240.0.0.0~255.255.255.255

私网IP范围是:
10.0.0.0～10.255.255.255
172.16.0.0～172.31.255.255
192.168.0.0～192.168.255.255

子网掩码为二进制下前面是连续的1，然后全是0
例如: 255.255.255.32 就是一个非法的掩码 (全是1)
注意二进制下全是 1 或者全是 0 均为非法
'''


import re

# 判断是否是合法的 IP 地址
def isLegalIP(IP):
    if not IP or IP == "":
        return False

    # 正则表达式判断 IP 地址
    pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    match = pattern.match(IP)
    if not match:
        return False

    nums = IP.split(".")
    for num in nums:
        n = int(num)
        if n < 0 or n > 255:
            return False

    return True


# 判断 IP 地址属于哪一类
def CatagoryIP(IP):
    if not IP or IP == "":
        return False
    nums = IP.split(".")
    # A
    if 126 >= int(nums[0]) >= 1:
        return "A"
    # B
    if 191 >= int(nums[0]) >= 128:
        return "B"
    # C
    if 223 >= int(nums[0]) >= 192:
        return "C"
    # D
    if 239 >= int(nums[0]) >= 224:
        return "D"
    # E
    if 255 >= int(nums[0]) >= 240:
        return "E"

    return False


# 判断是否是 私有IP
def isPrivateIP(IP):
    if not IP or IP == "":
        return False

    nums = IP.split(".")
    if int(nums[0]) == 10:
        return True
    if int(nums[0]) == 172:
        if 31 >= int(nums[1]) >= 16:
            return True
    if int(nums[0]) == 192 and int(nums[1]) == 168:
        return True

    return False


# 判断是否是合法的 子网掩码
def isLegalMaskCode(Mask):
    if not Mask or Mask == "":
        return False
    if not isLegalIP(Mask):
        return False
    # 聪明，一行代码将 四段二进制(8位) 拼接在一起
    # zfill() 函数返回指定长度的字符串，原字符串右对齐，前面填充0
    binaryMask = "".join(map(lambda x: bin(int(x))[2:].zfill(8), Mask.split(".")))
    # 通过指针判断 子网掩码 是否合法
    indexOfFirstZero = binaryMask.find("0")
    indexOfLastOne = binaryMask.rfind("1")
    if indexOfLastOne > indexOfFirstZero:
        return False
    return True


# 输入 IP 地址 和 子网掩码
A, B, C, D, E, Err, P = [0, 0, 0, 0, 0, 0, 0]
s = input()
IP, Mask = s.split("~")

if not isLegalIP(IP) or not isLegalMaskCode(Mask):
    Err += 1
else:
    if isPrivateIP(IP):
        P += 1
    cat = CatagoryIP(IP)
    if cat == "A": A += 1
    if cat == "B": B += 1
    if cat == "C": C += 1
    if cat == "D": D += 1
    if cat == "E": E += 1

print(A, B, C, D, E, Err, P)
