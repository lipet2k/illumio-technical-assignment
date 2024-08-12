from log_parser.reader import Reader

class Protocols:

    def get_keyword(decimal:str) -> str:
        if decimal in Protocols.protocols.keys():
            return Protocols.protocols[decimal]

        return None
    
    @staticmethod
    def _read_protocols(filename:str='./data/protocol-numbers.csv') -> dict:
        try:
            protocols = dict()
            for index, row in enumerate(Reader.read_csv_file(filename)):
                if index == 0:
                    continue
                decimal, keyword, protocol, header, reference = row
                protocols[decimal] = keyword.lower()
                
            return protocols
        except:
            raise Exception("Failed to read protocols csv file.")
    
    protocols = _read_protocols()