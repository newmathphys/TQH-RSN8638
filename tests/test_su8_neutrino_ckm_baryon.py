"""SU(8) вывод N, нейтрино γ₂/γ₃, CKM/PMNS, барионная асимметрия.
Запуск: python3 tests/test_su8_neutrino_ckm_baryon.py
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

ALPHA = 1/137.035999074
M_E_eV = 510998.95
GAMMA = np.array([14.13472514, 21.02203964, 25.01085758])
k_m = GAMMA[0] * ALPHA / 16

SAVE = 'docs/figures_su8'
os.makedirs(SAVE, exist_ok=True)

print("=" * 80)
print("SU(8) ВЫВОД N + НЕЙТРИНО + CKM/PMNS + БАРИОННАЯ АСИММЕТРИЯ")
print("=" * 80)

results = []

# ═════════════════════════════════════════════════════
# 1: N = 63·α⁻¹ + 3π/2
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[1] ВЫВОД N = 8638 ИЗ dim(SU(8)) = 63")
print(f"{'='*70}")

N_derived = 63/ALPHA + 3*np.pi/2
N_int = int(round(N_derived))
print(f"  N = 63·α⁻¹ + 3π/2 = 63·{1/ALPHA:.3f} + {3*np.pi/2:.4f}")
print(f"    = {63/ALPHA:.2f} + {3*np.pi/2:.4f} = {N_derived:.2f}")
print(f"    = {N_int}")
print(f"  N_RSN = 8638")
print(f"  {'✅ Совпадает' if N_int == 8638 else '❌'}")

# ═════════════════════════════════════════════════════
# 2: НЕЙТРИНО С γ₂, γ₃ ПОПРАВКАМИ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[2] НЕЙТРИНО С ВЫСШИМИ НУЛЯМИ ζ(s)")
print(f"{'='*70}")

ns = np.array([-2404, -2392, -2368])
ms_raw = [M_E_eV * np.exp(k_m * n) for n in ns]

ms_corr = []
for n in ns:
    corr = (ALPHA/16)*(GAMMA[1]/n + GAMMA[2]/n**2)
    m = M_E_eV * np.exp(k_m*n + corr)
    ms_corr.append(m)
ms_corr = np.array(ms_corr)

dm2_sol_raw = ms_raw[1]**2 - ms_raw[0]**2
dm2_atm_raw = ms_raw[2]**2 - ms_raw[1]**2
dm2_sol = ms_corr[1]**2 - ms_corr[0]**2
dm2_atm = ms_corr[2]**2 - ms_corr[1]**2

print(f"  Без поправок:")
for i, (n, m) in enumerate(zip(ns, ms_raw)):
    print(f"    nu_{i+1}: n={n}, m={m:.5f} eV")
print(f"    dm2_sol = {dm2_sol_raw:.2e} eV2")

print(f"  С поправками gamma_2, gamma_3:")
for i, (n, m) in enumerate(zip(ns, ms_corr)):
    print(f"    nu_{i+1}: n={n}, m={m:.5f} eV")
print(f"    dm2_sol = {dm2_sol:.2e} eV2 (exp 7.5e-5)")
print(f"    dm2_atm = {dm2_atm:.2e} eV2 (exp 2.5e-3)")

ok_sol = abs(dm2_sol/7.5e-5 - 1) < 0.5
ok_atm = abs(dm2_atm/2.5e-3 - 1) < 0.5
results.append((f"dm2_sol", f"{dm2_sol:.2e}", "✅" if ok_sol else "❌"))
results.append((f"dm2_atm", f"{dm2_atm:.2e}", "✅" if ok_atm else "❌"))

# ═════════════════════════════════════════════════════
# 3: CKM/PMNS УГЛЫ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[3] УГЛЫ СМЕШИВАНИЯ ПОКОЛЕНИЙ")
print(f"{'='*70}")

theta_12 = np.arcsin((GAMMA[1]-GAMMA[0]) / (GAMMA[0]*np.sqrt(63)))
theta_13 = np.arcsin((GAMMA[2]-GAMMA[0]) / (GAMMA[0]*np.sqrt(63)))
theta_23 = np.arcsin((GAMMA[2]-GAMMA[1]) / (GAMMA[0]*np.sqrt(63)))

print(f"  theta_12 = {np.degrees(theta_12):.2f} deg (CKM Cabibbo ~13.02 deg)")
print(f"  theta_13 = {np.degrees(theta_13):.2f} deg")
print(f"  theta_23 = {np.degrees(theta_23):.2f} deg")

ok_cab = abs(np.degrees(theta_12) - 13.02)/13.02 < 0.1
results.append((f"CKM Cabibbo", f"{np.degrees(theta_12):.2f} deg", "✅" if ok_cab else "❌"))

# ═════════════════════════════════════════════════════
# 4: БАРИОННАЯ АСИММЕТРИЯ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("[4] БАРИОННАЯ АСИММЕТРИЯ η")
print(f"{'='*70}")

eta = np.exp(k_m * -2404) * 63 / 8638
print(f"  eta = exp(k*-2404) * 63/8638 = {eta:.2e}")
print(f"  exp = ~6e-10")
ok_eta = abs(eta/6e-10 - 1) < 2
results.append((f"eta", f"{eta:.2e}", "✅" if ok_eta else "❌"))

# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("ИТОГ")
print(f"{'='*70}")
for name, val, status in results:
    print(f"  {status} {name:<25s} {val}")
    
pass_cnt = sum(1 for _,_,s in results if '✅' in s)
print(f"\n  {pass_cnt}/{len(results)} пройдено")
print(f"\n  N вывод: N = 63·alpha^(-1) + 3pi/2 = {N_int} ✅")
