import toml

from src.LxGenInterfaces import LxGenGPIO, LxGenUART, LxGenSPI, LxGenClk

class LxGen:
    # Supported boards
    supported_boards = ["sipeed_tang_primer_20k"]

    def __init__(self, input_file):
        self.input_file = input_file
        self.interfaces = {}
        self.interfaces_list = []
        

        with open(self.input_file, "r") as f:
            self.config = toml.load(f)  # передаём открытый файл, а не строку
            self.FPGA_name = self.config.get('board', None)
            self.board = None

            if not self.FPGA_name:
                raise ValueError("FPGA name not found in the configuration file.")
            
            if self.FPGA_name not in self.supported_boards:
                raise ValueError(f"Unsupported board: {self.FPGA_name}. Supported boards are: {', '.join(self.supported_boards)}")
            
            self.__load_board()
            self.__load_interfaces()
            
            tio = open("test.io", "a+")
            lcfg = open("test.lcfg", "a+")
            for interface in self.interfaces_list:
                gen = interface.generate()
                print(gen[0], file=tio)
                print(gen[1], file=lcfg)
            
    def __load_interfaces(self):
        self.interfaces = self.config.get('interfaces', [])
        if not self.interfaces:
            raise ValueError("No interfaces found in the configuration file.")
        
        for interface in self.interfaces:
            #print(f"Interface Type: {interface.get('type')}, Name: {interface.get('name')}, IO: {interface.get('io')}, Pins: {interface.get('pins')}") 
            match interface.get('type'):
                case 'gpio':
                    self.interfaces_list.append(LxGenGPIO(
                        name=interface['name'],
                        io=interface['io'],
                        pins=interface['pins'],
                        mode=interface.get('mode', 'InOut')
                    ))
                case 'uart':
                    self.interfaces_list.append(LxGenUART(
                        name=interface['name'],
                        io=interface['io'],
                        pins=interface['pins']
                    ))
                case 'spi':
                    self.interfaces_list.append(LxGenSPI(
                        name=interface['name'],
                        io=interface['io'],
                        pins=interface['pins']
                    ))
                case 'clk':
                    self.interfaces_list.append(LxGenClk(
                        name=interface['name'],
                        io=interface['io'],
                        pins=interface['pins']
                    ))
                case _:
                    raise ValueError(f"Unsupported interface type: {interface.get('type')}")       
            

    def __load_board(self):
        match self.FPGA_name:
            case "sipeed_tang_primer_20k":
                from src.LxGenBoards.sipeed_tang_primer_20k import SipeedTangPrimer20K
                self.board = SipeedTangPrimer20K()
            case _:
                raise ValueError(f"Unsupported board: {self.FPGA_name}. Supported boards are: {', '.join(self.supported_boards)}")

    def generate(self):
        # Placeholder for generation logic
        
        print(f"Generating with config: {self.config}")