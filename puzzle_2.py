from collections import Counter


def checksum(box_ids):
    most_common_values = [dict(Counter(box_id).most_common(2)).values() for box_id in box_ids]
    count = lambda num: sum([num in values for values in most_common_values])

    return count(2) * count(3)


def most_common_ids(ids):
    while ids:
        id_1 = ids.pop()
        
        for id_2 in ids:
            answer = ''.join([char1 for char1, char2 in zip(id_1, id_2) if char1 == char2])
            
            if len(answer) == len(id_1) - 1:
                return answer


if __name__ == '__main__':
    with open('inputs/input_2.txt') as f:
        puzzle_input = [line.strip() for line in f.readlines()]
    
    # part 1
    assert checksum(puzzle_input) == 7105
    
    # part 2
    assert most_common_ids(['abcde',
                            'fghij',
                            'klmno',
                            'pqrst',
                            'fguij',
                            'axcye',
                            'wvxyz']) == 'fgij'
    assert most_common_ids(puzzle_input) == 'omlvgdokxfncvqyersasjziup'
