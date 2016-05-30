from collections import Counter, namedtuple
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
        building_permit = namedtuple('BuildingPermit',header, rename=True)
        for line in csv_reader:
            fields = building_permit(*line)
            cntr['Total lines'] += 1
            cntr[fields.PERMIT_TYPE] += 1
            paid = float(fields.AMOUNT_PAID[1:])
            cntr[fields.PERMIT_TYPE+'_paid'] += paid
            cntr['Total paid'] += paid
    print("Report on columns PERMIT_TYPE and AMOUNT_PAID\n")
    for ctr in sorted(cntr.keys()):
        if ctr == 'Total lines':
            print('%-30s %8d %6.2f %15.2f %6.2f' % (ctr, cntr[ctr],
                                    ((cntr[ctr]*100)/cntr['Total lines']),
                                    cntr['Total paid'],
                                    100.0))
        elif not ctr.endswith('paid'):
            print('%-30s %8d %6.2f %15.2f %6.2f' % (ctr, cntr[ctr],
                                    ((cntr[ctr]*100)/cntr['Total lines']),
                                    cntr[ctr+'_paid'],
                                    ((cntr[ctr+'_paid']*100)/cntr['Total paid'])))

if __name__ == '__main__':
    main()
