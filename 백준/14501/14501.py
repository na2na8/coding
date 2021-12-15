class Node :
    def __init__(self, parents, start, duration, end, reward, sum_reward) :
        self.parents = parents
        self.start = start
        self.duration = duration
        self.end = end
        self.reward = reward
        self.sum_reward = sum_reward
        self.Y = None
        self.N = None

def make_tree(N, T, P, node, reward_collection) :
    # Y
    y_start = node.end + 1
    # reward_collection에 추가
    # y_sum_reward = node.sum_reward + node.reward
    # reward_collection.append(y_sum_reward)
    if y_start <= N :
        y_duration = T[y_start-1]
        y_end = y_start + y_duration -1
        
        y_reward = P[y_start-1]
        y_sum_reward = node.sum_reward + node.reward
        # # reward_collection에 추가
        reward_collection.append(y_sum_reward)
        if y_end <= N :
            node.Y = Node(node, y_start, y_duration, y_end, y_reward, y_sum_reward)
            make_tree(N, T, P, node.Y, reward_collection)

        
    # N
    n_start = node.start + 1
    if n_start <= N :
        n_duration = T[n_start - 1]
        n_end = n_start + n_duration - 1
        n_reward = P[n_start-1]
        n_sum_reward = node.sum_reward
        if n_end <= N :
            node.N = Node(node, n_start, n_duration, n_end, n_reward, n_sum_reward)
            make_tree(N, T, P, node.N, reward_collection)


if __name__ == "__main__" :
    # 남은 일자
    N = int(input())
    # 걸리는 시간
    T = []
    # 받는 임금
    P = []
    for n in range(N) :
        T_P = [int(tp) for tp in input().split(' ')]
        T.append(T_P[0])
        P.append(T_P[1])

    root_start = 1
    root_duration = T[0]
    root_end = 1 + T[0] - 1
    root_reward = P[0]
    root = Node(None, root_start, root_duration, root_end, root_reward, 0)

    reward_collection = []
    make_tree(N, T, P, root, reward_collection)
    print(max(reward_collection))
    