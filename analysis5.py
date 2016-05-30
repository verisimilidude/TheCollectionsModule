from collections import Counter, namedtuple, defaultdict, deque
import csv
from timeit import timeit
from operator import itemgetter

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

def getTop10_method1(lead_contractors):
    return sorted(lead_contractors.items(),reverse=True,key=itemgetter(1))[:10]

def getTop10_method2(lead_contractors):
    top10 = deque(maxlen=10)
    curMin = 0
    for contractor, proj_count in lead_contractors.items():
        if proj_count > curMin:
            top10.appendleft( (contractor, proj_count) )
            curMin = proj_count
    return sorted(list(top10), reverse=True, key=itemgetter(1))

def main():
    cntr = Counter()
    lead_contractors = defaultdict(int)
    with open(r'C:\Users\Phil\pytalk\Building_Permits.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = get_header(csv_reader)
        building_permit = namedtuple('BuildingPermit',header, rename=True)
        for line in csv_reader:
            fields = building_permit(*line)
            cntr['Total lines'] += 1
            lead_contractors[fields.CONTRACTOR_1_NAME] += 1
    print("Lead contractor name is blank %d times (%f percent)" %
          (lead_contractors[''], lead_contractors['']*100/cntr['Total lines']))

    top10Contractorsv1 = getTop10_method1(lead_contractors)
    print("\nMethod 1 Top Contractors (by # of projects)\n"
          "# of Projects      Name")
    for contractor in top10Contractorsv1:
        print("%6d             %s" % tuple(reversed(contractor)))

    top10Contractorsv2 = getTop10_method2(lead_contractors)
    print("\nMethod 2 Top Contractors (by # of projects)\n"
          "# of Projects      Name")
    for contractor in top10Contractorsv1:
        print("%6d             %s" % tuple(reversed(contractor)))

    # Time the two methods
    print("\nCalculating timings")
    def timeable_m1():
        getTop10_method1(lead_contractors)
    def timeable_m2():
        getTop10_method2(lead_contractors)
    print("Time for method 1: %d\nTime for method 2: %d" % (
        timeit(timeable_m1, number=1000),
        timeit(timeable_m2, number=1000)))

if __name__ == '__main__':
    main()
