p1_a = [0, 0, 0]
p1_b = [0, 0, 0]
p1_c = [0, 0, 0]

def check_result(l1:list, l2:list, l3:list):
    # 4 cases to win:
    # - if an array has only 1s
    if 0 not in (l1 or l2 or l3):
        print('Win')

    # - if all arrays have 1 at the same index
    for i in range(2):
        if (l1[i] and l2[i] and l3[i]) == 1:
            print('Win')

    # - if the arrays have 1 at n+1 or n-1 index
    if l2[1] == 1 and (l1[0] == 1 and l3[2]) == 1 or (l1[2] == 1 and l3[0]):
        print('Win')

check_result(l1=[1,1,0],
             l2=[1,1,0],
             l3=[0,0,1])