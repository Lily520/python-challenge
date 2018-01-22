#23 this，string模块

import this
import string

if __name__ == "__main__":

    input = "va gur snpr bs jung"

    From = string.ascii_lowercase
    To = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]

    str = str.maketrans(From,To)

    result = input.translate(str)
    print(result) #in the face of what

    #import this 后的一句输出是：In the face of ambiguity
    ## 答案：ambiguity 