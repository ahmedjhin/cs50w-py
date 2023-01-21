class players:
    def __init__(self, rank, name):
        self.rank = rank
        self.name = name


    def rankabrove(self):
        if self.rank < 20:
            print(f"{self.name} you are trash")
        else:
            print(f"{self.name} you are in ")




player1 = players(13,"s3don")
player2 = players(29,"ahmed")
player1.rankabrove()
player2.rankabrove()
