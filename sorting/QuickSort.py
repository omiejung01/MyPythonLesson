#QuickSort of Int
#simplify version

def divide(list):
    # pivot is last element of a list

    if (len(list)==0):
        #print (' ')
        return ' '
    elif len(list) == 1:
        #print(list[0])
        return list[0]
    else:
        pivot = list[len(list)-1]
        left= []
        right =[]

        for x in list[0:len(list)-1]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)

        #print(left)
        #print(pivot)
        #print(right)
        return divide(left), pivot, divide(right)

