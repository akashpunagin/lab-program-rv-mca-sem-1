class Operator:
    lst = None
    def __init__(self):
        self.lst = []

    def get(self):
        is_error = True
        while is_error:
            try:
                size = int(input("Enter size of the list: "))
                is_error = False
                for index in range(size):
                    ele = None
                    while ( type(ele) != int ):
                        try:
                            ele = int(input(f"Enter element-{index + 1}: "))
                            self.lst.append(ele)
                        except:
                            print("Invalid element. Enter an integer\n")
            except:
                print("Invalid input for size. Try again\n")

    def __add__(self, other):
        res_lst = []
        zipped_lst = list(zip(self.lst, other.lst))
        for i, j in zipped_lst:
            _sum = i + j
            res_lst.append(_sum)
        print(res_lst)

    def __sub__(self, other):
        res_lst = []
        zipped_lst = list(zip(self.lst, other.lst))
        for i, j in zipped_lst:
            _diff = i - j
            res_lst.append(_diff)
        print(res_lst)

    def __mul__(self, other):
        res_lst = []
        zipped_lst = list(zip(self.lst, other.lst))
        for i, j in zipped_lst:
            _product = i * j
            res_lst.append(_product)
        print(res_lst)

    def __floordiv__(self, other):
        res_lst = []
        zipped_lst = list(zip(self.lst, other.lst))
        for i, j in zipped_lst:
            _division = i // j
            res_lst.append(_division)
        print(res_lst)
            
    def __pow__(self, other):
        res_lst = []
        zipped_lst = list(zip(self.lst, other.lst))
        for i, j in zipped_lst:
            _pow = i ** j
            res_lst.append(_pow)
        print(res_lst)
