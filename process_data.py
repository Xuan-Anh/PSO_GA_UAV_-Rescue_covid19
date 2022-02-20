
import os
import io
import pandas as pd

# BASE_DIR = "/"
X_COORD = 'x'
Y_COORD = 'y'
COORDINATES = 'coordinates'
INSTANCE_NAME = 'instance_name'
MAX_VEHICLE_NUMBER = 'max_vehicle_number'
VEHICLE_CAPACITY = 'vehicle_capacity'
DEPART = 'depart'
DEMAND = 'demand'
READY_TIME = 'ready_time'
DUE_TIME = 'due_time'
SERVICE_TIME = 'service_time'
DISTANCE_MATRIX = 'distance_matrix'


def calculate_distance(cust_1, cust_2):
    x_diff = cust_1[COORDINATES][X_COORD] - cust_2[COORDINATES][X_COORD]
    y_diff = cust_1[COORDINATES][Y_COORD] - cust_2[COORDINATES][Y_COORD]
    return (x_diff**2 + y_diff**2)**0.5


def load_problem_instance(problem_name='R101'):
    
    text_file = os.path.join('data_csv', problem_name + '.csv')
    parsed_data = {}

    data_csv = pd.read_csv(text_file, sep=',')

    
    parsed_data[INSTANCE_NAME] = data_csv[INSTANCE_NAME][0]
    # print("________________ parsed_data[INSTANCE_NAME] ________________")
    # print(parsed_data)

    parsed_data[MAX_VEHICLE_NUMBER] = int(data_csv[MAX_VEHICLE_NUMBER][0])
    parsed_data[VEHICLE_CAPACITY] = float(data_csv[VEHICLE_CAPACITY][0])
# vị trí khởi hành
    parsed_data[DEPART] = {
                    COORDINATES: {
                        X_COORD: float(data_csv[X_COORD][0]),
                        Y_COORD: float(data_csv[Y_COORD][0]),
                    },

                    DEMAND: float(data_csv[DEMAND][0]),
                    READY_TIME: float(data_csv[READY_TIME][0]),
                    DUE_TIME: float(data_csv[DUE_TIME][0]),
                    SERVICE_TIME: float(data_csv[SERVICE_TIME][0]),
                }
                
    number_of_customers = len(data_csv) - 1
    for i in range(1, number_of_customers + 1):
        parsed_data[F'C_{i}'] = {
                        COORDINATES: {
                            X_COORD: float(data_csv[X_COORD][i]),
                            Y_COORD: float(data_csv[Y_COORD][i]),
                        },
                        DEMAND: float(data_csv[DEMAND][i]),
                        READY_TIME: float(data_csv[READY_TIME][i]),
                        DUE_TIME: float(data_csv[DUE_TIME][i]),
                        SERVICE_TIME: float(data_csv[SERVICE_TIME][i]),
                    }
            


    customers = [DEPART] + [F'C_{x}' for x in range(1, number_of_customers+1)]
    parsed_data[DISTANCE_MATRIX] = \
        [[calculate_distance(parsed_data[c1], parsed_data[c2]) for c1 in customers] for c2 in customers]

    return parsed_data


if __name__ == '__main__':
    data =  load_problem_instance()
    print(data)
    # print(data)