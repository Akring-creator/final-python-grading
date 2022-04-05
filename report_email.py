import os
from datetime import date
import reports
import emails

today = date.today()
files = os.listdir('description')
attachment = 'processed.pdf'
def init_title(today):
    formatdate = today.strftime("%B %d, %Y")
    return "Processed Update on {}".format(formatdate)

def make_content(files):
    paragraph = "<br/>"
    for file in files:
        with open('description/'+file) as f:
            lines = f.readlines()
            line1 = lines[0].strip('\n')
            paragraph += 'nama ' + line1 + '<br/>'
            line2 = lines[1].strip('\n')
            paragraph += 'nama: ' + line2 + '<br/>'
            f.close()
        paragraph += '<br/>'
    return paragraph
content = make_content(files)
# content = "<br/>name = mangga<br/>berat = 200 kg<br/><br/>name = telur<br/>berat = 100 kg<br/>"
if __name__ == '__main__':
    title = init_title(today)
    reports.generate_report(attachment, content, title)
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    massage = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(massage)
