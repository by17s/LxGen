if __name__ == "__main__":
    import sys
    from src import lxgen
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
        
    lg = lxgen.LxGen(sys.argv[1])