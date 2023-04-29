from bread import Broad
from datetime import date
from pytest import fixture


@fixture()
def board_inst_fix():
    board_inst = Broad()
    board_inst.sourdough_int = 123
    return board_inst


def test_calc_by_form_dough_func(board_inst_fix):
    board_inst_fix.expected_form_dough_int = 1000
    board_inst_fix.calc_ingredient_func()
    for key, value in board_inst_fix.__dict__.items():
        print(key, value)


def test_calc_by_broad_func(board_inst_fix):
    board_inst_fix.expected_broad_int = 900
    board_inst_fix.calc_ingredient_func(broad_prm=True)
    for key, value in board_inst_fix.__dict__.items():
        print(key, value)

