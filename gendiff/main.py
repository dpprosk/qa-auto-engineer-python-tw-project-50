import argparse
import json
from operator import itemgetter


def start():
    parser = argparse.ArgumentParser(
        description=("Compares two configuration files "
                     "and shows a difference."))
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def generate_diff(file_path1, file_path2):
    f1 = json.load(open(file_path1))
    f2 = json.load(open(file_path2))
    result = []
    for key, value in f1.items():
        if key not in f2:
            result.append(('-', key, value))
        elif value != f2[key]:
            result.append(('-', key, value))
            result.append(('+', key, f2[key]))
        else:
            result.append((' ', key, value))
    for key, value in f2.items():
        if key not in f1:
            result.append(('+', key, value))

    print('{')
    for item in sorted(result, key=itemgetter(1)):
        print(f'  {item[0]} {item[1]}: {item[2]}')
    print('}')