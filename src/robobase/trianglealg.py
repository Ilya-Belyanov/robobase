class Point:
    """Point object"""
    def __init__(self, coords=None):
        if coords is None:
            coords = [0, 0]
        self.x = coords[0]
        self.y = coords[1]

    def coord(self):
        return [self.x, self.y]


class Triangle:
    """Triangle object"""
    def __init__(self, points=None):
        if points is None:
            points = [Point(), Point(), Point()]
        self.point_1 = points[0]
        self.point_2 = points[1]
        self.point_3 = points[2]

    def is_intersection(self, other):
        if self.check_separate(self.line_point_pairs(), other.points()):
            return False
        if self.check_separate(other.line_point_pairs(), self.points()):
            return False
        return True

    @classmethod
    def check_separate(cls, pairs, points):
        for s_p in pairs:
            duration = cls.is_clock_wise(s_p[0], s_p[1], s_p[2])
            separate = True
            for point in points:
                if duration == cls.is_clock_wise(s_p[0], s_p[1], point) or cls.is_line(s_p[0], s_p[1], point):
                    separate = False
                    break
            if separate:
                return True
        return False

    def points(self):
        return [self.point_1, self.point_2, self.point_3]

    def edges(self):
        return [[self.point_1, self.point_2],
                [self.point_2, self.point_3],
                [self.point_3, self.point_1]]

    def line_point_pairs(self):
        return [[self.point_1, self.point_2, self.point_3],
                [self.point_2, self.point_3, self.point_1],
                [self.point_3, self.point_1, self.point_2]]

    @staticmethod
    def duration_rotate(first: Point, second: Point, third: Point):
        return (second.x - first.x) * (third.y - first.y) \
             - (second.y - first.y) * (third.x - first.x)

    @classmethod
    def is_clock_wise(cls, first: Point, second: Point, third: Point):
        return cls.duration_rotate(first, second, third) < 0

    @classmethod
    def is_line(cls, first: Point, second: Point, third: Point):
        return cls.duration_rotate(first, second, third) == 0
