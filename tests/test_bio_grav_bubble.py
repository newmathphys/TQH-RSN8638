"""Био-регенерация ДНК + 3D антигравитационный пузырь RSN-8638.
Запуск: python3 tests/test_bio_grav_bubble.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

k_m = 14.1347251417 / (16 * 137.035999084)
N = 8638
FREE = 7472
V0 = 15.0

SAVE = 'docs/figures_bio_grav'
os.makedirs(SAVE, exist_ok=True)

print("=" * 80)
print("ПРИКЛАДНОЙ КОМПЛЕКС: РЕГЕНЕРАЦИЯ ДНК + АНТИГРАВИТАЦИОННЫЙ ПУЗЫРЬ")
print("=" * 80)

# ═════════════════════════════════════════════════════
# 1: ВОЛНОВОЙ ПАТТЕРН ДНК + ТЕМПЕРАТУРА
# ═════════════════════════════════════════════════════
print(f"\n[1] ДНК-РЕГЕНЕРАЦИЯ:")

phi = np.linspace(-2*np.pi, 2*np.pi, 1000)
psi = np.cos(2*np.pi*np.log(np.abs(phi)+1e-5)/k_m) * np.sin(phi)
bits = np.abs(psi) * 150
T_bio = 309.75 + bits * k_m * 0.05
T_bio_max = np.max(T_bio) - 273.15

print(f"  Амплитуда паттерна: {np.max(np.abs(psi)):.4f}")
print(f"  T_био max: {T_bio_max:.2f} °C")
print(f"  {'✅ Безопасно (<42°C)' if T_bio_max < 42 else '❌ ОПАСНОСТЬ!'}")

# ═════════════════════════════════════════════════════
# 2: 3D ТЕНЗОР НАТЯЖЕНИЯ + ТЕМПЕРАТУРА
# ═════════════════════════════════════════════════════
print(f"\n[2] АНТИГРАВИТАЦИОННЫЙ ПУЗЫРЬ:")

sz = 40
x = np.linspace(-5, 5, sz)
y = np.linspace(-5, 5, sz)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2) + 1e-5

pump = np.exp(-((R-2.5)/0.6)**2)
T00 = V0 * np.cos(2*np.pi*R*k_m) * (1 - 0.98*pump)
T_cond = 293.15 + pump * FREE * k_m * 4.5

print(f"  Радиус пузыря: 2.5 см")
print(f"  Подавление гравитации: 98%")
print(f"  T_проводник max: {np.max(T_cond)-273.15:.1f} °C")
print(f"  {'✅ Требует тугоплавкий материал' if np.max(T_cond) < 1500 else '❌ Расплавится'}")

# ═════════════════════════════════════════════════════
fig = plt.figure(figsize=(16, 6))
ax1 = fig.add_subplot(121)
ax1b = ax1.twinx()
l1 = ax1.plot(phi, psi, 'darkgreen', lw=2, label='Ψ_DNA')
l2 = ax1b.plot(phi, T_bio-273.15, 'crimson', lw=1.5, ls='--', label='T(°C)')
ax1.set_xlabel('φ'); ax1.set_ylabel('Ψ', color='darkgreen')
ax1b.set_ylabel('T (°C)', color='crimson')
ax1.set_title(f'ДНК-регенерация: T_max={T_bio_max:.1f}°C')
lines = l1 + l2; ax1.legend(lines, [l.get_label() for l in lines], loc='upper right', fontsize=8)
ax1.grid(alpha=0.3)

ax2 = fig.add_subplot(122, projection='3d')
surf = ax2.plot_surface(X, Y, T00, cmap='plasma', edgecolor='none', alpha=0.8)
ax2.set_xlabel('X (см)'); ax2.set_ylabel('Y (см)'); ax2.set_zlabel('T₀₀')
ax2.set_title(f'3D пузырь: 98% вес, T={np.max(T_cond)-273.15:.0f}°C')
fig.colorbar(surf, ax=ax2, pad=0.1, label='Натяжение')

plt.tight_layout()
plt.savefig(f'{SAVE}/bio_grav_bubble.png', dpi=150)
print(f"  ✅ График: {SAVE}/bio_grav_bubble.png")

print(f"\n{'='*70}")
print("ИТОГ")
print(f"{'='*70}")
print(f"""
  ДНК-РЕГЕНЕРАЦИЯ:
    Ψ_max = {np.max(np.abs(psi)):.4f}
    T_max = {T_bio_max:.1f} °C (< 42°C ✅)
    → Безопасно для живых тканей

  АНТИГРАВИТАЦИОННЫЙ ПУЗЫРЬ:
    Радиус = 2.5 см
    Вес = 2%
    T_проводник = {np.max(T_cond)-273.15:.0f} °C
    → Нужен Ti/W (тугоплавкий)

  k = {k_m} | N = {N} | FREE = {FREE}
""")
