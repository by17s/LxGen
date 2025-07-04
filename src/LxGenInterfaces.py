from src.LxGenIO import LxGenIO
from src.LxGenMainSoCCodeGen import LxGenMainSoCCodeGen

class LxGenInterface:
    def __init__(self, itype: str, name, io, pins, bus: str = "wishbone"):
        self.name = name
        self.io = io
        self.pins = pins
        self.bus = bus
        self.type = itype.lower()
        
        print(f"[LxGen{self.type.upper()}] Initializing {self.type} interface (Name: <{self.name}> IO: {self.io})")

    def __repr__(self):
        return f"LxGenInterface(name={self.name}, io={self.io}, pins={self.pins})"
    
class LxGenGPIO(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone", mode: str = "InOut"):
        super().__init__("GPIO", name, io, pins)
        
        if mode not in ["In", "Out", "InOut", "IRQ"]:
            raise ValueError(f"Unsupported mode: {mode}. Supported modes are: In, Out, InOut, IRQ")
        self.mode = mode
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus, {"mode" : self.mode}).gen_code()
        ]

class LxGenUART(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        super().__init__("UART", name, io, pins)
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus).gen_code()
        ]
        
class LxGenSPI(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        super().__init__("spi", name, io, pins)
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus, {"lfreq" : 1000}).gen_code()
        ]
        
class LxGenClk(LxGenInterface):
    def __init__(self, name, io, pins, bus: str = "wishbone"):
        super().__init__("clk", name, io, pins)
    
    def generate(self):
        return [
            LxGenIO(self.name, self.pins, self.io).gen_record(),
            LxGenMainSoCCodeGen(self.type, self.name, self.bus, {"lfreq" : 27e6}).gen_code()
        ]