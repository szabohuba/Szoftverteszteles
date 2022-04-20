import calc
import sys



def test_calc_addition():
    output = calc.add(1, 2)
    assert output == 3


def test_calc_subtract():
    output = calc.subtract(3, 1)
    assert output == 2


def test_calc_multiply():
    output = calc.multiply(2, 3)
    assert output == 6

    
def test_calc_divide():
    output = calc.divide(6, 3)
    assert output == 2


def test_calc_powerOf():
    output = calc.powerOf(2, 10)
    assert output == 1024


def test_calc_divide():
    output = calc.divide(1, 1)
    assert output == 1
 
def test_calc_maximum():
    output = calc.maximum(sys.maxsize+1,32111)
    assert output == sys.maxsize+1


def test_calc_minimum():
    output = calc.minimum(1200,32111)
    assert output == 1200
    