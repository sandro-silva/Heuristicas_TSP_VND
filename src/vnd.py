# ─────────────────────────────────────────────────
# 4. VND - Variable Neighborhood Descent
# ─────────────────────────────────────────────────
from src.leitura import tour_cost
from src.vizinhancas import swap, or_opt_k


def vnd(initial_tour: list[int], dist: list[list[float]]) -> tuple[list[int], float]:
    """
    VND com três vizinhanças sequenciais:
      N=1 → Swap
      N=2 → Or-opt-1
      N=3 → Or-opt-2
    Reinicia na primeira vizinhança a cada melhoria.
    """
    neighborhoods = [
        lambda t, d: swap(t, d),
        lambda t, d: or_opt_k(t, d, 1),
        lambda t, d: or_opt_k(t, d, 2),
    ]

    current = initial_tour[:]
    current_cost = tour_cost(current, dist)
    k = 0

    while k < len(neighborhoods):
        new_tour, new_cost = neighborhoods[k](current, dist)
        if new_cost < current_cost - 1e-9:
            current = new_tour
            current_cost = new_cost
            k = 0  # volta à primeira vizinhança
        else:
            k += 1  # avança para próxima vizinhança

    return current, current_cost
