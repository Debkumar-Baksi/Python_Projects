# LOGIC GATES
def AND(a,b):
    return int(a and b)

def OR(a,b):
    return int(a or b)

def NOT(x):
    return int(not x)

def XOR(a,b):
    return int(a!=b)

def XNOR(a,b):
    return int(not(a!=b))


# FULL ADDER
def full_adder(a,b,cin):
    op1_xor=XOR(a,b)
    op1_and=AND(a,b)
    op2_and=AND(cin,op1_xor)

    SUM=XOR(op1_xor,cin)
    CARRY=OR(op1_and,op2_and)
    # return (f"SUM : {SUM} , CARRY {CARRY}")
    return SUM , CARRY


# FULL SUBTRACTOR
def full_subtractor(a,b,bin):
    op1_xor=XOR(a,b)
    a_not=NOT(a)
    op1_and=AND(a_not,b)
    DIFF=XOR(op1_xor,bin)
    op1_xor_not=NOT(op1_xor)
    op2_and=AND(bin,op1_xor_not)
    BORROW=OR(op2_and,op1_and)

    # return (f"Difference : {DIFF} , Borrow : {BORROW}")
    return DIFF, BORROW

