
class PriorityQueue:
    def __init__(self, key):
        self.queue = []
        self.key = key # TODO: change to key list (add a key indicating whether the current direction is the same as the previous one)
        self.storage = []

    def pop(self):
        elem = self.queue[0]
        last_elem = self.queue.pop()
        if len(self.queue) > 0:
            self.queue[0] = last_elem
            self._move_down_()
        self.storage.append(elem)
        return elem

    def clean(self):
        self.storage = []

    def add(self, elem):
        self.queue.append(elem)
        self._move_up_()

    def _compare_(self, elem1, elem2):
        for k in self.key:
            if elem1[k] < elem2[k]:
                return True
            elif elem1[k] > elem2[k]:
                return False
        return False

    def _move_down_(self):
        curId = 0
        while curId < len(self.queue):
            leftChildId = curId * 2 + 1
            rightChildId = curId * 2 + 2

            if leftChildId >= len(self.queue):
                break
            if rightChildId >= len(self.queue) or \
                    (rightChildId < len(self.queue)
                        and self._compare_(self.queue[leftChildId], self.queue[rightChildId])):
                if self._compare_(self.queue[leftChildId], self.queue[curId]):
                    # swap curId and leftChildId
                    tmp = self.queue[leftChildId]
                    self.queue[leftChildId] = self.queue[curId]
                    self.queue[curId] = tmp
                    curId = leftChildId
                else:
                    break
            else:
                if self._compare_(self.queue[rightChildId], self.queue[curId]):
                    # swap curId and rightChildId
                    tmp = self.queue[rightChildId]
                    self.queue[rightChildId] = self.queue[curId]
                    self.queue[curId] = tmp
                    curId = rightChildId
                else:
                    break

    def _move_up_(self):
        curId = len(self.queue) - 1
        while curId > 0:
            fatherId = (curId - 1) / 2
            if self._compare_(self.queue[curId], self.queue[fatherId]):
                tmp = self.queue[fatherId]
                self.queue[fatherId] = self.queue[curId]
                self.queue[curId] = tmp
                curId = fatherId
            else:
                break

    def IsEmpty(self):
        return len(self.queue) == 0


