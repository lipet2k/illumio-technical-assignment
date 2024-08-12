from log_parser.protocol import Protocols
from log_parser.reader import Reader
from log_parser.writer import Writer

class Parser:
    
    def __init__(self, lookup_table:str):
        self.port_protocol_count = dict()
        self.tag_count = dict()
        self.combination_to_tag = dict()
        self._read_lookup_table(lookup_table=lookup_table)
    
    def read_logs(self, logs:str) -> None:
        for line in Reader.read_text_file(logs):
            record_fields = line.split()
            version, account_id, interface_id, srcaddr, dstaddr, srcport, dstport, protocol_decimal, packets, bytes, start, end, action, log_status = record_fields[:14]
            
            protocol_keyword = Protocols.get_keyword(decimal=protocol_decimal)

            if protocol_keyword and (dstport, protocol_keyword) in self.port_protocol_count.keys():
                self.port_protocol_count[(dstport, protocol_keyword)] += 1
                tag = self.combination_to_tag[(dstport, protocol_keyword)]
                self.tag_count[tag] += 1
            else:
                self.tag_count["Untagged"] += 1
    
    def write_output(self, port_protocol_filename:str, tag_matches_filename:str) -> None:
        Writer.write_port_protocol_counts(filename=port_protocol_filename, port_protocol_count=self.port_protocol_count)
        Writer.write_tag_counts(filename=tag_matches_filename, tag_counts=self.tag_count)
        
    def _read_lookup_table(self, lookup_table:str) -> None:
        self.tag_count["Untagged"] = 0
        for index, row in enumerate(Reader.read_csv_file(lookup_table)):
            if index == 0:
                continue
            dstport, protocol_keyword, tag = row
            self.combination_to_tag[(dstport, protocol_keyword)] = tag
            self.tag_count[tag] = 0
            self.port_protocol_count[(dstport, protocol_keyword)] = 0