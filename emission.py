import state

class ProbabiltyEmissioinPair:
    def __init__(self, probability, emission):
        self.probability = probability
        self.emission = emission


class Emission:
    def __init__(self, name):
        self.name = name
        self.states = []
    def add_state(self, state_to_add, probability):
        pair = state.ProbabiltyStatePair(probability, state_to_add)
        self.states.append(pair)