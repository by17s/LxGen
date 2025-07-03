class LxGenIO:
    def __init__(self, name, pins, io):
        self.name = name
        self.pins = pins
        self.io = io
        print(f"[LxGenIO] Initializing IO (Name: <{self.name}> IO: {self.io} Pins: {self.pins})")

    def gen_record(self):
        if len(self.pins) == 0:
            raise ValueError("[LxGenIO] Pins cannot be empty.")
        elif len(self.pins) == 1:
            return f'\t("{self.name}",  0, Pins("{self.pins[self.name]}"), IOStandard("{self.io}")),\n'
        else:
            d = f'\t("{self.name}", 0,\n'
            for pin in self.pins:
                d += f'\t\tSubsignal("{pin}", Pins("{self.pins[pin]}")),\n'
            d += f'\t\tIOStandard("{self.io}"),\n'
            return d + "\t)\n"
            