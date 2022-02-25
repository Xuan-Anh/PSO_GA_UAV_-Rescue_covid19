from process_data import load_problem_instance
import pandas as pd
import random
import os

if __name__ == '__main__':
    for file in os.listdir('data/'):
        file = file.strip('.txt')
        instance = load_problem_instance(file)
        data = {'instance_name': [instance['instance_name']], 'max_vehicle_number': [instance['max_vehicle_number']],
            'vehicle_capacity': [instance['vehicle_capacity']],'cust_no':[], 'x':[], 'y':[],
            'demand':[], 'ready_time':[], 'due_time':[], 'service_time':[], 'expired_time':[]}
        # tạo thời gian hết hạn của mẫu
        ave_demand = 0
        number_targer = 0
        sum_distance = 0
        ave_service_time =0
        
        for uav in instance['distance_matrix']:
            for j in uav:
                sum_distance +=j

        #convert csv
        del instance['instance_name']
        del instance['max_vehicle_number']
        del instance['vehicle_capacity']
        del instance['distance_matrix']
        
        for key in instance.keys():
            number_targer += 1
            data['instance_name'].append(None)
            data['max_vehicle_number'].append(None)
            data['vehicle_capacity'].append(None)
            data['cust_no'].append(key)
            data['x'].append(instance[key]['coordinates']['x'])
            data['y'].append(instance[key]['coordinates']['y'])
            data['demand'].append(instance[key]['demand'])
            ave_demand += instance[key]['demand']
            data['ready_time'].append(instance[key]['ready_time'])
            data['due_time'].append(instance[key]['due_time'])
            data['service_time'].append(instance[key]['service_time'])
            ave_service_time += instance[key]['service_time']
            data['expired_time'].append(None)
        data['instance_name'].pop()
        data['max_vehicle_number'].pop()
        data['vehicle_capacity'].pop()

        ave_demand = ave_demand/number_targer
        ave_number_target_of_uav = data['vehicle_capacity'][0]/ave_demand
        ave_distance = sum_distance/(number_targer**2)
        ave_service_time = ave_service_time/number_targer
        #thời gian trung bình 1 UAV đi
        time_window = (ave_distance + ave_service_time)*(ave_number_target_of_uav+1)

        for i in range(number_targer):
            data['expired_time'][i] = data['due_time'][i] + int(time_window * random.random())

        df = pd.DataFrame(data)
        df.to_csv('data_csv/'+df['instance_name'][0] + '.csv')



