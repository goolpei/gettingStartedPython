class Hanoi:
    def __init__(self, total_disks):
        self.total_disks = total_disks
        self.structure = [[x for x in range(total_disks, 0, -1)],[],[]]
        # [[5, 4, 3, 2, 1], [], []]

    def transfer_disk(self, col_from: int, col_to: int): 

        if col_from not in (1,2,3) or col_to not in (1,2,3):
            raise ValueError('Only 1, 2, and 3 columns')

        # so that the list can understand
        col_from -= 1
        col_to -= 1

        # can only transfer disks at the top, can't transfer larger disks on top of smaller disks
        if not self.structure[col_from]:
            raise ValueError('Column from is empty')

        if not self.structure[col_to]:
            self.structure[col_to].append(self.structure[col_from][-1])
            del self.structure[col_from][-1]
            return

        if self.structure[col_to][-1] > self.structure[col_from][-1]:
            self.structure[col_to].append(self.structure[col_from][-1])
            del self.structure[col_from][-1]
        else:
            raise ValueError("Can't transfer larger disks on top of smaller disks")

    def valid_move_not_involving_disk1(self):
        no_disk1 = []
        for i, col in enumerate(self.structure, 1):
            if 1 not in col: no_disk1.append(i)

        try:
            self.transfer_disk(no_disk1[0], no_disk1[1])
        except ValueError:
            self.transfer_disk(no_disk1[1], no_disk1[0])

        

def hanoi_solver(total_disks: int) -> str:

    hanoi = Hanoi(total_disks)
    result = []
    result.append(' '.join(map(str, hanoi.structure)))

    is_even = total_disks % 2 == 0
    
    if is_even: 
        i = 1
        j = 2
    else: 
        i = 1
        j = 3

    total_moves = (2**total_disks) - 1
    current_moves = 0

    while True:

        if current_moves >= total_moves: break
        hanoi.transfer_disk(i,j)
        current_moves += 1

        result.append(' '.join(list(map(str, hanoi.structure))))

        if current_moves >= total_moves: break
        hanoi.valid_move_not_involving_disk1()
        current_moves += 1

        result.append(' '.join(list(map(str, hanoi.structure))))

        if is_even:
            i += 1
            j += 1
            if i == 4: i = 1
            if j == 4: j = 1
        else:
            i -= 1
            j -= 1
            if i == 0: i = 3
            if j == 0: j = 3

    return '\n'.join(result)



print(hanoi_solver(5))
