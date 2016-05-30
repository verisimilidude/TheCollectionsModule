from collections import Counter
import csv

def main():
    cntr = Counter()
    with open(r'C:\Users\Phil\pytalk\Building_Permits.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            cntr['Total lines'] += 1
            cntr[line[2]] += 1
    for ctr in sorted(cntr.keys()):
        print('%-30s %8d' % (ctr, cntr[ctr]))

if __name__ == '__main__':
    main()
