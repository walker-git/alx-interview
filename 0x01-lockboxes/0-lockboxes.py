#!/usr/bin/python3

def canUnlockAll(boxes):
    # Implementation of the canUnlockAll function
    # ...

# Test cases
if __name__ == '__main__':
    # Test case 1
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    # Test case 2
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    # Test case 3
    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

