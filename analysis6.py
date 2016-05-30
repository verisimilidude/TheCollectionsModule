from collections import Counter, namedtuple, defaultdict, deque, OrderedDict
import csv

def get_header(csv_stream):
    """ Read in the first line of the CSV file which is a comma separated
    list of column names.  Strip leading/trailing space from the names in
    the list and return the list.
    """
    # read the first line of the file as a list
    header = csv_stream.__next__()
    # strip spaces from around the column names
    for colno, column in enumerate(header):
       header[colno] = column.strip()
    return header

def main():
    cntr = Counter()
    lead_contractors = defaultdict(int)
    with open(r'C:\Users\Phil\pytalk\Building_Permits.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = get_header(csv_reader)
        year_totals = OrderedDict()
        #year_totals = dict()
        for year in range(2001,2017):
            year_totals[str(year)] = 0
        year_totals[''] = 0
        building_permit = namedtuple('BuildingPermit',header, rename=True)
        for line in csv_reader:
            fields = building_permit(*line)
            year_issued = fields.ISSUE_DATE[6:]
            year_totals[year_issued] += 1
    print("Total permits issued by year\nYear  # issued")
    for year,num_issued in year_totals.items():
        print("%4s  %8d" % (year, num_issued))
        

    
if __name__ == '__main__':
    main()
