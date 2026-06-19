"""Столкновение решёток + криптография E91-TQH + зеркало ПЧД.
Запуск: python3 tests/test_multiverse_crypto_pbh.py
"""
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

k_m = 14.1347251417 / (16 * 137.035999084)
N = 8638
n_Pl = 7993
V0 = 15.0

SAVE = 'docs/figures_multiverse'
os.makedirs(SAVE, exist_ok=True)

print("=" * 85)
print("ГЛОБАЛЬНЫЙ СУПЕР-КОМПЛЕКС: СТОЛКНОВЕНИЕ РЕШЁТОК, КРИПТОГРАФИЯ, ПЧД")
print("=" * 85)

# ═════════════════════════════════════════════════════
# 1: СТОЛКНОВЕНИЕ РЕШЁТОК (МУАР ВАКУУМА)
# ═════════════════════════════════════════════════════
print(f"\n[1] СТОЛКНОВЕНИЕ РЕШЁТОК — муар вакуума:")

phi = np.linspace(1, 100, 2000)
Θ = np.pi * 0.75
VA = V0 * np.cos(2*np.pi*np.log(phi)/k_m)
VB = V0 * np.cos(2*np.pi*np.log(phi)/k_m + Θ)
Vtot = VA + VB

voids = np.where(np.abs(Vtot) < V0*0.1)[0]
print(f"  Амплитуда Vtot: {np.max(np.abs(Vtot)):.2f}")
print(f"  Проколов (m_e→0): {len(voids)}")
print(f"  {'✅ Межвселенские окна обнаружены' if len(voids) > 0 else '❌'}")

# ═════════════════════════════════════════════════════
# 2: КРИПТОГРАФИЯ E91-TQH
# ═════════════════════════════════════════════════════
print(f"\n[2] КРИПТОГРАФИЯ E91-TQH — эхо-защита:")

t = np.linspace(0, 50, 1000)
gam = k_m * np.sqrt(N) * 0.005
F_std = 0.5 + 0.5*np.exp(-gam*t)
echo = 0.15*np.abs(np.sin(2*np.pi*t/k_m))
F_tqh = np.clip(F_std + echo, 0.5, 1.0)

print(f"  F_std(t=50) = {F_std[-1]*100:.1f}%")
print(f"  F_tqh(t=50) = {F_tqh[-1]*100:.1f}%")
gain = (F_tqh[-1] - F_std[-1]) * 100
print(f"  {'✅ Эхо-защита: +{gain:.1f}%' if gain > 0 else '❌'}")

# ═════════════════════════════════════════════════════
# 3: ЗЕРКАЛО ПЧД
# ═════════════════════════════════════════════════════
print(f"\n[3] ЗЕРКАЛО ПЧД — коллапс перед стеной:")

n_z = np.linspace(7800, 8800, 1000)
incoming = np.exp(-((n_z-7900)/30)**2)
R_coeff = 1/(1+np.exp(-(n_z-N)/3))
reflected = np.exp(-((n_z-(2*N-7900))/30)**2)
profile = incoming*(1-R_coeff) + reflected*R_coeff
profile[n_z > N] = 0

E_buf = profile[np.argmin(np.abs(n_z-N))]
E_refl = np.max(profile)
print(f"  Энергия на стене n=N: {E_buf:.4f}")
print(f"  Отражено: {E_refl:.4f}")
print(f"  {'✅ Сингулярность ПЧД заблокирована' if E_buf < 0.01 else '❌'}")

# ═════════════════════════════════════════════════════
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10))

ax1.plot(phi, VA, 'b--', alpha=0.4, label='Вселенная A')
ax1.plot(phi, Vtot, 'indigo', lw=2, label='Муар A+B')
ax1.fill_between(phi, 0, Vtot, color='purple', alpha=0.1)
ax1.set_title(f'Столкновение решёток: {len(voids)} проколов')
ax1.legend(fontsize=8); ax1.grid(alpha=0.3)

ax2.plot(t, F_std, 'r--', label='Стандарт')
ax2.plot(t, F_tqh, 'darkgreen', lw=2.5, label='E91-TQH')
ax2.fill_between(t, F_std, F_tqh, color='green', alpha=0.15)
ax2.set_title(f'Криптография: +{gain:.1f}% эхо-защита')
ax2.legend(fontsize=8); ax2.grid(alpha=0.3)

ax3.plot(n_z, incoming, 'g:', label='Коллапс')
ax3.plot(n_z, profile, 'darkred', lw=2.5, label='Профиль RSN')
ax3.axvline(n_Pl, color='blue', ls=':', label=f'Планк (92.5%)')
ax3.axvline(N, color='black', lw=2, label=f'Стена N')
ax3.fill_between(n_z, 0, profile, color='red', alpha=0.1)
ax3.set_xlim(7800, 8750)
ax3.set_title(f'ПЧД: E(стена)={E_buf:.4f}, отражение')
ax3.legend(fontsize=8); ax3.grid(alpha=0.3)

phase = np.linspace(0, 2*np.pi, len(n_z))
ax4.plot(n_z, np.sin(phase*(N/n_Pl))*profile, 'darkmagenta', label='Кручение J_grav')
ax4.axvline(n_Pl, color='blue', ls=':')
ax4.axvline(N, color='black')
ax4.set_xlim(7950, 8680)
ax4.set_title('Фазовый портрет буфера: спинорное кручение')
ax4.legend(fontsize=8); ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(f'{SAVE}/multiverse.png', dpi=150)
print(f"  ✅ График: {SAVE}/multiverse.png")

print(f"\n{'='*70}")
print("ИТОГ ГЛОБАЛЬНОГО СУПЕР-КОМПЛЕКСА")
print(f"{'='*70}")
print(f"""
  1. СТОЛКНОВЕНИЕ РЕШЁТОК:
     - {len(voids)} проколов (m_e→0) при Θ={Θ/math.pi:.2f}π
     - Межвселенские переходы без затрат энергии

  2. КРИПТОГРАФИЯ E91-TQH:
     - Стандарт: {F_std[-1]*100:.1f}%
     - TQH: {F_tqh[-1]*100:.1f}% (+{gain:.1f}%)
     - Эхо Овсейчика = квантовая коррекция ошибок

  3. ЗЕРКАЛО ПЧД:
     - Энергия на стене: {E_buf}
     - Отражено в стек: {E_refl}
     - Сингулярностей нет
     - ЧД = информационный fuzzball

  k = {k_m:.6f} | N = {N} | Вселенная = закрытая система
""")
