
import argparse
from pathlib import Path

def find(path, glob):
    result = []
    for path in Path(path).rglob(glob):
        result.append(path)
    return result

def main(args):
    for path in find(args.path, args.pattern):
        print(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find files in a directory')
    parser.add_argument('-p', '--path', help='path to search', default=".")
    parser.add_argument('-g', '--pattern', help='pattern (glob) to search for', default="*")
    
    args = parser.parse_args()
    main(args)    
