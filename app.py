from src.parser import Parser

parser = Parser(lookup_table='./test/examples/example.csv')
parser.read_logs(logs='./test/examples/example.txt')
parser.write_output(port_protocol_filename='port_protocol_matches.csv', tag_matches_filename='tag_matches.csv')