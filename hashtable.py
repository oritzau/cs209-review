# quadratic probing
# hash function to do product of (character + position)
# we are going to enter 2190 words so table_size = 4451 (this is prime and at least 2* the number of elements I will add)


class hash_table:

    def __init__(self, table_size):
        self.__table = [None]*table_size


    def __hash_function(self, word):
        #ord(word[0])*(ord(word[1])+1)*
        # (ord(word[2])+2)* ... * (ord(word[len(word)-1]) +len(word)-1)

        # have to % by len(self.__table)
        # and return that value (the hash value of word)

        hash_value = 1
        for i in range(len(word)):
            hash_value = hash_value * (ord(word[i]) + i)

        return hash_value % len(self.__table)

    def __hash_function_java(self, word):
        power = len(word)-1
        hash_val = 0
        for char in word:
            hash_val += ord(char)*(31 ** power)
            power -= 1

        return hash_val % len(self.__table)
    
    def insert(self, word):
        orighv = self.__hash_function(word)
        collision_count = 0
        hv = orighv
        quadratic_value = 1
        while True:
            if self.__table[hv] == None:
                self.__table[hv] = word
                return collision_count
                #break
            elif self.__table[hv] == word:
                break # we won't add duplicate words
            else:
                # collision
                collision_count += 1
                hv = orighv + (quadratic_value * quadratic_value)
                hv = hv % len(self.__table)
                quadratic_value += 1
                

    def search(self, word):
        orighv = self.__hash_function(word)

        hv = orighv
        quadratic_value = 1
        while True:
            if self.__table[hv] == None:
                return False
            elif self.__table[hv] == word:
                return True
            else:
                # collision
                hv = orighv + (quadratic_value * quadratic_value)
                hv = hv % len(self.__table)
                quadratic_value += 1
