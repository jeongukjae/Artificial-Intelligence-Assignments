# -*- coding: utf8 -*-
# 8 puzzle 게임 환경 구성
import random

# diretion 상수
UP = 1
LEFT = 2
RIGHT = 3
DOWN = 4

class EightPuzzle:
    # 가능한 이동 방향들
    DIRECTIONS = [UP, LEFT, RIGHT, DOWN]

    def __init__(self):
        # 1 ~ 9, 0
        self.state = list(range(1, 9)) + [0]

    # x, y 좌표를 그냥 인덱스로 변경함
    def convert_coord(self, x, y):
        return y * 3 + x

    # 위 함수 반대
    def reverse_convert_coord(self, index):
        return index % 3, int(index / 3)

    # 가능한 방향인지 체크함
    def check_possible_direction(self, direction):
        x, y = self.get_coord()
        if (x is 2 and direction is RIGHT) or \
            (x is 0 and direction is LEFT) or \
            (y is 2 and direction is DOWN) or \
            (y is 0 and direction is UP):
            return False
        return True

    # 가능한 방향들을 받아옴
    def check_possible_directions(self, dirs):
        directions = dirs[:] # copy list

        for direction in directions:
            if not self.check_possible_direction(direction):
                directions.remove(direction)

        return directions

    # 빈칸(0)을 옮길 방향으로 act를 정의
    def act(self, direction):
        # 빈칸의 위치
        source = self.state.index(0)
        x, y = self.reverse_convert_coord(source)

        # 오류 체크
        if not self.check_possible_direction(direction):
            raise Exception("Bad Direction")

        # 옮길 곳 좌표 받아오기
        if direction is RIGHT:
            target_x = x + 1
            target_y = y
        elif direction is LEFT:
            target_x = x - 1
            target_y = y
        elif direction is DOWN:
            target_x = x
            target_y = y + 1
        elif direction is UP:
            target_x = x
            target_y = y - 1
        else:
            # 방향이 이상하다 -> Bad Direction
            raise Exception("Bad Direction")

        # swap
        target = self.convert_coord(target_x, target_y)
        self.state[source], self.state[target] = self.state[target], self.state[source]

    # 게임 하기 전 초기화 하는 함수
    def shuffle(self, times):
        for _ in range(times):
            # get possible direction
            while True:
                direction = random.choice(self.DIRECTIONS)
                if self.check_possible_direction(direction):
                    break
            
            self.act(direction)

    # 현재 state
    def get_state(self):
        return self.state

    # 현재 좌표
    def get_coord(self):
        return self.reverse_convert_coord(self.state.index(0))

    # 게임 끝났는지 체크
    def is_end(self):
        if [1,2,3,4,5,6,7,8,0] == self.state:
            return True
        
        return False