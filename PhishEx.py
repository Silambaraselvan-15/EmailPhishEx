import imaplib
import email
from email.header import decode_header

# to connect to the mail server

mail=imaplib.IMAP4_SSL("imap.gmail.com")
# give login credentials to login
mail.login("cyberdoclinux@gmail.com","kzen vsgx xucl xfas")
# select the inbox to read the mail in inbox
mail.select("inbox")
# get the emails
SearchStatus,message=mail.search(None,"ALL")
# get the email's id(no of email)
EmailsIds=message[0].split()
# to get the last email, use last index of emails_id
LastEmail=EmailsIds[-1]
# fetch the email data
fetch_status,MsgData=mail.fetch(LastEmail,"(RFC822)")
# parsing the email to get the data
RawEmailData=MsgData[0][1] #[0] for meta data
# the email content (subject)
# print("raw mail data:",RawEmailData)
Msg=email.message_from_bytes(RawEmailData)
# print("the message is :",Msg)
# to decode the header detail(subject) use decode_header function
subject,Encoded=decode_header(Msg["subject"])[0]
# print(Msg)
# print(Encoded)
if isinstance(subject,bytes): # to check whether it is in byte data type
    # To decode it with utf-8 if it is encoded
    subject=subject.decode(Encoded if Encoded else "utf-8") 
print("subject is :",subject) 

#Extracting the mail body (content)
if Msg.is_multipart(): # to check whether it has multiple part
    #if it has multiple parts , we should iterate through them
    for item in Msg.walk():
        # walk() function will iterate through the parts in the email like header,body,attachments....
        # to get the type of the content like plaintext or html or multipart
        ContentType=item.get_content_type()
        # to get the content-disposition (whether it is attached or inline)
        ContentDisposition=str(item.get("content-disposition"))

        if ContentType=="text/plain" and "attachement" not in ContentDisposition:
            # get_payload() with decode=True will decode the encoded content in bytes 
            # decode() will convert the decoded byte to string
            Body=item.get_payload(decode=True).decode()
            print("The body of the mail is: ",Body)
        elif ContentType=="text/html" and "attachement" not in ContentDisposition:
            Body=item.get_payload(decode=True).decode()
            # print("The body of the mail is: ",Body)
else:
    # well if it is not in multipart then we can decode it directly
    Body=Msg.get_payload(decode=True).decode()
    print("The body of the mail is: ",Body)
# to close the connection , use close() and logout()
# the From header contains the email addr and ip addr of the sender
FromHeader=Msg["From"]
if FromHeader:
    # the From header contains user name and email within " <> "
    # so split it and strip the <> of the last index 
    SenderEmail=FromHeader.split()[-1].strip("<>")
    print("the sender email id is: ",SenderEmail)
mail.close()
