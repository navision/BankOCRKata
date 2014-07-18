#!/usr/bin/env python

import argparse
from parser import Parser
from result_writer import ResultWriter


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input_file", help="file to read for account numbers in ocr kata format")
    arg_parser.add_argument("output_file", help="file to write account number statuses in ocr kata format")
    args = arg_parser.parse_args()
    with open(args.input_file, 'r') as infile:
        with open(args.output_file, 'w+') as outfile:
            ResultWriter().write_all(outfile, Parser().account_numbers_from(infile))


if __name__ == "__main__":
    main()