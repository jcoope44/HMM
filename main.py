import readFile
import state
import emission
import getProbability

states = readFile.get_states()
emissions = readFile.get_emissions(states)

observations = []
observations_valid = False
while not observations_valid:
    observation_string = input('Enter observation sequence (ex: A, B, C): ')
    observation_string = observation_string.replace(' ', '')
    observations = observation_string.split(',')

    observations_valid = True
    for observation in observations:
        if  observation not in emissions:
            observations_valid = False
            break
    
    if not observations_valid:
        print('Invalid observation sequence. Please try again.')
    

probability_and_sequence = getProbability.get_probability_and_sequence(states, emissions, observations) 
print(\
'The most likely state sequence is', probability_and_sequence.sequence,\
'with a probability of', probability_and_sequence.probability)





