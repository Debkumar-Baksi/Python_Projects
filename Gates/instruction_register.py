instruction_register = {'instruction': None}

def load_instruction(instruction):
    instruction_register['instruction'] = instruction

def get_instruction():
    return instruction_register['instruction']


# ir=InstructionRegister()
# instruction=('LOAD','A',[1,0,1,0])
# ir.load(instruction)
# print(ir.get())