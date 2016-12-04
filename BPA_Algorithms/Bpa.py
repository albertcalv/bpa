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


    def sort_list(self, list_t):
        list_sorted = sorted(list_t, key=lambda tup: tup[1], reverse=True)
        return list_sorted


    def scoring_function(self, set_of_tuples):
        suma=0
        for ttuple in set_of_tuples:
            suma += ttuple[1]
        return suma


    def fa_algorithm(self, set_of_lists, k=-1):
        # Check data
        self.check_size_of_lists(set_of_lists)
        self.check_lenght_of_lists(set_of_lists)

        len_list = len(set_of_lists[0])
        if k == -1 or k > len_list :
            k = len_list

        # Sort the lists
        set_of_lists = self.sort_lists(set_of_lists)

        # FA Algorithm
        score = {}
        len_set_of_list = len(set_of_lists)
        for i in range(0, len_set_of_list-1):
            for j in range(0, len_set_of_list):
                sample = set_of_lists[i][j]
                if sample[0] not in score:
                    score[sample[0]] = sample[1]
                    if len(score) == k:
                        break
                else:
                    score[sample[0]] += sample[1]

        # Package into an array of tuples
        result = []
        for item, mean in score.items():
            result.append((item, mean/len_set_of_list))
            
        return result
