import sympy as sy

from .dhmatrix import DHMatrix


class ForwardKinematics:
    """Класс для работы с прямой кинематикой"""

    @staticmethod
    def links(d_length: list, r_length: list, thetas: list, alpha: list) -> list:
        """Формирование всех матриц преобразования T(i-1, i)"""
        return [DHMatrix.matrix(r_length[i], alpha[i], d_length[i], thetas[i]) for i in range(len(d_length))]

    @staticmethod
    def frames(links: list) -> list:
        """Формирование всех матриц преобразования T(0, i) где i от 0 до N"""
        frames = list([sy.eye(4)])
        frames.append(links[0])
        for i in range(1, len(links)):
            frames.append(frames[-1] * links[i])
        return frames

    @staticmethod
    def result_matrix(links: list) -> sy.Matrix:
        """Формирование результирующей матрицы преобразования"""
        result = links[0]
        for i in range(1, len(links)):
            result = result * links[i]
        return result
