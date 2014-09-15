# -*- coding: utf-8 -*-
from icall import ICall


def setup_module():
    global acall
    acall = ICall(3.1415926, '.2f')

format
def test_icall_constructor():
    assert acall.args == (3.1415926, '.2f')
    assert acall.kwargs == {}

def test_i_call_function():
    assert acall(format) == format(3.1415926, '.2f')
