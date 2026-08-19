
## 1. Foundations of Portfolio Theory & Decision Framework

Modern Portfolio Theory (MPT) provides a mathematical framework for assembling a portfolio of assets such that expected return is maximized for a given level of risk.

```
Investment Timeline:
Time 0 (Present Decision) ---------------------> Time 1 (Future Outcome)
Commit capital based on                           Evaluate realized returns
expected return & uncertainty                     and carry systematic risk

```

* **Portfolio Definition**: A curated collection of financial assets (such as equities, bonds, or cash equivalents) held simultaneously to achieve a specified financial objective.

* **The Dual Investment Pillars**:
	* **Expected Return (Reward)**: The anticipated gain an investor expects to generate over a specified holding period.
	* **Risk (Uncertainty)**: The probability distribution of potential outcomes where realized returns deviate from expected returns.

* **Investment Horizon**: Decisions are made ex-ante at time $t_0$ (present) under uncertainty and evaluated ex-post at time $t_1$ (future realization).

* **Visualizing Risk via Dispersion**:
	* **Low-Risk Asset**: Narrow, tall probability distribution (tight clustering around the mean; low uncertainty).
	* **High-Risk Asset**: Wide, flat distribution (broad range of possible outcomes ranging from severe capital erosion to large gains).

* **The Rational Investor Rule**: Given two assets with identical expected returns, a rational investor will always select the asset with the lower dispersion of returns (lower risk).

---

## 2. Risk and Return for a Single Asset

Financial analysis transforms raw historical market prices into statistical metrics for decision-making.

### Market Data vs. Corporate Accounting Data

* **Corporate Accounting Data**: Financial statements and board disclosures are historical, published at discrete intervals, and susceptible to accounting manipulation.

* **Market Price Data**: Continuously traded, publicly accessible, forward-looking, and reflects the collective consensus of all market participants.

* **Stylized Properties of Asset Prices**: Financial time series are sequentially ordered, evenly spaced across trading intervals, exhibit volatility clustering (periods of calm followed by turbulence), and display significant noise.

### Mathematical Formulation of Single-Asset Metrics

* **Simple Periodic Return ($R_t$)**:
Converts a pair of sequential prices into a percentage return:

$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$$

(Note: A dataset containing $n$ sequential closing prices yields $n - 1$ return periods.)

* **Expected / Mean Return ($\bar{R}$)**:
The arithmetic mean of all calculated periodic returns:

$$\bar{R} = \frac{1}{n} \sum_{t=1}^{n} R_t$$

* **Sample Standard Deviation ($\sigma$)**:
The statistical measure of dispersion around the mean, representing total risk:

$$\sigma = \sqrt{\frac{\sum_{t=1}^{n} (R_t - \bar{R})^2}{n - 1}}$$

* **Spread**: $\sigma$ measures how far returns stray from their average.

* **Units**: Expressed in the exact same unit as the underlying periodic returns (e.g., daily percentage).

* **Excel Syntax**: `=STDEV.S(return_range)`.

---

## 3. Portfolio Mathematics: Risk, Diversification, and Correlation

The objective of portfolio construction is to combine individual assets such that their joint behavior creates a superior risk-return profile compared to holding any individual asset alone.

```
                     Total Portfolio Risk (sigma)
                                  |
        +-------------------------+-------------------------+
        |                                                   |
Unsystematic Risk (Idiosyncratic)             Systematic Risk (Market)
- Company-specific events                    - Economy-wide shocks
- Diversifiable via large N                  - Irreducible market floor
- Shocks offset across assets                - Measured by Beta (beta)

```

### The Two-Asset Portfolio Equations

* **Portfolio Expected Return ($E(R_p)$)**:
The weighted linear combination of individual asset returns:

$$E(R_p) = w_A E(R_A) + w_B E(R_B)$$

*Subject to*:

$$w_A + w_B = 1 \quad \text{where } w_A, w_B \ge 0 \text{ (for long-only portfolios)}$$

* **Portfolio Standard Deviation ($\sigma_p$)**:
Unlike return, portfolio risk is **non-linear** and depends on the co-movement of the assets:

$$\sigma_p = \sqrt{w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}}$$

Where:
* $w_A, w_B$ = Capital weight allocated to asset $A$ and asset $B$
* $\sigma_A, \sigma_B$ = Standard deviation (total risk) of asset $A$ and asset $B$
* $\rho_{AB}$ = Correlation coefficient between the returns of asset $A$ and $B$

### The Correlation Coefficient ($\rho$)

The correlation coefficient $\rho_{AB}$ (computed in Excel via `=CORREL(array1, array2)` strictly on **returns**, not raw prices) measures the degree of linear association between two return series.

| Correlation ($\rho$) | Relationship Between Assets                                                                 | Portfolio Diversification Effect                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\rho = +1.0$<br>    | Perfectly positive co-movement; assets rise and fall together in lockstep.                  | **No risk reduction.** Portfolio standard deviation is a simple weighted average: $\sigma_p = w_A\sigma_A + w_B\sigma_B$.                             |
| $0 < \rho < +1.0$    | Imperfect positive co-movement.                                                             | **Moderate diversification.** Portfolio risk is strictly less than the weighted average of individual risks ($\sigma_p < w_A\sigma_A + w_B\sigma_B$). |
| $\rho = 0.0$         | Uncorrelated; movement in one asset provides zero directional predictability for the other. | **Substantial diversification.** Eliminates the covariance term.                                                                                      |
| $\rho = -1.0$        | Perfectly negative co-movement; one asset rises while the other falls in exact proportion.  | **Maximum diversification.** Can construct a completely riskless portfolio ($\sigma_p = 0$) through precise weight calibration.                       |

---

## 4. Decomposing Risk: Systematic vs. Unsystematic

Total risk ($\sigma$) is separated into two fundamentally different components:

```
Portfolio Risk (sigma)
  ^
  |  \
  |   \  <-- Unsystematic Risk (diversifies away rapidly)
  |    \
  |     \________________________ <-- Systematic Risk Floor (irreducible)
  +------------------------------>
  0     10    20    30    40   50+  Number of Stocks Held (N)

```

* **Unsystematic (Idiosyncratic / Specific / Diversifiable) Risk**:
* **Characteristics**: Specific to an individual corporation or narrow industry (e.g., accounting fraud, product recall, factory fires, labor disputes).

* **Behavior**: Hits individual stocks independently. By holding a basket of stocks ($N \ge 20\text{–}30$), independent positive and negative shocks cancel each other out, driving unsystematic risk asymptotically toward zero.

* **Diminishing Marginal Benefit**: The steepest risk reduction occurs when moving from 1 to 10 stocks; adding subsequent stocks yields progressively smaller reductions in risk.

* **Systematic (Market / Non-Diversifiable) Risk**:
	* **Characteristics**: Macroeconomic shocks that affect all market participants simultaneously (e.g., central bank policy rate hikes, sudden currency depreciation, recessions, oil price shocks).
	* **Behavior**: Cannot be diversified away regardless of the number of stocks added ($N \to \infty$). It forms an irreducible structural risk floor.

| Feature                            | Unsystematic Risk                                              | Systematic Risk                                         |
| ---------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------- |
| **Alternative Names**              | Idiosyncratic, Specific, Unique, Diversifiable                 | Market, Non-Diversifiable, Undiversifiable              |
| **Source**                         | Company/industry-specific events                               | Macroeconomic & structural forces                       |
| **Examples**                       | Satyam/Enron fraud, factory fire, failed product               | RBI repo rate shifts, GDP contraction, crude oil spikes |
| **Eliminated by Diversification?** | **Yes** (approaches zero as $N$ increases)                     | **No** (forms the irreducible risk floor)               |
| **Priced by Market?**              | **No** (market does not pay a risk premium for avoidable risk) | **Yes** (compensated via the equity risk premium)       |

---

## 5. The Markowitz Efficient Frontier

Harry Markowitz (1952) formalized portfolio selection by showing that varying asset allocation weights ($w_i$) traces out a risk-return opportunity set in Expected Return vs. Standard Deviation ($\sigma$) space.

```
Expected Return E(R)
  ^
  |           /------------------- Efficient Frontier (Rational Region)
  |          / (Upper Curve)
  |         * MVP (Minimum Variance Portfolio)
  |          \
  |           \------------------- Dominated Set (Inefficient Region)
  +------------------------------>
  0                              Portfolio Risk (sigma)

```

* **The Opportunity Set / Feasible Region**: A sideways bullet-shaped curve traced by calculating risk and return across varying allocation combinations ($w_A$ from 0% to 100%).

* **Minimum Variance Portfolio (MVP)**: The leftmost apex of the bullet curve representing the portfolio combination with the absolute lowest achievable standard deviation ($\sigma_p$).

* **The Efficient Frontier**: The upper portion of the curve extending upwards from the MVP. Portfolios on this boundary maximize expected return for a given level of risk, or minimize risk for a target expected return.

* **Dominated (Inefficient) Portfolios**: The lower portion of the curve below the MVP. For every portfolio on the lower limb, there exists an efficient portfolio directly above it that delivers higher expected return at the exact same risk level. Rational investors never hold dominated portfolios.

* **The Market Portfolio ($M$)**: When expanded to include all risky assets in the economy weighted by market capitalization, unsystematic risk is fully eliminated, leaving only systematic risk. In practice, this is proxied by broad market indices such as the Nifty 50, BSE Sensex, or S&P 500.

---

## 6. The Capital Asset Pricing Model (CAPM)

Developed by William Sharpe, John Lintner, and Jan Mossin (1960s), CAPM builds on Markowitz's theory. Because rational investors eliminate unsystematic risk via diversification, **the market does not compensate investors for total risk ($\sigma$), but solely for systematic risk ($\beta$)**.

### The CAPM Equation

$$E(R_i) = R_f + \beta_i \left[ E(R_m) - R_f \right]$$



| Term                    | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| E(R_i)                  | Required / Expected return on asset i                 |
| R_f                     | Risk-free rate (pure time value of money)             |
| E(R_m)                  | Expected return of the broad market index             |
| [E(R_m) - R_f]          | Market Risk Premium (reward for bearing average risk) |
| beta_i                  | Systematic risk sensitivity of asset i                |
| beta_i * [E(R_m) - R_f] | Asset-specific Risk Premium                           |

### Sourcing CAPM Inputs (Indian Market Context)

* **Risk-Free Rate ($R_f$)**: Yield on zero-default-risk sovereign paper, typically sourced from 91-day Government of India Treasury Bills (T-Bills) or the 10-year Government Securities (G-Sec) yield published by the Reserve Bank of India (RBI).

* **Market Return ($E(R_m)$)**: Expected long-term return of broad benchmark indices such as Nifty 50 or BSE Sensex (historically 12% to 15% in India).

* **Market Risk Premium ($E(R_m) - R_f$)**: The additional return above sovereign cash demanded by investors to bear broad equity volatility (typically 5% to 9%).

### Estimating and Interpreting Beta ($\beta$)

Beta represents the slope of the **Security Characteristic Line (SCL)**, which regresses excess asset returns against excess market returns:

$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$$

* **Excel Implementation**:
`=SLOPE(Stock_Return_Series, Market_Return_Series)`
(Note: The dependent variable Y = Stock Returns, independent variable X = Market Returns.)

| Beta Range            | Classification                | Market Sensitivity & Asset Characteristics                                             | Typical Sector Examples                                       |
| --------------------- | ----------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **$\beta > 1.0$**<br> | **Aggressive**<br>            | Amplifies market movements in both directions; higher systematic risk than the market. | Small-cap stocks, Metals, Real Estate, High-growth Tech       |
| **$\beta = 1.0$**     | **Market Benchmark**          | Moves in perfect lockstep with benchmark systematic volatility.                        | Broad index funds, Large-cap diversified market proxies       |
| **$0 < \beta < 1.0$** | **Defensive**                 | Mutes market swings; less volatile than the overall market index.                      | Fast-Moving Consumer Goods (FMCG), Pharmaceuticals, Utilities |
| **$\beta < 0$**       | **Negative Beta (Insurance)** | Moves counter to the general market direction; serves as natural portfolio hedge.      | Gold ETFs, specialized inverse hedging instruments            |

---

## 7. Mathematical & Practical Implementations

### Worked Problem 1: Two-Asset Portfolio Return and Risk Computation

**Input Parameters**:

* Asset A (ABC Ltd): Expected Return $E(R_A) = -1.23\%$, Standard Deviation $\sigma_A = 1.66\%$, Weight $w_A = 0.30$

* Asset B (XYZ Ltd): Expected Return $E(R_B) = -0.42\%$, Standard Deviation $\sigma_B = 2.07\%$, Weight $w_B = 0.70$

* Correlation coefficient: $\rho_{AB} = 0.33$

**Step 1: Expected Portfolio Return**:

$$E(R_p) = (0.30 \times -1.23\%) + (0.70 \times -0.42\%) = -0.369\% - 0.294\% = -0.663\% \approx -0.66\%$$

**Step 2: Portfolio Variance ($\sigma_p^2$)**:

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}$$
$$\sigma_p^2 = (0.30)^2(1.66)^2 + (0.70)^2(2.07)^2 + 2(0.30)(0.70)(1.66)(2.07)(0.33)$$
$$\sigma_p^2 = 0.09(2.7556) + 0.49(4.2849) + 2(0.21)(1.66)(2.07)(0.33)$$
$$\sigma_p^2 = 0.2480 + 2.0996 + 0.4764 = 2.8240$$

**Step 3: Portfolio Standard Deviation ($\sigma_p$)**:

$$\sigma_p = \sqrt{2.8240} \approx 1.68\%$$

*Analytical Insight*: The simple weighted average of risk is $(0.30 \times 1.66\%) + (0.70 \times 2.07\%) = 1.947\%$. Because $\rho_{AB} = 0.33 < 1$, the combined risk drops to **1.68%**, demonstrating the diversification effect.

---

### Worked Problem 2: SCL Capital Asset Pricing Model Valuation

**Scenario**: Calculate the required rate of return for an asset given the following Indian market conditions:

* Risk-free rate ($R_f$) = 6.0% (RBI 10-Yr G-Sec)
* Expected Market Return ($E(R_m)$) = 15.0% (Nifty 50 benchmark)
* Stock Beta ($\beta_i$) = 1.20 (Aggressive Equity)

**Step 1: Calculate the Market Risk Premium**:

$$\text{MRP} = E(R_m) - R_f = 15.0\% - 6.0\% = 9.0\%$$

**Step 2: Apply the CAPM Formula**:

$$E(R_i) = R_f + \beta_i [E(R_m) - R_f]$$
$$E(R_i) = 6.0\% + 1.20(9.0\%) = 6.0\% + 10.8\% = 16.8\%$$

---

### Worked Problem 3: Solving for Implied Systematic Risk ($\beta$)

**Scenario**: An asset offers an expected return of $E(R_i) = 24.0\%$ in an economy where $R_f = 6.0\%$ and $E(R_m) = 15.0\%$. Determine the asset's Beta.

$$\beta_i = \frac{E(R_i) - R_f}{E(R_m) - R_f} = \frac{24.0\% - 6.0\%}{15.0\% - 6.0\%} = \frac{18.0\%}{9.0\%} = 2.0$$

*Interpretation*: The asset carries twice the systematic risk of the broad market index ($\beta = 2.0$), requiring an 18.0% risk premium above the baseline risk-free rate.

---

### Total Risk ($\sigma$) vs. Systematic Risk ($\beta$)

| Dimension               | Total Risk ($\sigma$)                                           | Systematic Risk ($\beta$)                                                                     |
| ----------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Core Measurement**    | Total dispersion/volatility around the asset's individual mean. | Co-movement sensitivity relative to broad market fluctuations.                                |
| **Statistical Formula** | $\sigma = \sqrt{\frac{\sum (R_t - \bar{R})^2}{n-1}}$            | $\beta = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$                                        |
| **Composition**         | Systematic Risk + Unsystematic Risk                             | Pure Systematic Risk                                                                          |
| **Relevance**           | Evaluates standalone assets or undiversified portfolios.        | Determines pricing and required return for fully diversified investors in equilibrium (CAPM). |

Through this progression—from single-stock dispersion to correlation matrices, the efficient frontier, and CAPM equilibrium—modern finance demonstrates that asset pricing and portfolio construction depend not on an asset's standalone volatility, but on the systematic risk it contributes to a diversified portfolio.