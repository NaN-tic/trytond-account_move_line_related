# This file is part of account_move_line_related module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .party import *


def register():
    Pool.register(
        Party,
        module='account_move_line_related', type_='model')
