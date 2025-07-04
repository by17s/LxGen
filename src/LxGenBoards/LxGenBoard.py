class LxGenBoardDependency:
    def __init__(self, name, path):
        self.name = name
        self.path = path

class LxGenBoard:
    def __init__(self, name):
        self.name = name
        self.dependency = []
        print(f"[LxGenBoard] Current board: {self.name}")
    
    def add_dependency(self, depend: LxGenBoardDependency) -> bool:
        self.dependency.append(depend)
        
    def gen_import(self):
        if not self.dependency:
            return ""
        imports = [f"from {dep.path} import {dep.name}" for dep in self.dependency]
        return "\n".join(imports)
