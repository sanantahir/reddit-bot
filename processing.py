from communities_and_meta import subs_and_meta_info

# list_of_flairs_to_check = ['[Patron]', '[HIRING]', 'Hiring', "[HIRING]-one-off", "[HIRING]-project", "Artist Needed", 'Paid', "Paid Request", ]

# list_to_parse_title = ['[HIRING]', '[Hiring]', '[hirng]',]

# list_to_process_submission = list_of_flairs_to_check + list_to_parse_title


def processing(submission, sub):

    if submission.link_flair_text:
        for condition in subs_and_meta_info[sub]['flair']:
            if condition == submission.link_flair_text:
                return submission

    for cond in subs_and_meta_info[sub]['title']:
        if cond in submission.title: 
            return submission


