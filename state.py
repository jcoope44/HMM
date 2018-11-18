import emission

class ProbabiltyStatePair:
    def __init__(self, probability, state):
        self.probability = probability
        self.state = state


class State:
    def __init__(self, name):
        self.name = name
        self.states = {}
        self.emissions = {}
    def add_state(self, state, probability):
        pair = ProbabiltyStatePair(probability, state)
        self.states[state.name] = pair
    def add_emission(self, emission_to_add, probability):
        pair = emission.ProbabiltyEmissioinPair(probability, emission_to_add)
        self.emissions[emission_to_add.name] = pair