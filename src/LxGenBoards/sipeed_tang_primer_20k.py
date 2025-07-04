from src.LxGenBoards.LxGenBoard import LxGenBoard, LxGenBoardDependency

class SipeedTangPrimer20K(LxGenBoard):
    def __init__(self):
        super().__init__("sipeed_tang_primer_20k")

    def __generate__(self):
        print(f"[SipeedTangPrimer20K] Generating configuration for {self.name}")
        
    def add_dependency(self, depend: LxGenBoardDependency) -> bool:
        return super().add_dependency(depend)
