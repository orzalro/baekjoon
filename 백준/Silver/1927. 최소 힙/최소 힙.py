import sys

input = sys.stdin.readline

n = int(input())
heap = []


def up(index):
    if index > 0:
        parent = (index - 1) // 2
        if heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            up(parent)


def down(index):
    child = 2 * index + 1
    smallest = index
    if child < len(heap) and heap[child] < heap[smallest]:
        smallest = child
    if child + 1 < len(heap) and heap[child + 1] < heap[smallest]:
        smallest = child + 1
    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        down(smallest)


for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) > 0:
            print(heap[0])
            temp = heap.pop()
            if len(heap) != 0:
                heap[0] = temp
                down(0)
        else:
            print(0)
    else:
        heap.append(x)
        up(len(heap) - 1)