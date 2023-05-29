import subprocess
import sys

def run_pycodestyle(filename):
    command = ['pycodestyle', '--show-source', '--show-pep8', filename]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <filename>')
        sys.exit(1)
    
    filename = sys.argv[1]
    run_pycodestyle(filename)