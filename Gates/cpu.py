from alu import *
from register import *
from program_counter import *
from instruction_register import *
from memory import *

# Setup for registers
registers = {
    'A': [0, 0, 0, 0],
    'B': [0, 0, 0, 0],
    'ACC': [0, 0, 0, 0]
}

def load_register(reg_name, value):
    if len(value) == 4:
        registers[reg_name] = value.copy()

def get_register(reg_name):
    return registers[reg_name]

def cpu_load(program):
    load_program(program)

def cpu_run():
    while True:
        instr_address = get_pc()
        instr = read_memory(instr_address)
        load_instruction(instr)

        opcode = instr[0]

        if opcode == 'LOAD':
            reg = instr[1]
            value = instr[2]
            load_register(reg, value)

        elif opcode == 'ADD':
            reg1 = get_register(instr[1])
            reg2 = get_register(instr[2])
            result = operate('ADD', reg1, reg2)
            load_register('ACC', result)

        elif opcode == 'SUB':
            reg1 = get_register(instr[1])
            reg2 = get_register(instr[2])
            result = operate('SUB', reg1, reg2)
            load_register('ACC', result)

        elif opcode == 'STORE':
            src = instr[1]
            dest = instr[2]
            value = get_register(src)
            load_register(dest, value)

        elif opcode == 'JMP':
            jump_pc(instr[1])
            continue

        elif opcode == 'HALT':
            print("Execution halted.")
            break

        increment_pc()


program = [
    ('LOAD', 'A', [0, 1, 0, 1]),  # 5
    ('LOAD', 'B', [0, 0, 1, 1]),  # 3
    ('ADD', 'A', 'B'),
    ('HALT',)
]


cpu_load(program)
cpu_run()

print(get_register('A'))  # [0, 1, 0, 1] (unchanged)
print(get_register('ACC'))  # Should print the result of 5 + 3 = [1, 0, 0, 0]