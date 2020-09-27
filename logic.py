#password generetor
import string
import random



def passwordgen():

     s1 = string.ascii_uppercase
     s2 = string.ascii_lowercase
     s3 = string.digits
     #s4 = string.punctuation

     sample = []
     sample.extend(s1)
     sample.extend(s2)
     sample.extend(s3)
    # sample.extend(s4)

     passlen = int(input("Enter the length of password you want...\n"))

     random.shuffle(sample)

     passget = ("".join(sample[0:passlen]))

     print(passget)


passwordgen()
