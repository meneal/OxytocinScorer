def rescale(row, rev_list, non_zero_medians):
    reverse_likert_score = [3,2,1,0]

    row = { question: int(row[question]) 
            if isinstance(row[question], basestring)
            and row[question] != 'BLANK' 
            and question != 'Participant.ID'
            else row[question]
            for (question,score) in row.iteritems() }

    row = { question: row[question] - 1 
            if row[question] != 'BLANK' 
            and question != 'Participant.ID'
            else row[question]
            for (question, score) in row.iteritems() }    

    for question, score in row.iteritems():
        if question in rev_list and row[question] != 'BLANK':
            row[question] = reverse_likert_score[score]

    for question, score in row.iteritems():
        if score == 'BLANK':
            if question in non_zero_medians:
                row[question] = 1
            else:
                row[question] = 0
    return row


def row_select_reduce(row, question_set):
    targets = [ score if question in question_set else 0
                for (question, score) in row.iteritems() ]
    return reduce(lambda score_1, score_2: score_1 + score_2, targets)
        
