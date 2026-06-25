# ─────────────────────────────────────────────────
# 2. Heurística de Construção: Nearest Neighbor
# ─────────────────────────────────────────────────
import math


def nearest_neighbor(dist: list[list[float]], start: int = 0) -> list[int]:
    """
    Constrói solução gulosa: partindo de 'start', sempre visita
    a cidade mais próxima ainda não visitada.
    """
    n = len(dist)
    visited = [False] * n
    tour = [start]
    visited[start] = True

    for _ in range(n - 1):
        current = tour[-1]
        best_next = -1
        best_d = math.inf
        for j in range(n):
            if not visited[j] and dist[current][j] < best_d:
                best_d = dist[current][j]
                best_next = j
        tour.append(best_next)
        visited[best_next] = True

    return tour

