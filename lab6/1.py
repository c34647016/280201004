email = "ceng113@example.com"
your_email = input("email:")
your_email_l = your_email.lower()
your_email_l_parts = your_email_l.split("@")
removed_dots = your_email_l_parts[0].replace(".", "")
finale = removed_dots + "@" + your_email_l_parts[1]
print(finale == email)