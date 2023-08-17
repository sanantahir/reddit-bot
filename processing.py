list_of_flairs_to_check = ['[Patron]', '[HIRING]', 'Hiring', "[HIRING]-one-off", "[HIRING]-project", "Artist Needed", 'Paid', "Paid Request", ]

list_to_parse_title = ['[HIRING]', '[Hiring]', '[hirng]',]

list_to_process_submission = list_of_flairs_to_check + list_to_parse_title

notify = []


def processing(submission):
    for checker in list_to_process_submission:
        if submission.link_flair_text:
            if checker.lower() in submission.title.lower() or checker.lower() == submission.link_flair_text.lower():
                return submission
        else: 
            if checker.lower() in submission.title.lower():
                return submission
