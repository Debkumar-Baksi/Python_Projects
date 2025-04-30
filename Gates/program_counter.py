program_counter = {'address': 0}

def increment_pc():
    program_counter['address'] += 1

def jump_pc(addr):
    program_counter['address'] = addr

def get_pc():
    return program_counter['address']
# pc=ProgramCounter()

# print("Initial PC : ",pc.get())

# for _ in range(3):
#     print("Program Counter : ",pc.get())
#     pc.increment()


# pc.jump(10)
# pc.increment()
# print("Current address : ",pc.get())