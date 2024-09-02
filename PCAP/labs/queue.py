class QueueError(BaseException):  # Choose base class for the new exception.
    def error():
        return "Error: Tried to call get() on an empty list"


class Queue:
    def __init__(self):
        self.__q = []
        self.__length = 0

    def put(self, elem):
        self.__q.append(elem)
        self.__length += 1

    def get(self):
        if self.__length == 0:
            raise QueueError
        else:
            elem = self.__q[0]
            del self.__q[0]
            self.__length -= 1
            return elem


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return self._Queue__length == 0


# Test 1

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

# Test 2

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
