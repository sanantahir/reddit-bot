from praw_auth import reddit
import processing
import mail_sender 
import time
from communities_and_meta import subs_and_meta_info

list_of_subreddits_to_listen_to = ['artcommission', 'artcommissions', 'commissions', 'hireanartist', 'HungryArtists', 'inat', 'ComicBookCollabs', '3Drequests']


list_of_recipients = ["maliksanan28@gmail.com"]

# "jesterpk870@gmail.com"

list_of_notified_submission = []

while True:
    print("here")
    for sub in subs_and_meta_info.keys():
        try:
            submissions = reddit.subreddit(sub).new(limit = 200)
            print(f"Got New Submissions from {sub}")
        except:
            continue
        for submission in submissions:
            processed_submission = processing.processing(submission, sub)
            if processed_submission is not None and processed_submission not in list_of_notified_submission:
                print("Submission Found")
                subject = f"Someone in {processed_submission.subreddit.display_name} wants to hire an artist!"
                body = f"""
                Title: {submission.title}
                flair: {submission.link_flair_text}
                URL: https://www.reddit.com{submission.permalink}
                """
                mail_sender.the_mail.send(list_of_recipients, subject, body)
                print("Mail Sent")
                list_of_notified_submission.append(submission)
            else:
                pass
    
    time.sleep(50)