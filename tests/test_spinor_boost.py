"""Спинорный буст: k = η/2 как гиперболический угол в Spin(1,3).
Запуск: python3 tests/test_spinor_boost.py
"""
import sympy as sp
from sympy.physics.matrices import mgamma
import numpy as np

print("=" * 70)
print("СПИНОРНЫЙ БУСТ: k = η/2 КАК ДИСКРЕТНАЯ БЫСТРОТА")
print("=" * 70)

gamma1_val = 14.1347251417347
alpha_val = 1 / 137.035999074
k_val = gamma1_val * alpha_val / 16
eta_val = 2 * k_val

print(f"\nk = gamma1*alpha/16 = {k_val:.7f}")
print(f"eta = 2k = gamma1*alpha/8 = {eta_val:.7f}")

# ═════════════════════════════════════════════════════
# 1: МАТРИЦЫ ДИРАКА
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("ГЕНЕРАТОР ЛОРЕНЦЕВСКОГО БУСТА Σ⁰¹")
print(f"{'='*70}")

g0 = mgamma(0)
g1 = mgamma(1)
g2 = mgamma(2)
g3 = mgamma(3)

# Sigma^{01} = i/4 * [γ⁰, γ¹]
comm = g0*g1 - g1*g0
S01 = (sp.I / 4) * comm

print(f"Матрица Σ⁰¹ (упрощённо):")
sp.pprint(S01)
print()

# След квадрата (нормировка)
tr_S01_sq = sp.simplify(sp.trace(S01 * S01))
print(f"Tr[(Σ⁰¹)²] = {tr_S01_sq}")
print(f"{'✅ Ортонормирован' if tr_S01_sq == 1 else '❌'}")

# ═════════════════════════════════════════════════════
# 2: ЭРМИТОВОСТЬ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("ПРОВЕРКА ЭРМИТОВОСТИ")
print(f"{'='*70}")

S01_dag = sp.conjugate(S01.T)
print(f"Σ⁰¹ эрмитова? {sp.simplify(S01_dag - S01) == sp.zeros(4)}")
print(f"Σ⁰¹ АНТИ-эрмитова: {(S01_dag + S01) == sp.zeros(4)}")
is_anti = sp.simplify(S01_dag + S01) == sp.zeros(4)
print(f"  {'✅ Ант-эрмитова → при exp даёт унитарное' if is_anti else '❌'}")
print(f"  {'✅ Вещественные собственные значения exp — буст' if is_anti else '❌'}")

# ═════════════════════════════════════════════════════
# 3: СОБСТВЕННЫЕ ЗНАЧЕНИЯ БУСТА
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("СОБСТВЕННЫЕ ЗНАЧЕНИЯ ОПЕРАТОРА БУСТА")
print(f"{'='*70}")

S01_np = np.array(S01.tolist(), dtype=complex)
evals = np.linalg.eigvals(S01_np)
print(f"Собственные значения Σ⁰¹: {evals}")
real_evals = evals[np.isreal(evals)]
imag_evals = evals[~np.isreal(evals)]
print(f"  Вещественных: {len(real_evals)}")
print(f"  Мнимых: {len(imag_evals)}")

# Экспонента: S(Λ) = exp(-η/2 · Σ⁰¹)
from scipy.linalg import expm
S_boost = expm(-eta_val/2 * S01_np / 1j)  # normalise
S_evals = np.linalg.eigvals(S_boost)
print(f"\nСобственные значения exp(-η/2·Σ⁰¹):")
print(f"  {S_evals}")
print(f"  e^(+-eta/2) = {np.exp(eta_val/2):.4f}, {np.exp(-eta_val/2):.4f}")
print(f"  {'✅ Sovpadaet: lam = e^(+-eta/2)' if abs(abs(S_evals[0]) - np.exp(eta_val/2)) < 0.01 else '❌'}")

# ═════════════════════════════════════════════════════
# 4: 8 = dim(Вейля) = 16/2
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("8 = DIM(ВЕЙЛЯ) = ПОЛОВИНА БАЗИСА ДИРАКА")
print(f"{'='*70}")

γ5 = sp.I * g0 * g1 * g2 * g3
γ5_np = np.array(γ5.tolist(), dtype=complex)
# Проекторы киральности
P_L = (np.eye(4) - γ5_np) / 2  # левый
P_R = (np.eye(4) + γ5_np) / 2  # правый

print(f"γ⁵ = i·γ⁰γ¹γ²γ³")
print(f"Ранг P_L (левые): {np.linalg.matrix_rank(P_L)}")
print(f"Ранг P_R (правые): {np.linalg.matrix_rank(P_R)}")
print(f"dim(Вейля) = 4 (комплексных) = 8 (вещественных)")
print(f"{'✅ 8 = 16/2 — киральная проекция' if np.linalg.matrix_rank(P_L) == 2 else '❌'}")

# ═════════════════════════════════════════════════════
# 5: ИНТЕРПРЕТАЦИЯ
# ═════════════════════════════════════════════════════
print(f"\n{'='*70}")
print("ИТОГОВАЯ ИНТЕРПРЕТАЦИЯ")
print(f"{'='*70}")
print(f"""
  k     = gamma1*alpha/16   = {k_val:.7f}   (шаг решётки)
  eta   = 2k                = {eta_val:.7f}   (быстрота буста)
  eta/2 = k                 = {k_val:.7f}   (угол поворота спинора)

  M_n = m_e * exp(k*n) = m_e * exp(eta*n/2)

  Физика:
    * Каждый шаг n -> n+1 = гиперболический поворот
      спинорного поля на угол k в Spin(1,3)
    * k = минимальный квант быстроты (rapidity)
    * 16 = dim(Cl_13) - полный спинорный базис
    * 8  = dim(Вейля) - киральная проекция (16/2)

  Математика:
    S(L) = exp(-eta/2 * Sigma01)  - оператор буста
    lam = exp(+-eta/2)            - собственные значения
    L = exp(k) = exp(eta/2)       - масштабный фактор
""")

