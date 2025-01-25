import re

def base_conversion(a,b,d):
    j = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    c = 0
    for i in range(len(b)) :
        if b[len(b)-1-i] in j :
            e = 10 + j.index(b[len(b)-1-i])
        else:
            e = int(b[len(b)-1-i])
        c = c + (e * (a**i))
    print("c:",c)
    b = c
    c = ""
    while b != 0 :
        i = b % d
        b = b // d
        if i > 9 :
            i = j[i-10]
        c = str(i) + c
    return c


def convert_base(n,from_base,to_base):
    # 判断是否为负数
    is_negative = n.startswith('-')
    if is_negative:
        n = n[1:]  # 移除负号，稍后再加上
    # 将任意进制的数字字符串转换为十进制整数
    if '.' in n:
        integer_part, fractional_part = n.split('.')
        integer_decimal = int(integer_part, from_base)  # 整数部分转换为十进制
        # 处理小数部分
        fractional_decimal = 0
        for i, digit in enumerate(fractional_part):
            fractional_decimal += int(digit, from_base) * (from_base ** -(i + 1))
    else:
        integer_part = n
        integer_decimal = int(n, from_base)
        fractional_decimal = 0
    # 转换整数部分
    if to_base == 10:
        result_integer = integer_decimal
    else:
        result_integer = ""
        while integer_decimal:
            result_integer = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[integer_decimal % to_base] + result_integer
            integer_decimal //= to_base
    # 转换小数部分
    if to_base == 10:
        result_fractional = fractional_decimal
    else:
        result_fractional = ""
        precision = 10  # 控制小数的精度
        while precision and fractional_decimal:
            fractional_decimal *= to_base
            digit = int(fractional_decimal)
            result_fractional += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[digit]
            fractional_decimal -= digit
            precision -= 1
    # 合并整数部分和小数部分
    if result_fractional:
        result = str(result_integer) + '.' + str(result_fractional)
    else:
        result = result_integer
    # 如果是负数，加上负号
    if is_negative:
        return "-" + str(result)
    return result


def validate_input(P):
    """验证输入内容，允许数字、小数点、正负号和字母"""
    # 正则表达式：匹配负号、数字、小数点和字母
    if P == "" or re.match(r"^[-+]?[0-9a-zA-Z.]*$", P):
        return True
    else:
        return False

def validate_input2(P):
    if P == "" or re.match(r"[0-9]*$", P):
        return True
    else:
        return False