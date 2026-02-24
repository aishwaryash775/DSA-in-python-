password = "abcdbdcd"
print(password.isalpha())  

#output
#true 


password = "123"
print(password.isdigit())
#output
#true

password = "abc123"
print(password.isalnum()) #means alphanumeric
#output
#true

password = "abctt"
print(password.islower())
#output
#true
password = "ABCTT"
print(password.isupper())
#output
#true

password = "aaavvvva"
print(password.lower())
#output
#aaavvvva

password = "hbhvhbhjh"
print(password.upper())
#output
#HBHVHBHJH