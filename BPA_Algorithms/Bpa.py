class Bpa:

    def __init__(self):
        pass

    # Check data
    def check_size_of_lists(self, set_of_lists):
        try:
            if len(set_of_lists) < 2:
                raise NameError("Number of list < 2")
        except NameError:
            print("Error in Input data :(")
            raise

    def check_lenght_of_lists(self, set_of_lists):
        snitch = len(set_of_lists[0])
        for list_t in set_of_lists:
            try:
                if len(list_t) != snitch:
                    raise NameError("The lists are different size")
            except NameError:
                print("Error in Input data :(")


    def sort_lists(self, set_of_lists):
        set_of_lists_sorted = []
        for i, list_t in enumerate(set_of_lists):
            set_of_lists_sorted.append(sorted(list_t, key=lambda tup: tup[1], reverse=True))
        return set_of_lists_sorted


    def bpa_test(self, set_of_lists, k=-1):

        # Check data
        self.check_size_of_lists(set_of_lists)
        self.check_lenght_of_lists(set_of_lists)

        len_set_of_list = len(set_of_lists)
        len_list = len(set_of_lists[0])

        # If k is not set, k is equal to the size of the lists
        if k == -1 or k > len_list :
            k = len_list

        #Sort the lists
        set_of_lists = self.sort_lists(self, set_of_lists)

        #FA test
        score = []
        cuota = 0

        while cuota < k:

            for i in range(0, len_set_of_list):
                for j in range(0, len_list):
                    sample = set_of_lists[i][j][0]
                    #print (sample)

            cuota+=1
