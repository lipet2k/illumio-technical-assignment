import csv
import os

class Writer:
    
    @staticmethod
    def write_tag_counts(filename:str, tag_counts:dict, output_dir:str='output') -> None:
        Writer._create_output_dir(folder_name=output_dir)
        with open(f"{output_dir}/" + filename, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Tag', 'Count'])
            
            for tag, count in tag_counts.items():
                writer.writerow([tag, count])
                
    @staticmethod
    def write_port_protocol_counts(filename:str, port_protocol_count:dict, output_dir:str='output') -> None:
        Writer._create_output_dir(folder_name=output_dir)
        with open(f"{output_dir}/" + filename, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Port', 'Protocol', 'Count'])
            
            for port_protocol, count in port_protocol_count.items():
                writer.writerow([port_protocol[0], port_protocol[1], count])
    
    @staticmethod
    def _create_output_dir(folder_name:str) -> None:
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)