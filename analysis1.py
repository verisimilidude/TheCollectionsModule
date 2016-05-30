from collections import Counter

def main():
    cntr = Counter()
    for line in open(r'C:\Users\Phil\pytalk\Building_Permits.csv'):
        cntr['lines'] += 1
    print(cntr['lines'])

if __name__ == '__main__':
    main()
