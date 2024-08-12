import csv
from collections.abc import Iterator

class Reader:
    
    @staticmethod
    def read_text_file(filename:str) -> Iterator[str]:
        with open(filename) as file:
            for line in file:
                yield line

    @staticmethod
    def read_csv_file(filename:str) -> Iterator[str]:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                yield row