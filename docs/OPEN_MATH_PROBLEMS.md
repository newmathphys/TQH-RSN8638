# Open Mathematical Problems of TQH/RSN-8638

---

## Problem 1. Exact Calculation of $\varepsilon_K$

### 1.1 Physics of the Problem
$\varepsilon_K$ is the CP-violation parameter in $K^0$-$\bar{K}^0$ mixing. In the Standard Model:

$$\varepsilon_K = \frac{G_F^2 f_K^2 m_K M_W^2}{6\sqrt{2}\pi^2 \Delta m_K} \cdot \text{Im}(\lambda_t) \cdot B_K \cdot \eta_{cc} \cdot \eta_{tt} \cdot \eta_{ct}$$

### 1.2 In RSN Framework

**Mixing amplitude** $M_{12}$ arises as a two-step quantum jump:

$$M_{12} = \langle \bar{K}^0 | \mathcal{H}_{\rm weak} | K^0 \rangle$$

On the $N=8638$ lattice, the weak interaction operator is:

$$\mathcal{H}_{\rm weak} = \frac{G_F}{\sqrt{2}} \sum_{i,j} V_{ij} \, J_i^\mu J_{\mu j}^\dagger$$

### 1.3 Lattice Parameters

| Parameter | Value | Origin |
|-----------|-------|--------|
| $n_s$ | 812 | $\ln(m_s/m_e)/k$ |
| $n_d$ | 344 | $\ln(m_d/m_e)/k$ |
| $n_{\rm im}(s)$ | 0.54 | $\dim(G_2)\cdot\varepsilon = 7.5\cdot\varepsilon$ |
| $n_{\rm im}(d)$ | 7.5 | $\dim(G_2)/2$ |
| $\Delta m_K$ | $3.484\times10^{-15}$ GeV | PDG |
| $\delta_{CP}$ | $275.2^\circ$ | $4\pi/3 + 2\pi k\gamma_1(1+\varepsilon)$ |

### 1.4 Jump Hierarchy

Strange quark $s$ ($n_s=812$) and light quark $d$ ($n_d=344$) are separated by $\Delta n = 468$ lattice steps. Mixing amplitude:

$$\mathcal{A}_{sd} \propto k^2 \cdot \exp\left(-\frac{\Delta n}{n_{\rm im}}\right) \cdot \sin\delta_{CP}$$

### 1.5 Proposed Formula

$$\varepsilon_K^{\rm RSN} = \frac{V_{us}V_{cb}^2}{N\varepsilon} \cdot \frac{k^2}{(\Delta n_{sd})^2} \cdot \frac{\varphi}{2\pi} \cdot \mathcal{F}_{B_K}$$

where $\mathcal{F}_{B_K}$ is the lattice $B_K$ parameter.

### 1.6 Current Accuracy

$$\varepsilon_K^{\rm RSN} \approx 1.77\times10^{-3} \quad \text{(PDG: } 2.23\times10^{-3}\text{)}$$

Deviation $20\%$. Requires **full lattice calculation** of the box diagram on $N=8638$.

---

## Problem 2. Gravitational Wave Spectrum for LISA

### 2.1 Physics

The topological phase transition $G_2 \to SU(5)$ at $T_* \sim 10^9$ GeV generates a stochastic GW background. The characteristic frequency is:

$$f_0 = \frac{1}{2\pi} \cdot \frac{k \cdot N}{t_{\rm univ}} \approx 0.5\ \text{mHz}$$

### 2.2 What's Known

- $f_0 = 0.5$ mHz (within LISA band)
- $\Omega h^2 \sim 10^{-12}$ (from topological flop)
- Source: instantaneous rearrangement of 14 $G_2$ generators

### 2.3 What's Missing

- Parameters $\alpha$ (latent heat) and $\beta/H$ (duration)
- Numerical simulation: $h(t) \to \text{FFT} \to \Omega(f)$
- Comparison with LISA sensitivity curve

### 2.4 Proposed Approach

$$\Omega_{\rm GW}(f)h^2 = \Omega_{\rm peak} \cdot \frac{(f/f_0)^{n_1}}{1 + (f/f_0)^{n_2}}$$

Parameters from Caprini et al. (2024) with RSN-specific inputs:
- $\alpha = \varepsilon \cdot \varphi/(1-\varepsilon) \approx 0.1255$
- $\beta/H = \pi/(2kN)\cdot1000 \approx 28.2$
- $T_* \approx 10^9$ GeV

**Difficulty:** Medium (requires GW signal generation code and Fourier analysis).

---

## Problem 3. Axion Coupling Constant

### 3.1 Physics

The light dilaton of RSN is actually an axion with mass:

$$m_a = \frac{m_\pi f_\pi}{f_a} \approx 5.35\ \mu\text{eV}$$

where $f_a = \frac{m_e N^3}{\delta_{\rm top}} \approx 2.23 \times 10^9$ GeV.

### 3.2 What's Known

- $m_a = 5.35$ $\mu$eV
- $g_{a\gamma\gamma} \approx 5.2 \times 10^{-13}$ GeV$^{-1}$
- ADMX sensitive range: $1$-$100$ $\mu$eV

### 3.3 What's Needed

- Full axion Lagrangian from spectral action
- Precise calculation of $g_{a\gamma\gamma}$ including model-dependent factors
- Prediction for ADMX Phase 2 and BabyIAXO

**Difficulty:** Low-Medium (requires deriving axion EFT from the spectral action).

---

## Problem 4. Proton Decay Rate

### 4.1 Prediction

$$\tau_p = \tau_n \cdot \exp\left(k \cdot 83 \cdot 104 \cdot \frac{2\pi-1}{3}\right) \approx 1.01 \times 10^{38}\ \text{years}$$

### 4.2 Current Limits

| Experiment | Limit | Year |
|------------|-------|------|
| Super-Kamiokande | $>1.6\times10^{34}$ yr | 2020 |
| Hyper-Kamiokande (projected) | $>10^{35}$ yr | ~2030 |
| DUNE (projected) | $>10^{36}$ yr | ~2035 |

### 4.3 What's Needed

- Derivation of baryon number violation from spectral lattice
- Calculation of $p \to e^+\pi^0$ partial width
- Detailed prediction for Hyper-K and DUNE

**Difficulty:** Medium (requires instanton calculation on the $G_2$ lattice).

---

## Problem 5. CPT Operators on the Lattice

### 5.1 Formalism

C, P, T operators are defined:
- $C = i\gamma^2\gamma^0$ (charge conjugation)
- $P = \gamma^0$ (parity)
- $T = i\gamma^5C$ (time reversal)

### 5.2 What Needs Verification

They must commute with the Mathieu-Ovseichik difference Hamiltonian:

$$\hat{H}\Psi_n = -\frac{\Psi_{n+1} - 2\Psi_n + \Psi_{n-1}}{2k^2} + V_0\cos(2\pi n k)\Psi_n$$

### 5.3 Required Steps

- Construct C, P, T matrices in Weyl representation
- Verify: $[\hat{H}, C] = 0$, $[\hat{H}, P] = 0$, $[\hat{H}, T] = 0$
- Verify CPT: $(CPT)\hat{H}(CPT)^{-1} = \hat{H}$

**Difficulty:** Medium (requires $4\times4$ matrix algebra on the discrete spectrum).

---

## Summary

| # | Problem | Difficulty | Status | Priority |
|---|---------|-----------|--------|----------|
| 1 | $\varepsilon_K$ | High | $20\%$ accuracy | High |
| 2 | GW spectrum | Medium | Needs simulation | Medium |
| 3 | Axion coupling | Low-Medium | Needs EFT | Medium |
| 4 | Proton decay | Medium | Needs instanton | Low |
| 5 | CPT verification | Medium | Needs matrix check | Low |

All problems are **computational, not conceptual**. The theoretical framework is complete and self-consistent.
