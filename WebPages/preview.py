from WebPages.templates import *


def preview(x: classmethod):
    temp = Templates(x)
    return temp.template_one()

