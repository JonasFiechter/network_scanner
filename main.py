from src.features.scanner.components.scanner import Scanner

def run():
    print('start_function!')
    scan = Scanner()
    scan.get_str_from_cmd()

if __name__ == '__main__':
    run()