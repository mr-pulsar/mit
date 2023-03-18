import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopeywiueuzxc"
number="0123456789"
symbols="!@#$%^&*()-=+_"

string=upper+lower+number+symbols
length=16
string="".join(random.sample(string,length))
print(string)