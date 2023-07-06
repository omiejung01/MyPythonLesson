
# Built-in
# Queue + Stack

from queue import Queue, LifoQueue

def run_q():
    # Initializing
    q = Queue(maxsize=3)

    q.put(11) # Python built-in use "put" for Enqueue
    q.put(12)
    q.put(13)

    if q.full():
        print("Full")
    else:
        print("Not full")

    print("Now, Dequeue the element out of Queue")

    print(q.get()) # Python built-in use "get" for Dequeue

    if q.full():
        print("Full")
    else:
        print("Not full")

    print(q.get())
    print(q.get())

    if q.empty():
        print("Empty")
    else:
        print("Not empty")

    print('Number of elements in a queue:' + str(q.qsize()))


def run_stack():
    # Initializing
    stack = LifoQueue(maxsize=3)
    stack.put(11) # Python built-in use "tut" for Push
    stack.put(12)
    stack.put(13)

    if stack.full():
        print("Full")
    else:
        print("Not full")

    print("Now, POP() the element out of Stack")

    print(stack.get()) # Python built-in use "Get" for Dequeue

    if stack.full():
        print("Full")
    else:
        print("Not full")

    print(stack.get())
    print(stack.get())

    if stack.empty():
        print("Empty")
    else:
        print("Not empty")

    print('Number of elements in a stack:' + str(stack.qsize()))

def run():
    #run_q()
    run_stack()


