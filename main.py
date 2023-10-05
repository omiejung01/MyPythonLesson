def serial_sum(m, n = None):
    sum = 0
    if n is None:
        for x in range(m+1):
            sum += x
    else:
        for x in range(m,n+1):
            sum += x
    return sum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(serial_sum(5))
    print(serial_sum(2,5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
