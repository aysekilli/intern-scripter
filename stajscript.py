name = input("Enter your name and surname: ")
department = input("Enter your department: ")
year = input("Enter your year of study (e.g. 1, 2, 3, etc.): ")
interests = input("Enter your interests: ")
company = input("Enter the company you are applying to: ")
uni = input("Enter your university: ")
days = input("Enter the minimum number of days for your internship: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

text = (
    f"I am a {year} year student at {uni}, Department of {department}.\n"
    f"I would like to do a summer internship in your company {company}, to improve myself in the field of software.\n"
    f"I am particularly interested in {interests} and have gained basic knowledge in these areas.\n"
    f"I am eager to learn like many other students, enjoy researching, and can adapt well to teamwork.\n"
    f"My obligatory internship duration is at least {days} working days.\n"
    f"I would be very excited and pleased to learn from you if I could have the opportunity to improve myself in the dynamic structure of your company.\n"
    f"I'm sharing the necessary documents and my CV in the attached file for you to view.\n"
    f"Thank you a lot in advance for your attention.\n"
    "Stay with technology,\n"
    f"{name}\n"
    f"{department} Student\n"
    f"{uni}\n"
    f"Phone number: {phone}\n"
    f"Email: {email}"
)

print(text)
print("By the way, I actually took help from my own Python codes to create this internship application script. It is below with the files.")

with open("internship_application.txt", "w") as file:
    file.write(text)