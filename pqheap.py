
class ItemAndPriority:

    def __init__(self, item, priority):
        self.item = item
        self.pri = priority



class BinaryMaxHeap:

    # instance variable to be:
    # a python list (of ItemAndPriority)
    def __init__(self):
        self.__heap = []

    def is_empty(self):
        return len(self.__heap) == 0

    def __rci(self,i):
        return 2*i + 2

    def __lci(self,i):
        return 2*i + 1

    def __parenti(self,i):
        return (i - 1)//2

    def add(self, item, priority):
        unit = ItemAndPriority(item, priority)
        self.__heap.append(unit)

        # where did we put unit
        # in len(self.__heap) - 1 is where

        curri = len(self.__heap) - 1
        pari = self.__parenti(curri)

        while curri > 0:
            if self.__heap[curri].pri > self.__heap[pari].pri:
                # swap them
                temp = self.__heap[curri]
                self.__heap[curri] = self.__heap[pari]
                self.__heap[pari] = temp
                curri = pari
                pari = self.__parenti(curri)
            else:
                break

    def remove(self):
        thing_to_return = self.__heap[0]
        
        # get rid of the root
        # put last item in root
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop() # removes the last element, the one we just put in the root
        
        # downward reheapify
        lasti = len(self.__heap) - 1
        par_i = 0
        # we stop this loop if we get to a leaf
        # or when we don't swap a parent with a child (happens when parent is > both children)
        while True:
            if self.__lci(par_i) > lasti:
                # is a leaf and we're done
                break
            elif self.__rci(par_i) > lasti:
                # only has a left child
                if self.__heap[par_i].pri < \
                   self.__heap[self.__lci(par_i)].pri:
                    temp = self.__heap[par_i]
                    self.__heap[par_i] = \
                        self.__heap[self.__lci(par_i)]
                    self.__heap[self.__lci(par_i)] = temp
                    # update the idx for next iteration
                break
            elif self.__heap[self.__lci(par_i)].pri > \
               self.__heap[self.__rci(par_i)].pri:
                if self.__heap[par_i].pri < \
                   self.__heap[self.__lci(par_i)].pri:
                    temp = self.__heap[par_i]
                    self.__heap[par_i] = \
                        self.__heap[self.__lci(par_i)]
                    self.__heap[self.__lci(par_i)] = temp
                    # update the idx for next iteration
                    par_i = self.__lci(par_i)
                else:
                    break  # downward reheapify is done
            else:
                if self.__heap[par_i].pri < \
                   self.__heap[self.__rci(par_i)].pri:
                    # swap
                    temp = self.__heap[par_i]
                    self.__heap[par_i] = \
                        self.__heap[self.__rci(par_i)]
                    self.__heap[self.__rci(par_i)] = temp
                    # update the idx for next iteration
                    par_i = self.__rci(par_i)
                else:
                    break  # downward reheapify is done

        return thing_to_return



class PriorityQueue:

    def __init__(self):
        self.__thePQ = BinaryMaxHeap()

    def enqueue(self, item, priority):
        self.__thePQ.add(item, priority)

    def dequeue(self):
        return self.__thePQ.remove()

    def is_empty(self):
        return self.__thePQ.is_empty()


