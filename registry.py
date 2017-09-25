from smtplib import SMTP
from config import sdaf, sender_email


# function to take attendee details (and whether we like them or not)
def take_details():
    username = input('Name: ')
    contact = input('Email: ')
    status = input('Status: like/dislike ')
    print('')
    return username, contact, status


# search by name though email list and return email
def get_email(search_term, l):
    for u in l:
        if search_term == u['name']:
            return u['email']


# send email function
def send_email(email_address, msg):
    with SMTP('smtp.gmail.com', 587) as s:
        try:
            s.starttls()
            s.login(sender_email, sdaf)
            s.sendmail(sender_email, email_address, msg)
            print('sent!')
        except Exception as err:
            print('sending failed: ', err)


details = {}
details_list = []

# register attendees
while True:
    take_details_ = input('Take details? y/n ')
    print('')
    if take_details_ == 'y':
        details_ = take_details()
        details['name'], details['email'], details['status'] = details_[0], details_[1], details_[2]
        details_list.append(details)
        details = {}
    else:
        print('Thank you for your time, now you can search for emails by name.\n')
        break

# search for attendees email by name
while True:
    name = input('Name of contact: ')
    if name == '':
        break
    email = get_email(name, details_list)
    print('{}\'s contact is {}\n'.format(name, email))


# based on whether we like the attendee or not, send a personalized email
for user in details_list:
    if user['status'] == 'like':
        send_email(user['email'], 'Hi {}!\n\nThanks for coming, we\'ll keep in touch :)'.format(user['name']))
    else:
        send_email(user['email'], 'Hi {}!\n\nThanks for coming.'.format(user['name']))
