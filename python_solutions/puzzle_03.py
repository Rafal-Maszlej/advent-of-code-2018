class Area:
    EMPTY_AREA = '.'
    INTERSECT_AREA = 'X'
    
    def __init__(self, size=1000):
        self.size = size
        self.board = self.get_empty_board()
        self.intact_claims = []
    
    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)
    
    def get_empty_board(self):
        return [[self.EMPTY_AREA] * self.size for _ in range(self.size)]
    
    def reset(self):
        self.board = self.get_empty_board()
        self.intact_claims = []

    def parse_claim(self, claim):
        return [int(i) for i in claim.lstrip('#')
                                     .replace(' @ ', ',')
                                     .replace(': ', ',')
                                     .replace('x', ',')
                                     .split(',')]
    
    def add_claim(self, claim):
        claim_id, x, y, width, height = self.parse_claim(claim)
        self.add_to_intact(claim_id)
        
        for h in range(y, y + height):
            for w in range(x, x + width):
                if self.board[h][w] != self.EMPTY_AREA:
                    self.remove_from_intact(self.board[h][w])
                    self.remove_from_intact(claim_id)
                    
                    self.board[h][w] = self.INTERSECT_AREA
                else:
                    self.board[h][w] = claim_id
    
    def fill_board(self, data):
        for claim in data:
            self.add_claim(claim)

    def get_intersection_size(self):
        return sum([row.count(self.INTERSECT_AREA) for row in self.board])
    
    def add_to_intact(self, claim_id):
        self.intact_claims.append(claim_id)
        
    def remove_from_intact(self, claim_id):
        if claim_id in self.intact_claims:
            self.intact_claims.remove(claim_id)


if __name__ == '__main__':
    # tests
    # part 1
    test_data = ['#1 @ 1,3: 4x4',
                 '#2 @ 3,1: 4x4',
                 '#3 @ 5,5: 2x2']
    area = Area()
    area.fill_board(test_data)
    
    assert area.get_intersection_size() == 4
    
    # part 2
    assert area.intact_claims == [3]
    
    area.reset()
    
    
    # puzzle solver
    # part 1
    with open('../inputs/input_3.txt') as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    area.fill_board(puzzle_input)
    
    assert area.get_intersection_size() == 113966
    
    # part 2
    assert area.intact_claims == [235]
