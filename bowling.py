from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
        self.first_bonus = 0
        self.second_bonus = 0

    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) == 10:
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self.frames):
            raise BowlingError
        return self.frames[i]

    def calculate_score(self) -> int:
        score_sum = 0
        is_perfect = True
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if frame.score() < 10 or frame.is_spare():
                is_perfect = False
            frame_score = frame.score()
            if i < len(self.frames) -1:
                if frame.is_spare():
                    frame_score += self.frames[i+1].get_first_throw()
                if frame.is_strike():
                    frame_score += self.frames[i + 1].score()
                    if self.frames[i+1].is_strike() and i < len(self.frames) - 2:
                        frame_score += self.frames[i + 2].get_first_throw()

            score_sum += frame_score

        if is_perfect:
            return 300
        return score_sum + self.first_bonus + self.second_bonus

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        if self.frames[-1].is_spare() or self.frames[-1].is_strike():
            self.first_bonus = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        if self.frames[-1].is_strike():
            self.second_bonus = bonus_throw
