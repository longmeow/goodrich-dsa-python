from bai1_1 import *
from bai1_2 import *

def removeDups(first):
    if first is None:
        return None
 
    current = first
    while current.link:
        if current.data == current.link.data:
            linkNext = current.link.link
            current.link = linkNext
        else:
            current = current.next 
 
    return first

