memory = {'cells': [None] * 16}

def load_program(program):
    for i in range(len(program)):
        memory['cells'][i] = program[i]

def read_memory(address):
    return memory['cells'][address]

def write_memory(address, value):
    memory['cells'][address] = value

# mem=Memory()
# program=[
#     ('LOAD', 'A', [0, 1, 0, 1]),
#     ('LOAD', 'B', [0, 0, 1, 0]),
#     ('ADD', 'A', 'B'),
#     ('HALT')
# ]

# mem.load_program(program)
# print(mem.read(3))