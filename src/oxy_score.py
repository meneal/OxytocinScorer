import csv
import argparse
from collections import OrderedDict
from helpers.helpers import rescale, row_select_reduce
    
def score(datafile):
    def rescale_dat(datafile):
        non_zero_medians = ['X3', 'X7', 'X11',' X12',
                            'X25', 'X26', 'X38', 'X45',
                            'X52','X55']

        rev_list = ['X3', 'X7', 'X11', 'X12', 'X15',
                          'X17', 'X21', 'X22', 'X26', 'X32',
                          'X38', 'X40', 'X43', 'X45', 'X48',
                          'X52', 'X55']

        dat = None
        with open(datafile, 'rb') as csvfile:
            oxy_reader = csv.DictReader(csvfile)
            dat = [ rescale(line, rev_list, non_zero_medians) 
                for line in oxy_reader ]
        return dat
                
    def score(dat):
        def calculate_awr(line):
            question_set = ['X2', 'X7', 'X25', 'X32', 'X45',
                            'X52', 'X54', 'X56']
            return row_select_reduce(line, question_set)
            

        def calculate_cog(line):
            question_set = ['X5', 'X10', 'X15', 'X17', 'X30',
                            'X40', 'X42', 'X44', 'X48', 'X58',
                            'X59', 'X62']
            return row_select_reduce(line, question_set)

        def calculate_com(line):
            question_set = ['X12', 'X13', 'X16', 'X18', 'X19',
                            'X21', 'X22', 'X26', 'X33', 'X35',
                            'X36', 'X37', 'X38', 'X41', 'X46',
                            'X47','X51','X53','X55','X57','X60',
                            'X61']
            return row_select_reduce(line, question_set)


        def calculate_mot(line):
            question_set = ['X1', 'X3', 'X6', 'X9', 'X11', 'X23',
                            'X27', 'X34', 'X43', 'X64']
            return row_select_reduce(line, question_set)


        def calculate_rrb(line):
            question_set = ['X4', 'X8', 'X14', 'X20', 'X24', 'X28',
                            'X29', 'X31', 'X39', 'X49', 'X50', 'X63']
            return row_select_reduce(line, question_set)


        def calculate_sci(line):
           return line['awr'] + line['cog'] + line['com'] + line['mot']

        def calculate_srs2(line):
            return line['sci'] + line['rrb']

        aggregated_dat = []
        for line in dat:
            calculated_dat = {
                    'id'   : line['Participant.ID'],
                    'awr'  : calculate_awr(line),
                    'cog'  : calculate_cog(line),
                    'com'  : calculate_com(line),
                    'mot'  : calculate_mot(line),
                    'rrb'  : calculate_rrb(line),
                    'sci'  : None,
                    'srs2' : None
                }
            calculated_dat['sci']  = calculate_sci(calculated_dat)
            calculated_dat['srs2'] = calculate_srs2(calculated_dat)
            aggregated_dat.append(calculated_dat)
        return aggregated_dat

    dat = rescale_dat(datafile)
    scored_dat = score(dat)
    return scored_dat

def write_to_csv(datafile, outputfile):
    dat = score(datafile)
    header = OrderedDict([('id', None), ('awr',None), ('cog',None), 
        ('com',None),  ('mot',None), ('rrb',None), 
        ('sci', None), ('srs2',None)])
    with open(outputfile, 'wb') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)
        csv_writer.writeheader()
        for row in dat:
            csv_writer.writerow(row)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('datafile', 
        help="The relative path from the root directory \
         to the file you want to process")
    parser.add_argument('outputfile', 
        help="The relative path from the root directory \
         to the output file")
    args = parser.parse_args()
    write_to_csv(args.datafile, args.outputfile)

if __name__ == "__main__":
    run()