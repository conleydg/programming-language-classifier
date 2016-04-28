import glob


def read_code(directory):
    files = glob.glob('{}/**/*.python3'.format(directory), recursive=True)
    texts = []
    for file in files:
        with open(file) as f:
            texts.append(f.read())
    print(len(texts))





# file_list = []
#
# for name in glob.glob('/Users/David/documents/tiy/programming-language-classifier/benchmarksgame-2014-08-31/benchmarksgame/bench/threadring/*'):
#     file_list.append(name)

read_code('/Users/David/documents/tiy/programming-language-classifier/benchmarksgame-2014-08-31/benchmarksgame/bench/')
