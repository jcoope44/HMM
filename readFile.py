import csv
import state
import emission

def get_states():
    with open('transition_matrix.csv') as transition:
        reader = csv.reader(transition, delimiter=',')
        states = {}
        csv_header = next(reader)

        for row in reader:
            current_state = state.State(row[0])
            states[row[0]] = current_state
        
        transition.seek(0)

        row_number = 0
        for row in reader:
            if row_number != 0:
                column_number = 0
                for column in row:
                    if column_number != 0:
                        states[row[0]].add_state(states[csv_header[column_number]], float(column))
                    column_number += 1    
            row_number += 1

        return states


def get_emissions(states):
    with open('emission_matrix.csv') as emission_matrix:
        reader = csv.reader(emission_matrix, delimiter=',')
        csv_header = next(reader)
        emissions = {}

        row_number = 0
        for header in csv_header:
            if row_number != 0:
                current_emission = emission.Emission(header)
                emissions[header] = current_emission
            row_number += 1    
        
        emission_matrix.seek(0)
        row_number = 0
        for row in reader:
            if row_number != 0:
                column_number = 0
                for column in row:
                    if column_number != 0:
                        current_state = states[row[0]]
                        current_emission = emissions[csv_header[column_number]]
                        current_emission.add_state(current_state, float(column))
                        current_state.add_emission(current_emission, float(column))
                    column_number +=1
            row_number += 1

        return emissions
