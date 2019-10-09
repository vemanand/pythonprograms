'''
Program to accomplish mailmerge: Sending same email to multiple names/emails.
The message body is stored in one file - body.txt and names are stored in another - names.txt
This program will read both files and send e-mail to the listed addresses with different subject (based on name)
here, we don't actually send e-mails. Instead, store each message in a separate file
File operations: open(), read(), write(). strip() is used to remove any white spaces
'''

with open("../resources/names.txt", 'r', encoding='utf-8') as names_file:
    # open body.txt for reading
    with open("../resources/body.txt", 'r', encoding='utf-8') as body_file:
        # read entire content of the body
        body = body_file.read()
        # iterate over names
        for name in names_file:
            mail = "Hello " + name + body
            # write the mails to individual files
            with open(name.strip() + ".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)