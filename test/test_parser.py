import os
from log_parser.parser import Parser
from log_parser.writer import Writer

parser = Parser(lookup_table='./test/examples/example.csv')
large_parser = Parser(lookup_table='./test/examples/large_mapping.csv')

def test_init_parser():
    assert parser.combination_to_tag[('25','tcp')] == 'sv_P1'
    assert ('24', 'tcp') not in parser.combination_to_tag.keys()
    
    assert large_parser.combination_to_tag[('100', '100')] == 'tag100'
    assert ('24', '25') not in large_parser.combination_to_tag.keys()

def test_read_logs():
    parser.read_logs(logs='./test/examples/example.txt')
    assert parser.tag_count['Untagged'] == 4
    
    assert os.path.getsize('test/examples/large_logs.txt') > 10000000 # 10 MB
    large_parser.read_logs(logs='./test/examples/large_logs.txt')
    assert large_parser.tag_count['Untagged'] == 100000