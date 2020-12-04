# import pprint
class Dice :
    def __init__(self, x, y) :
        # 위치
        self.x = x
        self.y = y
        # 윗면
        self._1 = 0
        # 앞면
        self._2 = 0
        # 오른쪽 면
        self._3 = 0
        # 왼쪽 면
        self._4 = 0
        # 뒷면
        self._5 = 0
        # 아랫면
        self._6 = 0
    
    def east(self, maps) :
        # 주사위 면 변화
        save = [0, 0, 0, 0, 0, 0]
        save[0] = self._4
        save[1] = self._2
        save[2] = self._1
        save[3] = self._6
        save[4] = self._5
        save[5] = self._3

        self._1 = save[0]
        self._2 = save[1]
        self._3 = save[2]
        self._4 = save[3]
        self._5 = save[4]
        self._6 = save[5]

        # 주사위 이동
        self.y = self.y + 1

        if maps[self.x][self.y+1] == 0 :      
            # 주사위 바닥면 복사
            maps[self.x][self.y] = self._6

            print(self._1)

            return maps



        else :
            # 지도 칸 수 -> 주사위 바닥면 & 지도 칸 0으로 초기화
            self._6 = maps[self.x][self.y]
            maps[self.x][self.y] = 0

            print(self._1)

            return maps
        
    def west(self, maps) :
        # 주사위 면 변화
        save = [0, 0, 0, 0, 0, 0]
        save[0] = self._3
        save[1] = self._2
        save[2] = self._6
        save[3] = self._1
        save[4] = self._5
        save[5] = self._4

        self._1 = save[0]
        self._2 = save[1]
        self._3 = save[2]
        self._4 = save[3]
        self._5 = save[4]
        self._6 = save[5]

        # 주사위 이동
        self.y = self.y - 1

        if maps[self.x][self.y-1] == 0 :       
            # 주사위 바닥면 복사
            maps[self.x][self.y] = self._6

            print(self._1)

            return maps

        else :
            # 지도 칸 수 -> 주사위 바닥면 & 지도 칸 0으로 초기화
            self._6 = maps[self.x][self.y]
            maps[self.x][self.y] = 0

            print(self._1)

            return maps
    
    def north(self, maps) :
        # 주사위 면 변화
        save = [0, 0, 0, 0, 0, 0]
        save[0] = self._5
        save[1] = self._1
        save[2] = self._3
        save[3] = self._4
        save[4] = self._6
        save[5] = self._2

        self._1 = save[0]
        self._2 = save[1]
        self._3 = save[2]
        self._4 = save[3]
        self._5 = save[4]
        self._6 = save[5]

        # 주사위 이동
        self.x = self.x - 1
        
        if maps[self.x-1][self.y] == 0 :        
            # 주사위 바닥면 복사
            maps[self.x][self.y] = self._6

            print(self._1)

            return maps

        else :
            # 지도 칸 수 -> 주사위 바닥면 & 지도 칸 0으로 초기화
            self._6 = maps[self.x][self.y]
            maps[self.x][self.y] = 0

            print(self._1)

            return maps

    def south(self, maps) :
        # 주사위 면 변화
        save = [0, 0, 0, 0, 0, 0]
        save[0] = self._2
        save[1] = self._6
        save[2] = self._3
        save[3] = self._4
        save[4] = self._1
        save[5] = self._5

        self._1 = save[0]
        self._2 = save[1]
        self._3 = save[2]
        self._4 = save[3]
        self._5 = save[4]
        self._6 = save[5]

        # 주사위 이동
        self.x = self.x + 1  

        if maps[self.x+1][self.y] == 0 :
                   
            # 주사위 바닥면 복사
            maps[self.x][self.y] = self._6

            print(self._1)

            return maps

        else :
            # 지도 칸 수 -> 주사위 바닥면 & 지도 칸 0으로 초기화
            self._6 = maps[self.x][self.y]
            maps[self.x][self.y] = 0

            print(self._1)

            return maps


if __name__ == "__main__" :
    inputs = input().split(' ')
    inputs = [int(i) for i in inputs]
    # 세로
    N = inputs[0]
    # 가로
    M = inputs[1]
    # 주사위 좌표 x
    x = inputs[2]
    # 주사위 좌표 y
    y = inputs[3]
    # 명령 개수
    K = inputs[4]

    # 주사위 초기화
    dice = Dice(x, y)

    # 지도 초기화
    maps = []
    for n in range(N) :
        row = [int(i) for i in input().split(' ')]
        maps.append(row)
    
    # 명령
    orders = [int(o) for o in input().split(' ')]
    # pprint.pprint(maps)
    for order in orders :
        # print("dice loc : " + str(dice.x) + ", " + str(dice.y))
        # print("order : " + str(order))
        # 동(오른쪽)
        if order == 1 :
            if dice.y + 1 == M :
                continue
            else :
                maps = dice.east(maps)
        # 서(왼쪽)
        elif order == 2 :
            if dice.y - 1 == -1 :
                continue
            else :
                maps = dice.west(maps)
        # 북(위쪽)
        elif order == 3 :
            if dice.x - 1 == -1 :
                continue
            else :
                maps = dice.north(maps)

        # 남(아래쪽)
        elif order == 4 :
            if dice.x + 1 == N :
                continue
            else :
                maps = dice.south(maps)