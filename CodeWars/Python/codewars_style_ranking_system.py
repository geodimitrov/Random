class User:
    valid_ranks = [
        -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8,
    ]

    def __init__(self):
        self.rank = -8
        self.progress = 0

    @staticmethod
    def get_activity_points(curr_rank, activity_rank):
        points = 0
        rank_diff = User.valid_ranks.index(activity_rank) - User.valid_ranks.index(curr_rank)

        if rank_diff == 0:
            points = 3
        elif rank_diff == -1:
            points = 1
        elif rank_diff > 0:
            points = 10 * (rank_diff ** 2)

        return points

    def get_next_rank_index(self, rank_progress):
        result = self.valid_ranks.index(self.rank) + rank_progress
        if result >= len(self.valid_ranks):
            return -1

        return result

    def update_rank(self, points):
        rank_progress = (self.progress + points) // 100
        next_rank_index = self.get_next_rank_index(rank_progress)
        self.rank = self.valid_ranks[next_rank_index]

    def update_progress(self, points):
        earned_points = self.progress + points

        if not self.rank == 8:
            if earned_points < 100:
                self.progress += points
            elif earned_points == 100:
                self.progress = 0
            else:
                self.progress = (self.progress + points) % 100

        else:
            self.progress = 0

    def inc_progress(self, activity_rank):
        points = self.get_activity_points(self.rank, activity_rank)
        self.update_rank(points)
        self.update_progress(points)