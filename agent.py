#!/usr/bin/python

import random

class Agent:
    """
    Base class for agents in cake-cutting. Records valuations and includes all
    valuation generation functions. Child classes implement agent behavior for
    specific cake-cutting procedures.
    """
    def __init__(self, config, id):
        self.conf = config
        self.id = id
        self.V = [] # value for each of the conf.num_pieces pieces of the cake

    def gen_uniform_valuation(self):
        self.V = [1] * self.conf.num_pieces

    def gen_random_int_valuation(self, a=0, b=1):
        self.V = [round(random.uniform(a, b))
                  for i in range(self.conf.num_pieces)]
    
    def get_value_of_atoms(self, atoms):
        value = 0
        for atom in atoms:
            value += self.V[atom]
        return value
    
    def get_total_cake_value(self):
        return sum(self.V)

    # TODO add more value generation functions

    def __repr__(self):
        return "%s(id=%s valuation=%s)" % (
            self.__class__.__name__,
            self.id, self.V)
