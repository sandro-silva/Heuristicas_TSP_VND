# ─────────────────────────────────────────────────
# 5. Experimentos
# ─────────────────────────────────────────────────
import math
import os
import random
import time

from src.construcao import nearest_neighbor
from src.leitura import parse_tsplib, build_distance_matrix
from src.vnd import vnd


def run_instance(filepath: str, num_runs: int = 5) -> dict:
    """
    Executa nearest_neighbor + VND sobre uma instância.
    Retorna métricas: melhor custo, média de custo, média de tempo.
    """
    coords = parse_tsplib(filepath)
    dist = build_distance_matrix(coords)
    n = len(coords)

    costs = []
    times = []
    best_tour = None
    best_cost = math.inf

    starts = random.sample(range(n), min(num_runs, n))

    for s in starts:
        t0 = time.perf_counter()
        init = nearest_neighbor(dist, start=s)
        tour, cost = vnd(init, dist)
        elapsed = time.perf_counter() - t0

        costs.append(cost)
        times.append(elapsed)

        if cost < best_cost:
            best_cost = cost
            best_tour = tour

    return {
        "instance": os.path.basename(filepath),
        "n": n,
        "best": best_cost,
        "avg_cost": sum(costs) / len(costs),
        "avg_time_s": sum(times) / len(times),
        "best_tour": best_tour,
    }
