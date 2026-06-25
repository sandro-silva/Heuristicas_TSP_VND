# ─────────────────────────────────────────────────
# 7. Main
# ─────────────────────────────────────────────────

import random
import os
from src.experimentos import run_instance

if __name__ == "__main__":
    random.seed(42)

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    instance_path = os.path.join(BASE_DIR, "instances", "berlin52.tsp")

    print("=" * 60)
    print("  TSP - VND  |  UFPB / Estrutura de Dados")
    print("=" * 60)

    result = run_instance(instance_path, num_runs=5)

    print(f"\nInstância   : {result['instance']}")
    print(f"Cidades (n) : {result['n']}")
    print(f"Melhor custo: {result['best']:.2f}")
    print(f"Custo médio : {result['avg_cost']:.2f}")
    print(f"Tempo médio : {result['avg_time_s']:.4f} s")
    print(f"\nMelhor tour : {result['best_tour']}")
    print("\n[Ótimo conhecido berlin52 = 7542]")
    print("=" * 60)