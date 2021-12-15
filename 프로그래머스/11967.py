
def turn_on(rooms, switches, x, y) :
    swt_room = switches[(x,y)]
    for switch in swt_room :
        rooms[switch[0]][switch[1]] = 1
    return rooms


def search(rooms, switches, x, y, N, room_check) :
    swt_keys = switches.keys()
    if (x, y) in swt_keys :
        rooms = turn_on(rooms, switches, x, y)
    room_check.append((x,y))
    print(room_check)
    print(rooms)
    print('------------------------------------------------------')
    # 우
    if y < N and rooms[x][y+1] == 1 and (x,y+1) not in swt_keys :
        print('우')
        search(rooms, switches, x, y+1, N, room_check)
    # 하
    if x < N and rooms[x+1][y] == 1 and (x+1,y) not in swt_keys :
        print('하')
        search(rooms, switches, x+1, y, N, room_check)
    # 좌
    if y > 0 and rooms[x][y-1] == 1 and (x,y-1) not in swt_keys :
        print('좌')
        search(rooms, switches, x, y-1, N, room_check)
    # 상
    if x > 0 and rooms[x-1][y] == 1 and (x-1,y) not in swt_keys :
        print('상')
        search(rooms, switches, x-1, y, N, room_check)  

    return rooms


def main() :
    N_M = input().split(' ')
    N = int(N_M[0])
    M = int(N_M[1])
    rooms = [[0 for col in range(N)] for row in range(N)]
    switches = dict()
    for m in range(M) :
        xy_ab = input().split(' ')
        switches_keys = switches.keys()
        xy = (int(xy_ab[0])-1, int(xy_ab[1])-1)
        if xy in switches_keys :
            switches[xy].append((int(xy_ab[2])-1, int(xy_ab[3])-1))
        else :
            switches[xy] = [(int(xy_ab[2])-1, int(xy_ab[3])-1)]
    print(switches) 
    rooms[0][0] = 1

    room_check = []
    search(rooms, switches, 0, 0, N, room_check)

    print(rooms)

main()