
class PriorityQueue:
    def __init__(self, key):
        self.queue = []
        self.key = key

    def pop(self):
        elem = self.queue[0]
        last_elem = self.queue.pop()
        if len(self.queue) > 0:
            self.queue[0] = last_elem
            self._move_down_()
        return elem

    def add(self, elem):
        self.queue.append(elem)
        self._move_up_()

    def _move_down_(self):
        curId = 0
        while curId < len(self.queue):
            leftChildId = curId * 2 + 1
            rightChildId = curId * 2 + 2

            if leftChildId >= len(self.queue):
                break
            if rightChildId >= len(self.queue) or \
                    (rightChildId < len(self.queue)
                            and self.queue[leftChildId][self.key] < self.queue[rightChildId][self.key]):
                if self.queue[leftChildId][self.key] < self.queue[curId][self.key]:
                    # swap curId and leftChildId
                    tmp = self.queue[leftChildId]
                    self.queue[leftChildId] = self.queue[curId]
                    self.queue[curId] = tmp
                    curId = leftChildId
                else:
                    break
            else:
                if self.queue[rightChildId][self.key] < self.queue[curId][self.key]:
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
            if self.queue[fatherId][self.key] > self.queue[curId][self.key]:
                tmp = self.queue[fatherId]
                self.queue[fatherId] = self.queue[curId]
                self.queue[curId] = tmp
                curId = fatherId
            else:
                break

    def IsEmpty(self):
        return len(self.queue) == 0


