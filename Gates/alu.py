from logic_gate import *

from logic_gate import *

def add(A, B):
    result = [0, 0, 0, 0]
    carry = 0
    for i in range(3, -1, -1):
        sum, carry = full_adder(A[i], B[i], carry)
        result[i] = sum
    return result

def sub(A, B):
    result = [0, 0, 0, 0]
    borrow = 0
    for i in range(3, -1, -1):
        diff, borrow = full_subtractor(A[i], B[i], borrow)
        result[i] = diff
    return result

def operate(opcode, A, B):
    if opcode == 'ADD':
        return add(A, B)
    elif opcode == 'SUB':
        return sub(A, B)
        



# a=[1,0,0,1] # 9
# b=[0,1,0,0] # 4
# alu=ALU()
# print(alu.operate('SUB',a,b))