""" Program-14 : Tower Of Hanoi """

def towerOfHanoi(n: int, src: str, dest: str, aux: str):
    if n == 1:
        print(f'Move top disk from {src} to {dest}')
    else:
        towerOfHanoi(n - 1, src, aux, dest)
        print(f'Move top disk from {src} to {dest}')
        towerOfHanoi(n - 1, aux, dest, src)

towerOfHanoi(4,'A','C','B')
