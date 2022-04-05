import shutil
import psutil
import socket
import emails

sender = 'automation@example.com'
recipient = 'username@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'

def cpu():
    percent = psutil.cpu_percent(1)
    if percent > 80:
        subject = "Error - CPU usage is over 80%"
        report = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(report)
def disk_usage():
    du = shutil.disk_usage('/')
    print(du.free/du.total)
    if du.free/du.total < 0.20:
        subject = "Error - Available disk space is less than 20%"
        report = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(report)
def memory():
    ram = psutil.virtual_memory()
    print(ram.free/1024)
    if ram.free/1024 < 500:
        subject = "Error - Available memory is less than 500MB"
        report = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(report)

def socket_check():
    localhost = socket.gethostbyname('localhost')
    print(localhost)
    if localhost != '127.0.0.1':
        ubject = "Error - localhost cannot be resolved to 127.0.0.1"
        report = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(report)

disk_usage()
cpu()
memory()
socket_check()
