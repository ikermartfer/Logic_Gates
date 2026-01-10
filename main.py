#Base lambda functions
N=lambda input: lambda volts: input and volts
P=lambda input: lambda volts: not input and volts
PARALLEL=lambda input1: lambda input2: input1 or input2
SERIES=lambda input1: lambda input2: input1 and input2
MIDDLE=lambda input1: lambda input2: input1 or input2
#Translation from True and False to one and zero for debugging
NUM=lambda val: "ONE" if val else "ZERO"
#Table for debugging
def table(fn):
    print(f"ZERO ZERO = {fn(ZERO)(ZERO)}")
    print(f"ONE ZERO = {fn(ONE)(ZERO)}")
    print(f"ZERO ONE = {fn(ZERO)(ONE)}")
    print(f"ONE ONE = {fn(ONE)(ONE)}")
#For clarity
VOLTAGE=True
GROUND=False
ONE=True
ZERO=False
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
            P(input1)(GROUND)
        )(
            P(input2)(GROUND)
        )
    )(
        SERIES(
            N(input1)(VOLTAGE)
        )(
            N(input2)(VOLTAGE)
        )
    )
)
NAND= lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        PARALLEL(
            P(input1)(VOLTAGE)
        )(
            P(input2)(VOLTAGE)
        )
    )(
        SERIES(
            N(input1)(GROUND)
        )(
            N(input2)(GROUND)
        )
    )
)
NOR=lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        SERIES(
            P(input1)(VOLTAGE)
        )(
            P(input2)(VOLTAGE)
        )
    )(
        PARALLEL(
            N(input1)(GROUND)
        )(
            N(input2)(GROUND)
        )
    )
)
OR=lambda input1: lambda input2: (         #4 transistors
    MIDDLE(
        SERIES(
            P(input1)(GROUND)
        )(
            P(input2)(GROUND)
        )
    )(
        PARALLEL(
            N(input1)(VOLTAGE)
        )(
            N(input2)(VOLTAGE)
        )
    )
)
NXOR=lambda input1: lambda input2: (         #9 transistors
    MIDDLE(
        P(
            SERIES(
                N(input1)(GROUND)
            )(
                N(input2)(GROUND)
            )
        )(
            PARALLEL(
                N(input1)(GROUND)
            )(
                N(input2)(GROUND)
            )
        )
    )(
        PARALLEL(
            SERIES(
                P(input1)(VOLTAGE)
            )(
                P(input2)(VOLTAGE)
            )
        )(
            SERIES(
                N(input1)(VOLTAGE)
            )(
                N(input2)(VOLTAGE)
            )
        )
    )
)
XOR=lambda input1: lambda input2: (         #9 transistors
    MIDDLE(
        P(
            SERIES(
                N(input1)(VOLTAGE)
            )(
                N(input2)(VOLTAGE)
            )
        )(
            PARALLEL(
                N(input1)(VOLTAGE)
            )(
                N(input2)(VOLTAGE)
            )
        )
    )(
        PARALLEL(
            SERIES(
                P(input1)(GROUND)
            )(
                P(input2)(GROUND)
            )
        )(
            SERIES(
                N(input1)(GROUND)
            )(
                N(input2)(GROUND)
            )
        )
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
#1 bit sum
SUM_1BIT=lambda N1: lambda N2: XOR(N1[0])(N2[0])
#2 bit sum
