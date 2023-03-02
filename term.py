from ecuation import Ecuation
from typing import Union

class Term:
    coeficient: Union[int, Ecuation]
    exponent: Union[int, Ecuation]
    variable: str

    def __init__(self, coeficient, variable, exponent) -> None:
        self.coeficient = coeficient
        self.exponent = exponent
        self.variable = variable
