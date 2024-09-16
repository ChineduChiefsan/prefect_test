from prefect import task, flow

@task
def add_one(x: int):
    x+=1
    return x
list = []


@flow
def main():
    for x in [1, 2, 3]:
        first = add_one(x)
        print('returning first {}'.format(first))
        list.append(first)
        second = add_one(first)
        list.append(second)
        third = add_one(second)
        list.append(third)
        #print('returning second {}'.format(second))
        return list




if __name__=="__main__":
    main()