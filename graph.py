import linked_list
import pqheap as Queue
import stack

class Vertex:

    def __init__(self, name):
        self.__name = name
        self.__flag = 'U'  # 'U' means Unvisited, 'V' means Visited, 'W' means Waiting

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_unvisited(self):
        self.__flag = 'U'

    def set_waiting(self):
        self.__flag = 'W'

    def set_visited(self):
        self.__flag = 'V'

    def is_unvisited(self):
        return self.__flag == 'U'


class Graph:

    def __init__(self, numVs):
        self.__vertices = [None]*numVs
        for i in range(numVs):
            self.__vertices[i] = Vertex('')

        self.__edge_list = [None]*numVs
        for i in range(numVs):
            self.__edge_list[i] = linked_list.LinkedList()

    # this adds an undirected edge
    # for unweighted edges, store a tuple of one value (the adjacent vertex)
    def add_edge(self, v1, v2):
        self.__edge_list[v1].add_to_beginning((v2,))
        self.__edge_list[v2].add_to_beginning((v1,))

    # for unweighted edges, store a tuple of one value (the adjacent vertex)
    def add_directed_edge(self, fromV, toV):
        self.__edge_list[fromV].add_to_beginning((toV,))

    # for weighted edges, store a tuple of 2 values (the adjacent vertex, the weight)
    def add_weighted_edge(self, v1, v2, weight):
        self.__edge_list[v1].add_to_beginning((v2,weight))
        self.__edge_list[v2].add_to_beginning((v1,weight))

    # for weighted edges, store a tuple of 2 values (the adjacent vertex, the weight)
    def add_weighted_directed_edge(self, fromV, toV,weight):
        self.__edge_list[fromV].add_to_beginning((toV,weight))

    def set_vertex_name(self, vNum, name):
        self.__vertices[vNum].set_name(name)

    # the edge list stores tuples, the [0]th element of the tuple is the
    # vertex number
    def dfs(self, startV):

        visited = ''
        # mark all vertices as unvisited
        for i in range(len(self.__vertices)):
            self.__vertices[i].set_unvisited()

        st = stack.stack()
        st.push(startV)
        visited += '(' + str(startV) + ')' + self.__vertices[startV].get_name() + ', '
        self.__vertices[startV].set_visited()

        while not st.is_empty():
            peekV = st.peek()
            temp = self.__edge_list[peekV].head
            while temp != None:
                # temp.data is one of the adjacent vertices to dqV
                if self.__vertices[temp.data[0]].is_unvisited():
                    st.push(temp.data[0])
                    visited += '(' + str(temp.data[0]) + ')' + self.__vertices[temp.data[0]].get_name() + ', '
                    self.__vertices[temp.data[0]].set_visited()
                    break
                else:
                    temp = temp.next
            if temp == None:  # means we didn't get an adjacent, unvisited vertex to peekV
                st.pop()

        return visited
    

    # the edge list stores tuples, the [0]th element of the tuple is the
    # vertex number
    def bfs(self, startV):
        visited = ''
        q = Queue.Queue()

        # mark all vertices as unvisited
        for i in range(len(self.__vertices)):
            self.__vertices[i].set_unvisited()

        q.enqueue(startV)
        self.__vertices[startV].set_waiting()

        while not q.is_empty():
            dqV = q.dequeue()
            visited += str(dqV) + self.__vertices[dqV].get_name() + ','
            self.__vertices[dqV].set_visited()

            # enqueues all the unvisited adjacent vertices to dqV
            temp = self.__edge_list[dqV].head
            while temp != None:
                # temp.data is one of the adjacent vertices to dqV
                if self.__vertices[temp.data[0]].is_unvisited():
                    q.enqueue(temp.data[0])
                    self.__vertices[temp.data[0]].set_waiting()
                temp = temp.next

        return visited
