from alu import *

registers = {
    'A': [0, 0, 0, 0],
    'B': [0, 0, 0, 0],
    'ACC': [0, 0, 0, 0]
}


def load(register_name, value):
    if len(value) == 4:
        registers[register_name] = value.copy()

def get(register_name):
    return registers[register_name]
    
# A=Register('A')
# B=Register('B')
# ACC=Register('ACC')

# A.load([1,0,0,1]) # 9
# B.load([0,1,0,0]) # 4
# alu=ALU()
# ACC.load(alu.operate('ADD' , A.get() , B.get()))

# print(ACC.get())