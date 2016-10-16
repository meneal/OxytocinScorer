import csv

non_zero_medians = {
    'X3'  : 1,
    'X7'  : 1,
    'X11' : 1,
    'X12' : 1,
    'X25' : 1,
    'X26' : 1,
    'X38' : 1,
    'X45' : 1,
    'X52' : 1,
    'X55' : 1
}

reverse_likert = ['X3', 'X7', 'X11', 'X12', 'X15',
                  'X17', 'X21', 'X22', 'X26', 'X32',
                  'X38', 'X40', 'X43', 'X45', 'X48',
                  'X52', 'X55']

with open('../dat/cleanDat.csv', 'rb') as csvfile:
    oxy_reader = csv.DictReader(csvfile)
    for line in oxy_reader:
        calculated_dat = {
                'id'   : line['Paticipant.ID'],
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
        
def calculate_awr(line):
    question_set = ['X2', 'X7', 'X25', 'X32', 'X45',
                    'X52', 'X54', 'X56']
    

def calculate_cog(line):
    question_set = ['X5', 'X10', 'X15', 'X17', 'X30',
                    'X40', 'X42', 'X44', 'X48', 'X58',
                    'X59', 'X62']


def calculate_com(line):
    question_set = ['X12', 'X13', 'X16', 'X18', 'X19',
                    'X21', 'X22', 'X26', 'X33', 'X35',
                    'X36', 'X37', 'X38', 'X41', 'X46',
                    'X47','X51','X53','X55','X57','X60',
                    'X61']


def calculate_mot(line):
    question_set = ['X1', 'X3', 'X6', 'X9', 'X11', 'X23',
                    'X27', 'X34', 'X43', 'X64']


def calculate_rrb(line):
    question_set = ['X4', 'X8', 'X14', 'X20', 'X24', 'X28',
                    'X29', 'X31', 'X39', 'X49', 'X50', 'X63']


def calculate_sci(line):
   return line['awr'] + line['cog'] + line['com'] + line['mot']

def calculate_srs2(line):
    return line['sci'] + line['rbb']



