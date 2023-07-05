#!/usr/bin/python3

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)

