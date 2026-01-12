#For clarity
VOLTAGE=True
GROUND=False
ONE=True
ZERO=False
#Base lambda functions
N=lambda input: lambda volts: input and volts
P=lambda input: lambda volts: not input and volts
#Functions representing the connections in series and in parallel
def SERIES(*args):
    def SERIES2(volts):
        x=args[0](volts)
        for elt in args[1:]:
            x=elt(x)
        return x
    return SERIES2
def PARALLEL(*args):
    def PARALLEL2(volts):
        x=GROUND
        for elt in args:
            x=x or elt(volts)
        return x
    return PARALLEL2
MIDDLE=lambda input1: lambda input2: input1 or input2
#Translation from True and False to one and zero for debugging
NUM=lambda val: "ONE" if val else "ZERO"
#Table for debugging
def table(fn):
    print(f"ZERO ZERO = {fn(ZERO)(ZERO)}")
    print(f"ONE ZERO = {fn(ONE)(ZERO)}")
    print(f"ZERO ONE = {fn(ZERO)(ONE)}")
    print(f"ONE ONE = {fn(ONE)(ONE)}")
#Logic Gates 
NOT=lambda input: (         #2 transistors
    MIDDLE(
        N(input)(GROUND)
    )(
        P(input)(VOLTAGE)
    )
)
AND=lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        PARALLEL(
            P(input1),
            P(input2)
        )(GROUND)
    )(
        SERIES(
            N(input1),
            N(input2)
        )(VOLTAGE)
    )
)
NAND= lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        PARALLEL(
            P(input1),
            P(input2)
        )(VOLTAGE)
    )(
        SERIES(
            N(input1),
            N(input2)
        )(GROUND)
    )
)
NOR=lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        SERIES(
            P(input1),
            P(input2)
        )(VOLTAGE)
    )(
        PARALLEL(
            N(input1),
            N(input2)
        )(GROUND)
    )
)
OR=lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        SERIES(
            P(input1),
            P(input2)
        )(GROUND)
    )(
        PARALLEL(
            N(input1),
            N(input2)
        )(VOLTAGE)
    )
)
NXOR=lambda input1: lambda input2: (         #8 transistors
    MIDDLE(
        PARALLEL(
            SERIES(
                N(input1),
                P(input2)
            ),
            SERIES(
                P(input1),
                N(input2)
            )
        )(GROUND)
    )(
        PARALLEL(
            SERIES(
                P(input1),
                P(input2)
            ),
            SERIES(
                N(input1),
                N(input2)
            )
        )(VOLTAGE)
    )
)
XOR=lambda input1: lambda input2: (         #8 transistors
    MIDDLE(
        PARALLEL(
            SERIES(
                N(input1),
                P(input2)
            ),
            SERIES(
                P(input1),
                N(input2)
            )
        )(VOLTAGE)
    )(
        PARALLEL(
            SERIES(
                P(input1),
                P(input2)
            ),
            SERIES(
                N(input1),
                N(input2)
            )
        )(GROUND)
    )
)
# print(table(XOR))
#For operations, we will represent numbers as lists of ONEs and ZEROs. Here are functions to translate them from list form to decimal
def dectolist(n,b):
    assert n<2**b, "Number needs more bits to be represented"
    sol=[]
    for i in range(b-1,-1,-1):
        if n<2**i:
            sol.append(ZERO)
        else:
            n-=2**i
            sol.append(ONE)
    return sol
#8 bit sum
