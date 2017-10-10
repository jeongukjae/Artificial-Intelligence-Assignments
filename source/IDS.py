# -*- coding:utf8 -*-
# 8 puzzle을 IDS로 품

# 게임 풀기 위해서 미리 만들어 놓은 Node, EightPuzzle 클래스들
from node import Node
from eightpuzzle import EightPuzzle, UP, DOWN, LEFT, RIGHT

import copy
import random
import time

# 이동 방향
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

# 부모 노드 중복 체크. 중복이면 그냥 바로 짜름
def check_duplication_of_parent(node):
    parent = node.get_parent()

    while True:
        # state (여기서는 길이가 9인 리스트)가 같으면 중복임
        if node.get_data().get_state() == parent.get_data().get_state():
            return True

        # 최상위 노드에 도달하면 짜름
        if parent.get_depth() == 1:
            return False

        parent = parent.get_parent()

# Expand 함수
def make_nodes(node):
    # 현재 state랑 depth 받아옴
    puzzle = node.get_data()
    depth = node.get_depth()

    # actions 복사함
    actions = DIRECTIONS[:]
    nodes = []

    for action in actions:
        # action이 가능한 action이어야 움직이도록 조절
        if not puzzle.check_possible_direction(action):
            continue

        # state는 원래 node가 값이 변경되지 않도록 복사해서 사용함
        copied = copy.deepcopy(puzzle)
        # 행동 취해봄
        copied.act(action)

        # 취한 행동으로 새로운 Node를 만듬
        new_node = Node(depth + 1, copied)
        # 부모 노드로 설정
        new_node.set_parent(node)

        # 근데 부모랑 중복이면 짜른다.
        if check_duplication_of_parent(new_node):
            continue

        # 부모랑 중복도 되지 않고, 가능한 state라면 nodes에 추가해줌
        nodes.append(new_node)

    # 자식 노드 리스트 반환
    return nodes

def recursive_dls(node, limit):
    # fringe를 쓰지 않는 방법으로 써져있었지만, 편의상 만듬
    fringe = []
    # 현재 탐색 중인 노드 로그 찍어주기
    print(node)

    # 만약 끝나는 상황이면 성공한 node를 반환함
    if node.get_data().is_end():
        return [], node

    # 만약 depth 한계에 도달하면 그만둠
    if node.get_depth() is limit:
        return make_nodes(node), False

    # node 자식을 확장해서 그 자식을 탐색해봄
    for child in make_nodes(node):
        # 재귀적으로 구현
        children, result = recursive_dls(child, limit)

        # 그 result가 False면 답을 찾지 못한 채 depth 한계에 도달한 것이므로,
        # False가 아닐 때 result를 반환해줌
        if result is not False:
            return fringe, result

        # result가 False면 그냥 fringe에 children 추가해줌
        fringe.extend(children)

    # 이렇게 fringe를 반환해주는 까닭은
    # depth의 한계에 도달한 node들의 자식들을 모으기 위함임
    return fringe, False

def search(initial_node):
    # fringe, next_generation 두 리스트를 만들어서 관리함
    # fringe를 통해 현재 탐색해야 할 노드들을 저장하고,
    # next_generation을 통해 다음번에 탐색해야 할 노드들을 저장함
    # (현재 fringe에 들어있는 노드들의 자식을 모으는 노드들)
    fringe = [initial_node]
    next_generation = []

    # depth limit을 설정할 변수
    depth_limit = 3
    
    while True:
        # fringe가 empty 상황이 아니라면
        while fringe:
            # 순서 상관없음
            current_node = fringe.pop(0)

            # 탐색해봄
            children, result = recursive_dls(current_node, depth_limit)

            # 근데 result가 False면 해당 깊이에서는 답이 없었다는 뜻이 되므로
            # False가 아닌 상황을 체크함
            if result is not False:
                return result

            # result가 False면 자식 세대를 추가함
            next_generation.extend(children)

        # 자식 세대를 탐색하기 위해 교체해줌
        fringe = next_generation
        next_generation = []

        # depth_limit을 3씩 올려줌
        depth_limit += 3

def run(times):
    # 초기 state 만들어주기
    puzzle = EightPuzzle()
    puzzle.shuffle(times) # puzzle 섞기

    # 탐색
    result = search(Node(1, puzzle))

    # 결과 출력
    print('game end : {0}'.format(result))

if __name__ == "__main__":
    start_time = time.time()

    for _ in range(1000):
        run(10)

    elapsed_time = time.time() - start_time
    print('average elapsed time : {0}'.format(elapsed_time / 1000))

# 10번 섞은 퍼즐을 푸는 데 걸린 평균 (1000번 시행)
# average elapsed time : 0.022545029878616334
# average elapsed time : 0.0198214430809021

# 15번 섞은 퍼즐을 푸는 데 걸린 평균 (1000번 시행)
# average elapsed time : 0.07743071508407592
# average elapsed time : 0.08387356281280517 