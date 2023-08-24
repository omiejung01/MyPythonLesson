

def swap(list):
    #number of swapping
    n = 0
    #use index
    size = len(list)
    counter = 0
    while counter < (size - 1):
        #print (list[counter+1])
        if list[counter] > list[counter+1]:
            #swap
            temp = list[counter + 1]
            list[counter + 1] = list[counter]
            list[counter] = temp
            n += 1
            #print(list)
        counter += 1
    return n

def sort(list):
    n = swap(list)
    print(list)
    while int(n) > 0:
        n = swap(list)
        print(list)


def temp():
    list1 = [6,5,7,8,9,3,4]
    print(list1)
    sort(list1)
    #print(list1)
