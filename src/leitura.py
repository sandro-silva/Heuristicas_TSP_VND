"""
Projeto Final - Estrutura de Dados e Complexidade de Algoritmos
UFPB - Centro de Informática

Problema: Travelling Salesman Problem (TSP)
Meta-heurística: Variable Neighborhood Descent (VND)

Estrutura:
  - Heurística de construção: Nearest Neighbor (Vizinho Mais Próximo)
  - Movimentos de vizinhança:
      N1: Swap  (troca de vértices)
      N2: Or-opt-1 (realoca um único nó)
      N3: Or-opt-2 (realoca um segmento de 2 nós)
  - VND: percorre as vizinhanças em ordem sequencial
"""

import math
import time
import random
import os
import urllib.request


# ─────────────────────────────────────────────────
# 1. Leitura de instâncias TSPLIB (.tsp)
# ─────────────────────────────────────────────────

def parse_tsplib(filepath: str) -> list[tuple[float, float]]:
    """Lê arquivo TSPLIB e retorna lista de coordenadas (x, y)."""
    coords = []
    reading = False
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line == "NODE_COORD_SECTION":
                reading = True
                continue
            if line in ("EOF", ""):
                if reading:
                    break
                continue
            if reading:
                parts = line.split()
                coords.append((float(parts[1]), float(parts[2])))
    return coords


def euclidean(a: tuple, b: tuple) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def build_distance_matrix(coords: list) -> list[list[float]]:
    n = len(coords)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = euclidean(coords[i], coords[j])
    return dist


def tour_cost(tour: list[int], dist: list[list[float]]) -> float:
    n = len(tour)
    return sum(dist[tour[i]][tour[(i + 1) % n]] for i in range(n))
