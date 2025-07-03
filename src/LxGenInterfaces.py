from src.LxGenIO import LxGenIO
from src.LxGenMainSoCCodeGen import LxGenMainSoCCodeGen

class LxGenInterface:
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        self.name = name
        self.io = io
        self.pins = pins
        self.bus = bus

    def __repr__(self):
        return f"LxGenInterface(name={self.name}, io={self.io}, pins={self.pins})"

class LxGenUART(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        super().__init__(name, io, pins)
        self.type = "uart"
        print(f"[LxGenUART] Initializing UART interface (Name: <{self.name}> IO: {self.io})")

    def __repr__(self):
        return f"LxGenUART(name={self.name}, io={self.io}, pins={self.pins})"
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus).gen_code()
        ]
        
class LxGenSPI(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        super().__init__(name, io, pins)
        self.type = "spi"
        print(f"[LxGenSPI] Initializing SPI interface (Name: <{self.name}> IO: {self.io})")

    def __repr__(self):
        return f"LxGenSPI(name={self.name}, io={self.io}, pins={self.pins})"
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus, {"lfreq" : 1000}).gen_code()
        ]
        
class LxGenClk(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        super().__init__(name, io, pins)
        self.type = "clk"
        print(f"[LxGenClk] Initializing Clk interface (Name: <{self.name}> IO: {self.io})")

    def __repr__(self):
        return f"LxGenClk(name={self.name}, io={self.io}, pins={self.pins})"
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus, {"lfreq" : 27e6}).gen_code()
        ]