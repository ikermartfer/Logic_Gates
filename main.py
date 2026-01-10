#Base lambda functions
N=lambda input: lambda volts: input and volts
P=lambda input: lambda volts: not input and volts
PARALLEL=lambda input1: lambda input2: input1 or input2
SERIES=lambda input1: lambda input2: input1 and input2
MIDDLE=lambda input1: lambda input2: input1 or input2
#Translation from True and False to one and zero for debugging
NUM=lambda val: "ONE" if val else "ZERO"
#For clarity
VOLTAGE=True
GROUND=False
ONE=True
ZERO=False
#Logic Gates (remaining: XOR,NXOR)
NOT=lambda input: (
    MIDDLE(
        N(input)(GROUND)
    )(
        P(input)(VOLTAGE)
    )
)
AND=lambda input1: lambda input2: (
    MIDDLE(
        SERIES(
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
NAND= lambda input1: lambda input2: NOT(AND(input1)(input2))
NOR=lambda input1: lambda input2: (
    MIDDLE(
        SERIES(
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
OR=lambda input1: lambda input2: NOT(NOR(input1)(input2))

