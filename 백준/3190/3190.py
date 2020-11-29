import pprint

# code of status
WALL = -1
BODY = 4
APPLE = 9 
PATH = 0

# movements
RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)

class Board :
    # status : 벽, 뱀의 몸, 사과
    def __init__(self, row, column, status) :
        self.row = row
        self.column = column
        self.status = status

class Snake :
    def __init__(self) :
        # body의 마지막 번째가 꼬리
        # pop 함수를 이용하여 꼬리를 이동시키고 좌표를 body의 맨 앞에 추가하여 머리를 늘린다.
        self.body = [[1,1]]
        self.length = len(self.body)
        self.dir = RIGHT

    def move(self, movements, board) :
        all_time = 0
        # all_time_save = all_time
        while True :
            all_time += 1
            try :
                direction = movements[all_time-1]
                # 왼쪽 회전
                if direction == 'L' :
                    if self.dir == RIGHT :
                        self.dir = UP
                    elif self.dir == UP :
                        self.dir = LEFT
                    elif self.dir == LEFT :
                        self.dir = DOWN
                    elif self.dir == DOWN :
                        self.dir = RIGHT
                # 오른쪽 회전
                elif direction == 'D' :
                    if self.dir == RIGHT :
                        self.dir = DOWN
                    elif self.dir == DOWN :
                        self.dir = LEFT
                    elif self.dir == LEFT :
                        self.dir = UP
                    elif self.dir == UP :
                        self.dir = RIGHT
                head = self.body[self.length-1]
                next_head = [head[0] + self.dir[0], head[1] + self.dir[1]]
                self.body.insert(0,next_head)

                # print("****************", all_time, "******************")
                # print(direction, self.dir)
                # 아무 것도 없는 경우
                if board[self.body[0][0]][self.body[0][1]].status == PATH :
                    tail = self.body.pop()
                    board[tail[0]][tail[1]].status = PATH
                    board[self.body[0][0]][self.body[0][1]].status = BODY
                # 사과가 있는 경우
                elif board[self.body[0][0]][self.body[0][1]].status == APPLE :
                    board[self.body[0][0]][self.body[0][1]].status = BODY
                # 머리의 위치가 벽이거나 몸일 때
                elif board[self.body[0][0]][self.body[0][1]].status == WALL or board[self.body[0][0]][self.body[0][1]].status == BODY :
                    return all_time
                # status_list(board)
            except KeyError :
                head = self.body[self.length-1]
                next_head = [head[0] + self.dir[0], head[1] + self.dir[1]]
                self.body.insert(0,next_head)

                # print("****************", all_time, "******************")
                # print(self.dir)
                # 아무 것도 없는 경우
                if board[self.body[0][0]][self.body[0][1]].status == PATH :
                    tail = self.body.pop()
                    board[tail[0]][tail[1]].status = PATH
                    board[self.body[0][0]][self.body[0][1]].status = BODY
                # 사과가 있는 경우
                elif board[self.body[0][0]][self.body[0][1]].status == APPLE :
                    board[self.body[0][0]][self.body[0][1]].status = BODY
                # 머리의 위치가 벽이거나 몸일 때
                elif board[self.body[0][0]][self.body[0][1]].status == WALL or board[self.body[0][0]][self.body[0][1]].status == BODY :
                    return all_time
                # status_list(board)

# print board
def status_list(board) :
    board_status = []
    for i in range(len(board)) :
        row = []
        for j in range(len(board)) :
            row.append(board[i][j].status)
        board_status.append(row)
    pprint.pprint(board_status)

if __name__ == "__main__" :
    # N intializing : board size 2<= N <= 100
    N = int(input())
    # board initializing
    board = [[0]*(N+2) for _ in range(N+2)]

    # snake location initializing
    board[1][1] = Board(1, 1, BODY)
    for row in range(N+2) :
        for column in range(N+2) :
            if row == 0 :
                board[row][column] = Board(row, column, WALL)
            elif row == N+1 :
                board[row][column] = Board(row, column, WALL)
            elif column == 0 :
                board[row][column] = Board(row, column, WALL)
            elif column==N+1 :
                board[row][column] = Board(row, column, WALL)
            else :
                board[row][column] = Board(row, column, PATH)

    # K initializing : number of apples 0<= K <= 100
    K = int(input())
    # save apple location to board
    for k in range(K) :
        apple_loc = input()
        apple_loc = apple_loc.split(' ')
        row = int(apple_loc[0])
        column = int(apple_loc[1])
        board[row][column] = Board(row, column, APPLE)
        
    # L initializing : number of movements of snake 1<= L <= 100
    L = int(input())
    # save movements of snake
    movements = {}
    for l in range(L) :
        m = input()
        m = m.split(' ')
        movements[int(m[0])] = m[1]
    
    
    # snake initializing
    anaconda = Snake()
    # board initializing with snake's location
    board[1][1] = Board(1, 1, BODY)
    # status_list(board)
    print(anaconda.move(movements, board))

    



    
    