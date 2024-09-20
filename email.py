import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Set up your email credentials
email_address = ''
email_password = ''
# Email recipients list
recipients = [
]
# Email content
subject = 'Application for Data Scientist/ML Engineer Role'
body = '''
Dear Hiring Manager,

I am writing to express my interest in the Data Scientist/ML Engineer position at your esteemed organization. With a strong foundation in Artificial Intelligence and Data Science, complemented by hands-on experience in developing and deploying machine learning models, I am confident in my ability to contribute effectively to your team.

I hold a B.Tech in Artificial Intelligence and Data Science from St. Joseph’s College of Engineering, Chennai. My expertise includes deep learning, natural language processing, computer vision, and predictive analytics. I have proficiency in programming languages such as Python and R, along with experience in frameworks like TensorFlow, PyTorch, and scikit-learn. Additionally, I am familiar with deploying AI/ML solutions on Azure.

My strong analytical and problem-solving skills, combined with effective communication and teamwork abilities, make me well-suited for this role. I am particularly drawn to your organization’s commitment to innovation and excellence in research communication, and I am eager to leverage my skills to enhance operational efficiency, improve data accuracy, and drive business insights.

Thank you for considering my application. I look forward to the opportunity to discuss how my background, skills, and experiences can be of value to your team.

Best regards,

Dhanushkumar R
danushidk507@gmail.com
+91 9600917002

LinkedIn :  https://www.linkedin.com/in/dhanushkumar-r-datascience/

'''
# Attach resume (ensure the file path is correct)
filename = "Dhanush_kumar_Resume.pdf"
attachment_path = "Dhanush_kumar_Resume.pdf"

# Create the email message
def create_email(to_address):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach resume
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)

    return msg
  
import re
from PyPDF2 import PdfReader

# Function to extract email addresses from text
def extract_emails(text):
    # Improved regular expression to capture all email formats
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        # Extract text from each page and ensure no missing content
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# Path to your PDF file
pdf_path = 'Company Wise HR Contacts _ HR Contacts.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Extract emails and store them in a list
email_list = extract_emails(pdf_text)

# Remove duplicates if any
email_list = list(set(email_list))

# Print the total number of emails extracted and the list of emails
print(f"Total emails extracted: {len(email_list)}")
print(email_list)

# Send the email to all recipients
def send_emails():
    try:
        # Setup SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)

        # Send emails to each recipient
        for recipient in recipients:
            email_message = create_email(recipient).as_string()
            server.sendmail(email_address, email_list, email_message)
            print(f"Email sent to {recipient}")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")
# Call the function to send emails
send_emails()

