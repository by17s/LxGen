class LxGenMainSoCCodeGen:
    def __init__(self, iname: str, name: str, bus: str = "wishbone", adddata: dict = {}):
        self.iname = iname
        self.name = name
        self.bus = bus
        self.adddata = adddata
    def __add_to_bus(self, bus: str, loc: str):
        if bus not in ["wishbone"]:
            raise ValueError(f"Unsupported bus type: {bus}")
        if bus == "wishbone":
            if self.iname in ["uart", "spi", "i2c"]:
                return f'self.add_csr("{self.name}")\n'
        return f''

    def __init_interface(self):
        match self.iname:
            case "gpio":
                return f'self.submodules.{self.name} = GPIO{self.adddata["mode"]}(self.platform.request("{self.name}", 0))\n'
            case "uart":
                return f'self.add_uart("{self.name}", uart_pads=platform.request("{self.name}", 0))\n'
            case "spi":
                return f'self.submodules.{self.name} = SPIMaster(platform.request("{self.name}"), 8, sys_clk_freq, spi_clk_freq={self.adddata["lfreq"]})\n'
            case "i2c":
                return f'self.submodules.{self.name} = I2CMaster(self.platform.request("{self.name}"))\n'
            case "clk":
                return ""
            case _:
                raise ValueError(f"Unsupported interface type: {self.iname}")
        
    def gen_code(self):
        code = ""
        code += "\t\t" + self.__init_interface()
        code += "\t\t" + self.__add_to_bus(self.bus, self.name)
        return code
    