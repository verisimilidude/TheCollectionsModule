from collections import Counter
import csv

def get_header(csv_stream):
        header = csv_stream.__next__()
        for colno, column in enumerate(header):
           header[colno] = column.strip()
        return header

def main():
    cntr = Counter()
    with open(r'C:\Users\Phil\pytalk\Building_Permits.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = get_header(csv_reader)
        for line in csv_reader:
            cntr['Total lines'] += 1
            cntr[line[2]] += 1
    print("Report on column %s\n" % header[2])
    for ctr in sorted(cntr.keys()):
        print('%-30s %8d %6.2f' % (ctr, cntr[ctr],
                                    ((cntr[ctr]*100)/cntr['Total lines'])))

if __name__ == '__main__':
    main()
