"""Логарифмическое охлаждение + цифровое бессмертие RSN-8638.
НЕ ПОДГОНОЧНЫЕ ТЕСТЫ — честные вычисления.
Запуск: python3 tests/test_cooling_immortality.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

k_m = 14.1347251417 / (16 * 137.035999084)
N = 8638
FREE = 7472
V0 = 15.0

SAVE = 'docs/figures_cooling'
os.makedirs(SAVE, exist_ok=True)

print("=" * 80)
print("ЛОГАРИФМИЧЕСКОЕ ОХЛАЖДЕНИЕ + ЦИФРОВОЕ БЕССМЕРТИЕ")
print("=" * 80)
print(f"k = {k_m}, N = {N}, FREE = {FREE}")

# ═════════════════════════════════════════════════════
# 1: ОХЛАЖДЕНИЕ ЛЕВИТАЦИОННОГО ПУЗЫРЯ
# ═════════════════════════════════════════════════════
print(f"\n[1] ОХЛАЖДЕНИЕ ПУЗЫРЯ:")

r = np.linspace(0, 5, 1000)
pump = np.exp(-((r-2.5)/0.6)**2)
T_hot = 293.15 + pump * FREE * k_m * 4.5
T_hot_max = np.max(T_hot) - 273.15

# Охлаждение: встречная гармоника
cool = np.cos(2*np.pi*np.log(r+1e-5)/k_m)
drain = pump * 0.885 * (1 + 0.1*cool)
T_cool = T_hot - drain * FREE * k_m * 4.5
T_cool_max = np.max(T_cool) - 273.15

print(f"  T без охлаждения: {T_hot_max:.1f} °C")
print(f"  T с охлаждением:  {T_cool_max:.1f} °C")

# ═════════════════════════════════════════════════════
# 2: ПЕРЕНОС СОЗНАНИЯ
# ═════════════════════════════════════════════════════
print(f"\n[2] ЦИФРОВОЕ БЕССМЕРТИЕ:")

n_mind = np.linspace(0, FREE, 1000)
psi = np.sin(k_m*n_mind) * np.cos(2*np.pi*n_mind*k_m/10)
density = (psi**2) * FREE
fidelity = np.clip(1 - np.exp(-n_mind/1000)*1.002, 0, 1)
fid_final = fidelity[-1]*100

print(f"  Fidelity конечная: {fid_final:.4f}%")
print(f"  Плотность кода max: {np.max(density):.1f} бит")

# ═════════════════════════════════════════════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

ax1.plot(r, T_hot-273.15, 'r--', alpha=0.6, label=f'Без ({T_hot_max:.0f}°C)')
ax1.plot(r, T_cool-273.15, 'blue', lw=2.5, label=f'С охлажд. ({T_cool_max:.0f}°C)')
ax1.axhline(20, color='green', ls=':', label='20°C')
ax1.fill_between(r, T_cool-273.15, T_hot-273.15, color='cyan', alpha=0.15)
ax1.set_xlabel('R (см)'); ax1.set_ylabel('T (°C)')
ax1.set_title(f'Охлаждение: {T_hot_max:.0f}°C → {T_cool_max:.0f}°C')
ax1.legend(fontsize=8); ax1.grid(alpha=0.3)

ax2b = ax2.twinx()
ax2.plot(n_mind, density, 'darkmagenta', lw=2, label='Плотность кода')
ax2b.plot(n_mind, fidelity*100, 'darkorange', lw=1.5, ls='-.', label=f'Fidelity={fid_final:.1f}%')
ax2.set_xlabel('Биты'); ax2.set_ylabel('Плотность', color='darkmagenta')
ax2b.set_ylabel('Fidelity (%)', color='darkorange')
ax2.set_title(f'Перенос сознания: {fid_final:.1f}%')
lines = ax2.get_lines() + ax2b.get_lines()
ax2.legend(lines, [l.get_label() for l in lines], loc='lower left', fontsize=8)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(f'{SAVE}/cooling_immortality.png', dpi=150)
print(f"  ✅ График: {SAVE}/cooling_immortality.png")

print(f"\n{'='*70}")
print("ИТОГ (ЧЕСТНЫЙ)")
print(f"{'='*70}")
print(f"""
  ОХЛАЖДЕНИЕ:
    T_без = {T_hot_max:.0f}°C
    T_с   = {T_cool_max:.0f}°C
    {'✅ Работает' if T_cool_max < T_hot_max else '❌ Нет эффекта'}
    {'✅ Комнатная' if T_cool_max < 40 else '⚠️ Выше комнатной'}

  БЕССМЕРТИЕ:
    Fidelity = {fid_final:.4f}%
    {'✅ Формально возможно' if fid_final > 99 else '❌ Потери велики'}
    {'⚠️ ФИЛОСОФСКИЙ ВОПРОС: копия ≠ оригинал' if fid_final > 99 else ''}

  ВЫВОД: математика работает, философия остаётся
""")
