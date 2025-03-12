# file.py
import os
import json
import csv

def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def extract_data_from_json(json_file):
    date =  json_file.split('/')[2].split('_')[0]
    frecuency = json_file.split('/')[2].split('_')[-2][:-3]
    heigth = json_file.split('/')[2].split('_')[-1][:-1]
    pool_name = json_file.split('/')[3]
    print(json_file)
    with open(json_file, 'r') as f:
        data = json.load(f)
        print(data.get('depth_pool',''))
        return {
            'date': date,
            'pool_name': pool_name,
            'frecuency': frecuency,
            'heigth': heigth,
            'd1_mean': data.get('diagonal1', '').get('mean', '')*-1,
            'd2_mean': data.get('diagonal2', '').get('mean', '')*-1,
            'mean_pool': data.get('depth_pool','').get('mean','')*-1,
            'height_water_normalized': data.get('height_water_normalized', ''),
            'x_min': data.get('denormalize', '').get('x_min', ''),
            'x_max': data.get('denormalize', '').get('x_max', ''),
            'y_min': data.get('denormalize', '').get('y_min', ''),
            'y_max': data.get('denormalize', '').get('y_max', ''),
            'z_min': data.get('denormalize', '').get('z_min', ''),
            'z_max': data.get('denormalize', '').get('z_max', '')
        }

def save_to_csv(data, output_csv):
    keys = data[0].keys()
    with open(output_csv, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main(directory, output_csv):
    json_files = find_json_files(directory)
    json_files = sorted(json_files)
    data = [extract_data_from_json(json_file) for json_file in json_files]
    save_to_csv(data, output_csv)

if __name__ == "__main__":
    directory = 'discrete_model/mean'  # Reemplaza con la ruta de tu carpeta
    output_csv = 'output.csv'  # Nombre del archivo CSV de salida
    main(directory, output_csv)