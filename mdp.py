#!/usr/bin/python3
import sys
import fileinput
import re
import argparse

def print_section(regex, print_body):
    header_match = False
    for line in fileinput.input(files=args.files):
        line = re.sub('^\ufeff', '', line) # remove UTF-8 BOM
        m = re.match('# +', line)
        if m:
            mp = re.search(regex, line)
            if args.reverse:
                if mp:
                    mp = False
                else:
                    mp = True
            if mp:
                sys.stdout.write(line)
                header_match = True
            else:
                header_match = False
        else:
            if not print_body:
                continue
            if header_match:
                sys.stdout.write(line)

def main():
    if args.pattern:
        print_section(args.pattern, args.section)
    else:
        print_section('.*', args.section)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process MD files.')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    parser.add_argument('-p', '--pattern', help='regex to match a header')
    parser.add_argument('-s', '--section', action='store_true', help='print section body')
    parser.add_argument('-r', '--reverse', action='store_true', help='print unmatched section')
    args = parser.parse_args()

    main()
