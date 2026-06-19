"""Ω_GW h² для LISA: спектр ГВ от топологического флопа G₂→SU(5).
Запуск: python3 tests/test_gw_lisa_spectrum.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

k = 14.1347251417 / (16 * 137.036)
N = 8638
n_gut = 7342
f0_mHz = 0.001 * 91 * k * 1000  # 0.587 mHz

SAVE = 'docs/figures_gw_lisa'
os.makedirs(SAVE, exist_ok=True)

print("="*70)
print("СПЕКТР ГВ ОТ G₂→SU(5) ДЛЯ LISA")
print("="*70)
print(f"f₀ = {f0_mHz:.3f} mHz")

# Моделирование: топологический флоп → сигнал h(t)
# Флоп G₂→SU(5) — мгновенная перестройка 14 генераторов
# Сигнал: затухающая синусоида (кольца после флопа)
t = np.linspace(0, 1000, 10000)  # условное время
tau = 50  # время затухания
h0 = 1e-18  # амплитуда

# Сигнал: суперпозиция гармоник от 14 генераторов
h_t = np.zeros_like(t)
for i in range(1, 8):  # 7 гармоник (половина от 14)
    f_i = f0_mHz * i / 1000  # в Гц
    h_t += h0 / i * np.sin(2*np.pi * f_i * t) * np.exp(-t/tau)

# FFT
dt = t[1] - t[0]
freqs = np.fft.rfftfreq(len(t), dt)
h_f = np.fft.rfft(h_t)
Omega = np.abs(h_f)**2 * freqs**2  # ∝ h²f²

# Кривая чувствительности LISA
f_lisa = np.logspace(-4, 0, 500)
S_lisa = 1e-20 * (1 + (f_lisa/1e-2)**(-2) + (f_lisa/1e-3)**2)

print(f"Пик Ω = {np.max(Omega):.2e}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Временной сигнал
ax1.plot(t[:500], h_t[:500], 'darkblue', lw=1)
ax1.set_xlabel('t (усл.)'); ax1.set_ylabel('h(t)')
ax1.set_title('Сигнал ГВ от топологического флопа G₂→SU(5)')
ax1.grid(alpha=0.3)

# Спектр + LISA
ax2.loglog(freqs[freqs>0], Omega[freqs>0], 'darkred', lw=2, label='RSN G₂→SU(5)')
ax2.loglog(f_lisa, S_lisa, 'gray', ls='--', label='LISA sensitivity')
ax2.axhline(1e-3, color='red', ls=':', alpha=0.5)
ax2.axvline(f0_mHz/1000, color='blue', ls=':', alpha=0.5, label=f'f₀={f0_mHz:.2f} mHz')
ax2.set_xlabel('f (Hz)'); ax2.set_ylabel('ΩGW h²')
ax2.set_title('Спектр: RSN vs LISA')
ax2.legend(fontsize=8); ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(f'{SAVE}/gw_lisa_spectrum.png', dpi=150)
print(f"✅ График: {SAVE}/gw_lisa_spectrum.png")
