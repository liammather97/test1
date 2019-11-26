import pytest
import factorial

def negative_test():
    assert factorial.factorial(-3)==""

def zero_test():
    assert factorial.factorial(0)
    
