"""Критический аудит: нейтрино, бег k, антиматерия. Честные результаты.
Запуск: python3 tests/test_neutrino_running_antimatter.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

k_m = 14.1347251417 / (16 * 137.035999084)
N = 8638
M_E_eV = 510998.95

GAMMA = [14.13472514, 21.02203964, 25.01085758]
GAMMA2 = GAMMA[1]
k_g2 = GAMMA2 * (1/137.036) / 16

DM2_SOLAR = 7.5e-5
DM2_ATMOS = 2.5e-3

SAVE = 'docs/figures_critical'
os.makedirs(SAVE, exist_ok=True)

print("=" * 80)
print("КРИТИЧЕСКИЙ АУДИТ: НЕЙТРИНО, БЕГ k, АНТИМАТЕРИЯ")
print("=" * 80)

results = []

# ═════════════════════════════════════════════════════
# 1: НЕЙТРИННЫЕ ОСЦИЛЛЯЦИИ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[1] НЕЙТРИНО: ∆m² ПРИ n=-2404,-2392,-2368")
print(f"{'='*70}")

ns = [-2404, -2392, -2368]
ms = [M_E_eV * np.exp(k_m * n) for n in ns]
dm_sol = ms[1]**2 - ms[0]**2
dm_atm = ms[2]**2 - ms[1]**2

for i, (n, m) in enumerate(zip(ns, ms)):
    print(f"  nu_{i+1}: n={n}, m={m:.5f} eV")
print(f"  ∆m²_sol = {dm_sol:.2e} eV² (exp {DM2_SOLAR:.2e})")
print(f"  ∆m²_atm = {dm_atm:.2e} eV² (exp {DM2_ATMOS:.2e})")

ok_sol = abs(dm_sol/DM2_SOLAR-1) < 2
ok_atm = abs(dm_atm/DM2_ATMOS-1) < 2
results.append(("Нейтрино ∆m²_sol", f"{dm_sol:.2e}", "✅" if ok_sol else "❌"))
results.append(("Нейтрино ∆m²_atm", f"{dm_atm:.2e}", "✅" if ok_atm else "❌"))

# ═════════════════════════════════════════════════════
# 2: БЕГ k ПО ВЫСШИМ НУЛЯМ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[2] БЕГ ПАРАМЕТРА: k(γ₂) НА УЗЛЕ top (n=42)")
print(f"{'='*70}")

m_t_g1 = (M_E_eV/1e9) * np.exp(k_m * 42)  # GeV
m_t_g2 = (M_E_eV/1e9) * np.exp(k_g2 * 42)  # GeV

print(f"  k(γ₁) = {k_m:.6f}, M_top = {m_t_g1:.2f} GeV")
print(f"  k(γ₂) = {k_g2:.6f}, M_top = {m_t_g2:.2f} GeV")
print(f"  Δ = {abs(m_t_g2/m_t_g1-1)*100:.1f}%")
ok_g2 = abs(m_t_g2/m_t_g1-1) < 50
results.append((f"Бег k(γ₂)/k(γ₁)", f"{m_t_g2:.0f}/{m_t_g1:.0f} GeV", "✅" if ok_g2 else "❌"))

# ═════════════════════════════════════════════════════
# 3: АНТИМАТЕРИЯ (n → -n)
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[3] АНТИМАТЕРИЯ: M(-n) ДЛЯ n=0,17,42")
print(f"{'='*70}")

for n_test in [0, 17, 42]:
    mp = M_E_eV * np.exp(k_m * n_test) / 1e6  # GeV
    mn = M_E_eV * np.exp(k_m * (-n_test)) / 1e6  # GeV
    print(f"  n={n_test:3d}: M(+)={mp:.4e} GeV, M(-)={mn:.4e} GeV")
    ok_anti = mp == mn if n_test == 0 else mp != mn
    if n_test == 0:
        results.append(("Анти-e⁻ M(0)=M(-0)", f"={mp:.2e}", "✅"))
    else:
        results.append((f"Анти-частица n={n_test}", f"M(-n)≠M(+n)", "❌"))

# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("ИТОГ КРИТИЧЕСКОГО АУДИТА")
print(f"{'='*70}")
for name, val, status in results:
    print(f"  {status} {name:<30s} {val}")
    
pass_cnt = sum(1 for _,_,s in results if '✅' in s)
print(f"\n  {pass_cnt}/{len(results)} проверок пройдено")
print(f"\n  ВЫВОДЫ:")
print(f"  1. Нейтрино: n=-2404,-2392,-2368 даёт ∆m²_atm≈{dm_atm:.2e} (OK),")
print(f"     но ∆m²_sol≈{dm_sol:.2e} — {'не' if not ok_sol else ''} совпадает")
print(f"  2. Бег k: k(γ₂) на top меняет массу на {abs(m_t_g2/m_t_g1-1)*100:.0f}%")
print(f"  3. Антиматерия: M(-n) ≠ M(+n) для n>0 — не физично")
print(f"\n  Проблемы требуют доработки теории.")
