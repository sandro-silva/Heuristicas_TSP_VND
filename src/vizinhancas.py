# ─────────────────────────────────────────────────
# 3. Movimentos de Vizinhança
# ─────────────────────────────────────────────────
from src.leitura import tour_cost


def swap(tour: list[int], dist: list[list[float]]) -> tuple[list[int], float]:
    """
    N1 - Swap (Troca de Vértices): troca as posições de dois nós i e j no tour.
    Para cada par (i, j), gera um novo tour com tour[i] e tour[j] trocados.
    Aplica a melhor troca encontrada (best improvement) até não haver melhoria.
    Complexidade por iteração: O(n²).
    """
    n = len(tour)
    best = tour[:]
    best_cost = tour_cost(best, dist)
    improved = True
    while improved:
        improved = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                new_tour = best[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_cost(new_tour, dist)
                if new_cost < best_cost - 1e-9:
                    best = new_tour
                    best_cost = new_cost
                    improved = True
    return best, best_cost


def or_opt_k(tour: list[int], dist: list[list[float]], k: int) -> tuple[list[int], float]:
    """
    N2/N3 - Or-opt-k: remove segmento de k nós e reinsere na melhor posição.
    k=1 → Or-opt-1 (reloca nó), k=2 → Or-opt-2 (reloca par).
    """
    n = len(tour)
    best = tour[:]
    best_cost = tour_cost(best, dist)
    improved = True
    while improved:
        improved = False
        for i in range(n):
            seg = [best[(i + s) % n] for s in range(k)]
            remaining = [best[(i + k + s) % n] for s in range(n - k)]
            for j in range(len(remaining)):
                new_tour = remaining[:j + 1] + seg + remaining[j + 1:]
                new_cost = tour_cost(new_tour, dist)
                if new_cost < best_cost - 1e-9:
                    best = new_tour
                    best_cost = new_cost
                    improved = True
    return best, best_cost
