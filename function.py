import string
from random import *

def generateAlphaNum(nbr):
    element = string.ascii_lowercase + string.digits
    tmp = sample(element, k=nbr)
    chaine = "".join(tmp)
    return chaine

def genarateAlphaNumMaj(nbr):
    element = string.digits + string.ascii_letters
    tmp = sample(element, k=nbr)
    chaine = "".join(tmp)
    return chaine

def generateAlphaNumSpe(nbr):
    element = string.digits + string.ascii_lowercase + "!#$&*-/_;:@?.,"
    tmp = sample(element, k=nbr)
    chaine = "".join(tmp)
    return chaine

def generateAll(nbr):
    element = string.ascii_letters + string.digits + "!#$&*-/_;:@?.,"
    tmp = sample(element, k=nbr)
    chaine = "".join(tmp)
    return chaine