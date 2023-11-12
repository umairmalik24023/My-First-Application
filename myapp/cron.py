from blacklist.models import models


def refresh_black_ip():
    
    b= Blacklist(ip='127.168.1.3')
    b.save()