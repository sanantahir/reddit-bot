from praw_auth import reddit
import processing
import mail_sender 
import time

list_of_subreddits_to_listen_to = ['artcommission', 'artcommissions', 'commissions', 'hireanartist', 'HungryArtists', 'inat', 'ComicBookCollabs']

list_of_recipients = ["maliksanan28@gmail.com", "jesterpk870@gmail.com"]

list_of_notified_submission = []

while True:

    for sub in list_of_subreddits_to_listen_to:
        try:
            submissions = reddit.subreddit(sub).new(limit = 30)
            print("Got New Submissions")
        except:
            continue
        for submission in submissions:
            processed_submission = processing.processing(submission)
            if processed_submission is not None and processed_submission not in list_of_notified_submission:
                print("Submission Found")
                subject = f"Someone in {processed_submission.subreddit.display_name} wants to hire an artist!"
                body = f"""
                Title: {submission.title}
                URL: https://www.reddit.com{submission.permalink}
                """
                mail_sender.the_mail.send(list_of_recipients, subject, body)
                print("Mail Sent")
                list_of_notified_submission.append(submission)
            else:
                print("No one want to hire an artist in this sub")
    
    time.sleep(50)