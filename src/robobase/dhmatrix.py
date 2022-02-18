import sympy as sy


class DHMatrix:
    """Класс для работы с матрицей Денавита-Хартенберга"""

    @staticmethod
    def matrix(r_length, alpha, d_length, theta):
        """Возвращает матрицу Денавита-Хартенберга из входных параметров"""
        return sy.Matrix([[sy.cos(theta), -1 * sy.sin(theta) * sy.cos(alpha),
                           sy.sin(theta) * sy.sin(alpha), r_length * sy.cos(theta)],
                         [sy.sin(theta), sy.cos(theta) * sy.cos(alpha),
                          -1 * sy.cos(theta) * sy.sin(alpha), r_length * sy.sin(theta)],
                         [0, sy.sin(alpha), sy.cos(alpha), d_length],
                         [0, 0, 0, 1]])

    @staticmethod
    def pos(matrix: sy.Matrix) -> sy.Matrix:
        """Возвращает матрицу положения x, y, z из матрицы Денавита-Хартенберга"""
        return sy.Matrix([matrix.row(j).col(3)[0] for j in range(3)])

    @staticmethod
    def rotate(matrix: sy.Matrix) -> sy.Matrix:
        """Возвращает матрицу поворота из матрицы Денавита-Хартенберга"""
        return sy.Matrix([[matrix.row(j).col(i)[0] for i in range(3)] for j in range(3)])
