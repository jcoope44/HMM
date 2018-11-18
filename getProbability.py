import state
import emission

def get_probability_and_sequence(states, emissions, observations):
    probability_matrix = get_probability_matrix(states, emissions, observations)
    index = len(observations) - 1
    
    probability = 0.0
    state_sequence = []
    for probability_key in probability_matrix:
        if probability_matrix[probability_key][index] >= probability:
            if len(state_sequence) > 0:
                state_sequence[0] = probability_key
            else:
                state_sequence.append(probability_key)
            probability = probability_matrix[probability_key][index]

    index -= 1
    while index >= 0:
        proceding_state = get_most_likely_proceding_state(states, state_sequence[-1], probability_matrix, index)
        state_sequence.append(proceding_state)
        index -= 1

    state_sequence.reverse()
    return type('',(object,),{'sequence' : state_sequence, 'probability' : probability})()

def get_most_likely_proceding_state(states, state, probability_matrix, i):
    best_probability = 0
    best_state = ""
    for key in probability_matrix:
        probability = probability_matrix[key][i] * states[key].states[state].probability
        if probability > best_probability:
            best_probability = probability
            best_state = key
    
    return best_state
        

def get_probability_matrix(states, emissions, observations):
    i = 0
    probabilityMatrix = {}
    for observation in observations:
        if i == 0:
            get_initial_probability(states, emissions, observation, probabilityMatrix)
        else:
            get_probability(states, emissions, observation, probabilityMatrix, i)
        i += 1

    return probabilityMatrix

def get_initial_probability(states, emissions, observation, probabilityMatrix):
    for key, current_state in states.items():
        probabilityMatrix[key] = [current_state.emissions[observation].probability]

def get_probability(states, emissions, observation, probabilityMatrix, i):
    for key, current_state in states.items():
        best_probability = 0
        for probability_key, state_probability in probabilityMatrix.items():
            probability = state_probability[i - 1] * states[probability_key].states[key].probability \
            * current_state.emissions[observation].probability
            if probability >= best_probability:
                best_probability = probability
        probabilityMatrix[key].append(best_probability)

