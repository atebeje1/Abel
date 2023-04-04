import os
from configparser import ConfigParser

kw = 'SPECIAL_CHARS'

c = ConfigParser()
c.read('setup.ini')

def compile(file):
    print('Compiling {} ...\n\n'.format(file))
    file = open(file, 'r')
    line_num = 0
    while line_num < len(file.readlines()):
        # CHecks for start of code blocks
        print(line_num)
        if file.readlines()[line_num].endswith(chr(int(c.get(kw, 'BLK_START')))):
            print('Start of code block')
        line_num += 1
    
    # for line in file.readlines():
    #     if line[-1] == chr(int(c.get(kw, 'EOL'))):
    #         print('Line of code')
    #     elif line[-1] == c.get(kw, 'BLK_START'):
    #         print('Start of new block')
    #         while not line.startswith(chr(int(c.get(kw, 'BLK_END')))):
                
    #     else:
    #         raise Exception('Missing end of line character')
    #     lexemes = line.split(' ')
    #     print(lexemes)

for file in os.listdir():
    if file == 'main.abel':
        compile('main.abel')