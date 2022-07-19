from src.features.scanner.components.scanner import Scanner

def run():
    print('start_function!')
    scan_inst = Scanner()
    scan_inst.search()
    scan_inst.show_results()

if __name__ == '__main__':
    run()