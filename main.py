if __name__ == "__main__":
    import sys
    from src import LxGen
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
        
    lg = LxGen.LxGen(sys.argv[1])
    lg.generate()