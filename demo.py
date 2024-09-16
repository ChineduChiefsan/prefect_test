import time
from time import time
from prefect import flow, task


@task
def add_numbers(e,f):
    #time.sleep(5)

    return e+f
@task
def muliply(x,y):
    #time.sleep(5)
    return  y*x

@flow
def calc(a,b):
    num_prod = muliply(a, b)
    num_sum = add_numbers(num_prod,b)

    return num_sum

if __name__=="__main__":
    print(calc(5,6))
