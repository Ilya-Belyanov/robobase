import sympy as sy
import numpy as np

from .dhmatrix import DHMatrix


class SpeedKinematics:
    """Speed Kinematics algorithms"""
    @classmethod
    def linear_speed(cls, transform, args: dict, delta: list):
        yak = cls.jacobi_linear(transform, args)
        return np.dot(yak, np.array(delta).T)

    @staticmethod
    def jacobi_linear(transform, args: dict):
        argNames = list(args.keys())
        return np.array(
            [[sy.diff(transform.row(i).col(3)[0], argNames[j]).subs(args).n() for j in range(len(args))] for i in
             range(3)], dtype='float')

    @classmethod
    def angle_speed(cls, frames, args: dict, delta: list):
        yak = cls.jacobi_angle(frames, args)
        return np.dot(yak, np.array(delta).T).T

    @staticmethod
    def jacobi_angle(frames, args: dict):
        return np.array([np.array(DHMatrix.rotate(frames[j]).evalf(subs=args).col(2)) for j in range(len(frames) - 1)],
                        dtype='float').T[0]
