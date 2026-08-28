## 1: The Foundations of Investment — Risk, Return, and the Horizon

### 1.1 First Principles: The Core Duality of Investing

Every financial investment balances two fundamental forces: **Return** (the prospective reward) and **Risk** (the uncertainty of that reward).

- **Return (Reward):** The percentage change in the value of an asset over a given holding period. If you invest capital into an asset (such as shares of Infosys or ABC Ltd.), the return represents the financial gain or loss you realize.
    
- **Risk (Uncertainty):** The dispersion of possible outcomes around what you expect to happen. In finance, risk is not merely the possibility of permanent loss; it is the degree of unpredictability regarding the future price.

A rational investor never evaluates return in isolation. Higher potential returns exist in competitive markets precisely to compensate investors for bearing greater uncertainty.

### 1.2 The Investment Horizon: Reasoning from $t=0$ to $t=1$

Financial decisions are structured across time:

```
Time t = 0 (Present) -----------------------------------> Time t = 1 (Future)
Decision Point: Capital Allocation                        Evaluation: Realized Return & Risk
```

- **$t = 0$ (The Decision Point):** You analyze available market data, evaluate opportunities, and commit capital. All expectations are formulated at $t=0$ under conditions of uncertainty.
    
- **$t = 1$ (The Realization Point):** The investment horizon concludes. The uncertain future has collapsed into a single historical fact: the realized return.

The absolute duration between $t=0$ and $t=1$ varies by market participant—ranging from milliseconds for high-frequency algorithmic traders to decades for pension funds—but the analytical framework remains identical.

### 1.3 Visualizing Risk: The Return Distribution

If an asset's return at $t=1$ is uncertain, it can be modeled as a probability distribution (often approximated by a normal or bell-shaped curve).

```
        Low-Risk Asset (Narrow & Tall)          High-Risk Asset (Wide & Flat)
                  |                                          |
                 / \                                         |
                /   \                                       / \
               /     \                                    /     \
             /         \                                /         \
           /             \                            /             \
  --------/---------------\--------          --------/---------------\--------
      -10%      0%      +10%                    -90%        0%      +200%
```

- **Low-Risk Asset:** The distribution is tall and narrow. Future outcomes cluster tightly around the expected average (e.g., between $-10\%$ and $+10\%$). The range of possibilities is compressed, making the asset predictable.
     
- **High-Risk Asset:** The distribution is wide and flat. The asset could yield massive gains ($+200\%$) or catastrophic losses ($-90\%$). The broad spread reflects high uncertainty.
 
**Core Principle:** The _width_ (spread) of the probability distribution is risk made visible.

### 1.4 Measuring Risk: Standard Deviation ($\sigma$)

To compare assets quantitatively, finance uses **Standard Deviation**, denoted by the Greek letter **$\sigma$ (Sigma)**.

$$\sigma = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(R_i - \bar{R})^2}$$

- $\sigma$ measures how far individual returns deviate from their arithmetic average ($\bar{R}$).
    
- Because $\sigma$ is expressed in the exact same units as returns (percentage points, $\%$), it provides a direct yardstick for volatility.
    
- **Large $\sigma$:** Wide spread, high volatility, high risk.
    
- **Small $\sigma$:** Tight spread, low volatility, low risk.

### 1.5 The Axiom of the Rational Investor

Modern financial theory rests on the assumption that investors are **risk-averse**:

| **Investment** | **Expected Return (E[R])** | **Risk (σ)**  | **Rational Choice** |
| -------------- | -------------------------- | ------------- | ------------------- |
| **Option A**   | $12\%$                     | $18\%$ (High) | Rejected            |
| **Option B**   | $12\%$                     | $6\%$ (Low)   | **Accepted**        |

Given two assets with the same expected return, a rational investor will **always** choose the asset with the lower standard deviation ($\sigma$). An investor only accepts higher $\sigma$ if compensated with a higher expected return.

---

## 2: Quantifying Return and Risk for a Single Asset

### 2.1 The Nature of Financial Data

Financial markets generate continuous time-series data characterized by key statistical properties:

1. **Chronological Sequence:** Observations are ordered strictly across time ($t_0, t_1, t_2, \dots, t_n$).
    
2. **Even Discretization:** Asset prices are recorded at regular intervals (daily closing prices, hourly intervals, etc.).
     
3. **Volatility Clustering:** Periods of market calm are typically followed by calm, while volatile shocks cluster together.
     
4. **Noise:** Short-term price changes contain significant random fluctuation.
 
Market prices reflect the aggregate buying and selling decisions of all participants simultaneously, updating in real time as new information arrives.

### 2.2 From Raw Prices to Percentage Returns

Raw stock prices cannot be directly compared across companies because share counts and nominal price levels differ arbitrarily. A ₹10 move on a ₹100 stock is a $10\%$ shift, whereas a ₹10 move on a ₹10,000 stock is a $0.1\%$ shift. We therefore normalize price series into **percentage returns**.

The simple return $R_t$ from period $t-1$ to period $t$ is calculated as:

$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$$

Where:

- $P_t$ = Asset price at the current period $t$.
    
- $P_{t-1}$ = Asset price at the prior period $t-1$.

_Note on Sample Size:_ Converting a series of $N$ discrete closing prices yields exactly $N-1$ periodic returns, because the initial price ($P_0$) has no preceding baseline.

### 2.3 Mathematical Derivations: Mean and Variance

#### 1. Arithmetic Mean Return ($\bar{R}$ or $E[R]$)

The average return measures the central tendency or expected reward over the sample period:

$$\bar{R} = \frac{1}{n}\sum_{t=1}^{n} R_t$$

Where $n$ is the total number of return periods ($N-1$).

#### 2. Sample Variance ($s^2$ or $\sigma^2$)

Variance measures the average squared deviation of individual returns from the mean return:

$$\sigma^2 = \frac{\sum_{t=1}^{n} (R_t - \bar{R})^2}{n - 1}$$

We divide by $n - 1$ rather than $n$ (known as **Bessel’s Correction**) to calculate an unbiased estimate of the population variance from sample data.

#### 3. Sample Standard Deviation ($\sigma$)

Taking the square root of variance returns the risk metric to the original percentage scale:

$$\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{t=1}^{n} (R_t - \bar{R})^2}{n - 1}}$$

### 2.4 Worked Example: Single-Stock Return and Risk

Consider a hypothetical 5-day daily closing price series for Stock ABC:

| **Day (t)** | **Closing Price (Pt​)** | **Return Calculation (Rt​=Pt−1​Pt​−Pt−1​​)** | **Daily Return (Rt​)** | **Deviation (Rt​−Rˉ)** | **Squared Deviation (Rt​−Rˉ)2** |
| ----------- | ----------------------- | -------------------------------------------- | ---------------------- | ---------------------- | ------------------------------- |
| **0**       | ₹100.00                 | Baseline                                     | —                      | —                      | —                               |
| **1**       | ₹102.50                 | $(102.50 - 100.00) / 100.00$                 | $+2.50\%$ ($+0.0250$)  | $+0.0225$              | $0.00050625$                    |
| **2**       | ₹99.00                  | $(99.00 - 102.50) / 102.50$                  | $-3.41\%$ ($-0.0341$)  | $-0.0366$              | $0.00133956$                    |
| **3**       | ₹101.00                 | $(101.00 - 99.00) / 99.00$                   | $+2.02\%$ ($+0.0202$)  | $+0.0177$              | $0.00031329$                    |
| **4**       | ₹100.50                 | $(100.50 - 101.00) / 101.00$                 | $-0.50\%$ ($-0.0050$)  | $-0.0075$              | $0.00005625$                    |

**Step 1: Calculate the Mean Daily Return ($\bar{R}$)**

$$\bar{R} = \frac{0.0250 - 0.0341 + 0.0202 - 0.0050}{4} = \frac{0.0061}{4} = 0.002525 \approx +0.25\%$$

**Step 2: Sum the Squared Deviations**

$$\sum (R_t - \bar{R})^2 = 0.00050625 + 0.00133956 + 0.00031329 + 0.00005625 = 0.00221535$$

**Step 3: Compute Sample Variance ($\sigma^2$) with $n - 1 = 3$**

$$\sigma^2 = \frac{0.00221535}{4 - 1} = \frac{0.00221535}{3} \approx 0.00073845$$

**Step 4: Compute Standard Deviation ($\sigma$)**

$$\sigma = \sqrt{0.00073845} \approx 0.02717 \approx 2.72\%$$

- **Summary Metrics:** Average Daily Return ($\bar{R}$) = $+0.25\%$, Daily Risk ($\sigma$) = $2.72\%$.

---

## 3: Diversification, Correlation, and Two-Asset Portfolios

### 3.1 The Two Types of Risk

Total risk ($\sigma$) breaks down into two distinct economic forces:

```
                                Total Risk (σ)
                                      |
         +----------------------------+----------------------------+
         |                                                         |
Unsystematic Risk (Idiosyncratic)                           Systematic Risk (Market)
- Firm-specific events                                     - Economy-wide events
- Diversifiable to 0                                       - Non-diversifiable floor
- Examples: Fraud, factory fires, product failure          - Examples: Interest rates, inflation, recessions
```

#### Unsystematic Risk (Company-Specific, Unique, Idiosyncratic)

- **Definition:** Risk factors specific to an individual firm or industry.
    
- **Examples:** An accounting scandal at Enron or Satyam, an engine emissions lawsuit at Volkswagen, a factory fire, or a failed drug trial.
    
- **Mechanism:** These events occur independently. While one company faces a negative idiosyncratic shock, another experiences a positive breakthrough. Across a basket of stocks, these individual shocks average out to zero.

#### Systematic Risk (Market-Wide, Non-Diversifiable)

- **Definition:** Macroeconomic forces that influence all operating businesses simultaneously.
    
- **Examples:** Central bank monetary policy changes (e.g., Reserve Bank of India rate hikes), national budget announcements, global recessions, or crude oil supply shocks.
    
- **Mechanism:** Because these forces impact the entire financial system at once, holding additional stocks cannot eliminate them.

### 3.2 The Mathematics of the Diversification Curve

As you add randomly selected stocks to an equity portfolio, total risk drops non-linearly:

```
Portfolio Risk (σ)
   ^
   |  \
   |   \  <-- Unsystematic Risk (Melts away with diversification)
   |    \
   |     ' - - - - - - - - - - - - - - - - - - - - - - -
   |==================================================== <-- Systematic Risk Floor
   |                                                         (Cannot be eliminated)
   +---------------------------------------------------->
   0     5     10    15    20    25    30    35    40    Number of Stocks Held
```

- **Steep Initial Drop:** Increasing portfolio size from 1 stock to 10–20 stocks eliminates the vast majority of unsystematic risk.
    
- **Diminishing Returns:** Moving from 30 stocks to 500 stocks removes only marginal residual variance.
    
- **The Systematic Floor:** The portfolio variance asymptotically approaches the average covariance among all assets in the market. No degree of diversification can push portfolio risk below this systematic boundary.

### 3.3 Correlation ($\rho$): The Mathematical Engine of Diversification

The diversification effect depends on how assets move relative to one another, quantified by the **Correlation Coefficient ($\rho$)**.

$$\rho_{AB} = \frac{\text{Cov}(R_A, R_B)}{\sigma_A \sigma_B} = \frac{\sum (R_{A,t} - \bar{R}_A)(R_{B,t} - \bar{R}_B)}{\sqrt{\sum (R_{A,t} - \bar{R}_A)^2 \sum (R_{B,t} - \bar{R}_B)^2}}$$

The correlation coefficient is bounded strictly between $-1.0$ and $+1.0$:

|**Value of Correlation (ρAB​)**|**Real-World Interaction**|**Impact on Portfolio Risk (σp​)**|
|---|---|---|
|$\rho = +1.0$ (Perfect Positive)|Assets move in lockstep|**No risk reduction.** $\sigma_p$ is simply the weighted average of individual risks.|
|$0.0 < \rho < +1.0$ (Imperfect Positive)|Assets generally move together, but not identically|**Significant risk reduction.** $\sigma_p$ is lower than the weighted average risk.|
|$\rho = 0.0$ (Uncorrelated)|Asset movements share no linear relationship|**Strong risk reduction.** Large diversification benefits.|
|$\rho = -1.0$ (Perfect Negative)|Assets move in exact opposite directions|**Maximum risk reduction.** Portfolio variance can theoretically be reduced to zero.|

### 3.4 Two-Asset Portfolio Mathematics

Let a portfolio consist of two assets, $A$ and $B$, with capital weights $w_A$ and $w_B$.

#### Weight Constraints

$$w_A + w_B = 1.0 \quad \text{where } w_A \ge 0, \; w_B \ge 0 \quad (\text{assuming no short selling})$$

#### Expected Return of the Portfolio ($E[R_p]$)

The expected return is the linear weighted average of the individual expected returns:

$$E[R_p] = w_A E[R_A] + w_B E[R_B]$$

#### Risk (Standard Deviation) of the Portfolio ($\sigma_p$)

Portfolio risk is non-linear and depends directly on the covariance term:

$$\sigma_p = \sqrt{w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}}$$

### 3.5 Numerical Demonstration: The "Missing Risk" Paradox

Consider two assets with the following properties:

- **Asset A (e.g., IT Sector / ABC Ltd.):** $E[R_A] = 10\%$, $\sigma_A = 16\%$
    
- **Asset B (e.g., Energy Sector / XYZ Ltd.):** $E[R_B] = 14\%$, $\sigma_B = 22\%$
    
- **Correlation ($\rho_{AB}$):** $0.20$
    
- **Portfolio Allocation:** $40\%$ in Asset A ($w_A = 0.40$), $60\%$ in Asset B ($w_B = 0.60$)

**1. Calculate Portfolio Expected Return:**

$$E[R_p] = (0.40 \times 10\%) + (0.60 \times 14\%) = 4.0\% + 8.4\% = 12.4\%$$

**2. Calculate Weighted Average Risk (Linear Baseline):**

$$\text{Linear Weighted Average} = (0.40 \times 16\%) + (0.60 \times 22\%) = 6.4\% + 13.2\% = 19.6\%$$

**3. Calculate True Portfolio Risk ($\sigma_p$):**

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}$$
$$\sigma_p^2 = (0.40)^2 (16)^2 + (0.60)^2 (22)^2 + 2(0.40)(0.60)(16)(22)(0.20)$$
$$\sigma_p^2 = (0.16 \times 256) + (0.36 \times 484) + 2(0.24)(352)(0.20)$$
$$\sigma_p^2 = 40.96 + 174.24 + 33.792 = 248.992$$
$$\sigma_p = \sqrt{248.992} \approx 15.78\%$$

- **Core Takeaway:** The portfolio risk ($\sigma_p = 15.78\%$) is not only lower than the weighted average ($19.60\%$), but it is lower than the risk of Asset A on its own ($16.0\%$), even though $60\%$ of the portfolio is invested in the higher-risk asset ($22.0\%$). Imperfect correlation causes the individual asset swings to offset one another.

---

## 4: Markowitz Modern Portfolio Theory and the Efficient Frontier

### 4.1 Constructing the Opportunity Set

When an investor varies the allocation weights ($w_A, w_B$) across two or more assets, each weight combination produces a distinct pair of portfolio return ($E[R_p]$) and portfolio risk ($\sigma_p$).

Plotting these combinations with risk ($\sigma$) on the x-axis and expected return ($E[R]$) on the y-axis reveals the **Feasible Set** (or Opportunity Set) of portfolios:

```
Expected Return E[R]
         ^
         |                    Efficient Frontier (Upper Boundary)
         |                    .---*---*---* [100% Asset B]
         |                   /
         |    MVP ->        *
         |                   \
         |                    '---*---* [100% Asset A]
         |                   Dominated Segment (Inefficient)
         +---------------------------------------------------->
         0                                            Risk (σ)
```

### 4.2 The Geometry of the Curve: The Sideways "Bullet"

The resulting curve forms a characteristic sideways bullet shape pointing leftward toward lower risk:

1. **Minimum Variance Portfolio (MVP):** The leftmost point on the bullet. It represents the specific combination of assets that achieves the lowest possible portfolio risk ($\sigma$).
    
2. **The Efficient Frontier (Upper Half):** The segment running upward and to the right from the MVP. For any level of risk, these portfolios offer the maximum achievable expected return.
    
3. **The Dominated Segment (Lower Half):** The segment running downward from the MVP. These portfolios are economically irrational. For any point on this lower branch, there is a portfolio directly above it on the upper branch that delivers a higher return for the exact same risk.

### 4.3 Discrete Portfolio Frontier Table

The table below illustrates an 11-portfolio family constructed by shifting weights in $10\%$ increments between Asset A ($E[R_A] = -1.23\%, \sigma_A = 1.66\%$) and Asset B ($E[R_B] = -0.42\%, \sigma_B = 2.07\%$) with $\rho = 0.33$:

|**Portfolio ID**|**Weight in A (wA​)**|**Weight in B (wB​)**|**Expected Return (E[Rp​])**|**Portfolio Risk (σp​)**|**Classification**|
|---|---|---|---|---|---|
|**P1**|$1.00$ ($100\%$)|$0.00$ ($0\%$)|$-1.23\%$|$1.66\%$|Dominated (Inefficient)|
|**P2**|$0.90$ ($90\%$)|$0.10$ ($10\%$)|$-1.15\%$|$1.56\%$|Dominated (Inefficient)|
|**P3**|$0.80$ ($80\%$)|$0.20$ ($20\%$)|$-1.07\%$|$1.50\%$|Dominated (Inefficient)|
|**P4 (MVP)**|$0.70$ ($70\%$)|$0.30$ ($30\%$)|$-0.99\%$|$1.48\%$|**Minimum Variance Portfolio**|
|**P5**|$0.60$ ($60\%$)|$0.40$ ($40\%$)|$-0.91\%$|$1.50\%$|**Efficient**|
|**P6**|$0.50$ ($50\%$)|$0.50$ ($50\%$)|$-0.83\%$|$1.55\%$|**Efficient**|
|**P7**|$0.40$ ($40\%$)|$0.60$ ($60\%$)|$-0.74\%$|$1.64\%$|**Efficient**|
|**P8**|$0.30$ ($30\%$)|$0.70$ ($70\%$)|$-0.66\%$|$1.76\%$|**Efficient**|
|**P9**|$0.20$ ($20\%$)|$0.80$ ($80\%$)|$-0.58\%$|$1.89\%$|**Efficient**|
|**P10**|$0.10$ ($10\%$)|$0.90$ ($90\%$)|$-0.50\%$|$2.03\%$|**Efficient**|
|**P11**|$0.00$ ($0\%$)|$1.00$ ($100\%$)|$-0.42\%$|$2.07\%$|**Efficient**|

_Note on Negative Return Data:_ If sample returns are negative over a given historical window, the entire bullet curve shifts below the horizontal axis. The underlying mathematical optimization and geometric shape remain identical.

### 4.4 The Logical Endpoint: The Market Portfolio

When Harry Markowitz's framework (1952) is expanded from two assets to all risky assets available in the global economy:

- The individual unsystematic risks of every firm cancel out completely.
    
- The optimal risky portfolio converges into the **Market Portfolio** ($M$), containing every traded risky asset weighted by its relative market capitalization.
    
- In practice, this concept forms the theoretical foundation for **Passive Index Investing** (e.g., investing in broad market indices such as the Nifty 50, BSE Sensex, or S&P 500).

---

## 5: The Capital Asset Pricing Model (CAPM)

### 5.1 From Total Risk ($\sigma$) to Systematic Risk ($\beta$)

Markowitz established that an investor can eliminate unsystematic risk by holding a diversified portfolio.

Because unsystematic risk can be diversified away freely by holding a basket of assets, **the market does not compensate investors for bearing firm-specific risk**. If an investor buys a single stock and suffers when a factory burns down, that risk was avoidable.

The market only compensates investors for bearing **Systematic Risk**—the risk that cannot be diversified away. Therefore, standard deviation ($\sigma$), which captures _total_ risk, is the wrong metric for pricing individual assets in a diversified portfolio. The correct metric is **Beta ($\beta$)**.

```
Standard Deviation (σ) = Total Risk (Systematic + Unsystematic)
Beta (β)               = Systematic Risk Only (Sensitivity to Market Movements)
```

### 5.2 The CAPM Equation and Components

Developed by William Sharpe, John Lintner, and Jan Mossin in the 1960s, the **Capital Asset Pricing Model (CAPM)** defines the equilibrium relationship between the systematic risk of an asset and its required expected return:

$$E[R_i] = R_f + \beta_i \left( E[R_m] - R_f \right)$$

```
Required Return = [Compensation for Time] + [Beta] × [Market Risk Premium]
                    (Risk-Free Baseline)             (Compensation for Market Risk)
```

#### The Four Core Variables

1. **Expected Required Return of Asset $i$ ($E[R_i]$):** The minimum return an investor must demand to justify holding asset $i$.
    
2. **Risk-Free Rate ($R_f$):** The theoretical rate of return on an investment with zero default and reinvestment risk over the holding period. This represents pure compensation for the time value of money.
      
    - _Indian Market Proxy:_ 91-day Government Treasury Bills (T-Bills) or the benchmark 10-year Government of India Sovereign Securities (G-Sec) yield, issued by the RBI.
        
3. **Expected Return of the Market ($E[R_m]$):** The return expected from holding the entire market portfolio.
       
    - _Indian Market Proxy:_ The broad market index (e.g., Nifty 50 or Sensex), which has historically returned roughly $12\% - 15\%$ annually.
         
4. **Market Risk Premium ($E[R_m] - R_f$):** The excess return that the overall stock market provides over the risk-free rate to compensate investors for taking equity risk.
     
5. **Beta of Asset $i$ ($\beta_i$):** The sensitivity of asset $i$'s returns to shifts in the broader market return.
 
### 5.3 Mathematical Estimation of Beta: The Security Characteristic Line (SCL)

Beta is the slope of the linear regression line (**Security Characteristic Line**, or SCL) where the asset's excess returns are plotted against the market's excess returns:

$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)} = \frac{\sigma_{im}}{\sigma_m^2}$$

```
Stock Return (Ri)
       ^                 Security Characteristic Line (SCL)
       |                            /
       |                           /  <-- Slope of this line = Beta (β)
       |                          /
       |                         /
-------+------------------------/------------------------> Market Return (Rm)
       |                       /
       |                      /
       |                     /
```

- In spreadsheet software (e.g., Excel/Google Sheets), beta is computed directly:
    
    `=SLOPE(known_y's, known_x's)` where `known_y's` is the column of Stock Returns and `known_x's` is the column of Market Returns.

### 5.4 Comprehensive Interpretation of Beta Values

|**Beta (β) Range**|**Classification**|**Sensitivity & Behavior**|**Asset Class / Sector Examples**|
|---|---|---|---|
|**$\beta > 1.0$**|**Aggressive**|Amplifies market movements in both directions. If the market rises by $10\%$, a stock with $\beta = 1.5$ is expected to rise by $15\%$. If the market drops by $10\%$, it falls by $15\%$.|Small-cap stocks, High-growth Tech, Real Estate, Metals & Mining.|
|**$\beta = 1.0$**|**Neutral / Market-Index**|Moves in exact lockstep with the broad market index.|Nifty 50 Index Fund, diversified mega-cap equities.|
|**$0.0 < \beta < 1.0$**|**Defensive**|Mutes market swings. If the market falls by $10\%$, an asset with $\beta = 0.5$ is expected to drop by only $5\%$.|Fast-Moving Consumer Goods (FMCG), Pharmaceuticals, Regulated Electric Utilities.|
|**$\beta = 0.0$**|**Risk-Free**|Returns are completely decoupled from market fluctuations.|Cash, Sovereign Treasury Bills.|
|**$\beta < 0.0$**|**Negative / Hedging Asset**|Moves in the opposite direction of the market. Provides built-in portfolio insurance during market crashes.|Gold / Gold ETFs, dedicated short/hedging vehicles.|

### 5.5 Step-by-Step CAPM Calculations

#### Scenario A: Computing Required Return from Known Inputs

Assume the following data for an Indian equity asset:

- Sovereign Risk-Free Rate ($R_f$) = $6.0\%$ (10-Year G-Sec yield)
     
- Expected Market Return ($E[R_m]$) = $15.0\%$ (Nifty 50 historical average)
     
- Stock Beta ($\beta$) = $1.20$
 
**Step 1: Compute the Market Risk Premium (MRP)**

$$\text{MRP} = E[R_m] - R_f = 15.0\% - 6.0\% = 9.0\%$$

**Step 2: Calculate the Security Risk Premium**

$$\text{Security Risk Premium} = \beta \times (E[R_m] - R_f) = 1.20 \times 9.0\% = 10.8\%$$

**Step 3: Solve for Expected Required Return ($E[R]$)**

$$E[R] = R_f + \text{Security Risk Premium} = 6.0\% + 10.8\% = 16.8\%$$

- **Interpretation:** Because the stock carries $20\%$ more systematic risk than the broader market ($\beta = 1.20$), investors require a $10.8\%$ premium over the safe rate, demanding a total expected return of $16.8\%$.

#### Scenario B: Solving Backwards for Beta

Assume an analyst observes a high-volatility stock with:

- Required Return ($E[R_i]$) = $24.0\%$
    
- Risk-Free Rate ($R_f$) = $6.0\%$
    
- Expected Market Return ($E[R_m]$) = $15.0\%$

**Step 1: Set up the CAPM equation**

$$24.0\% = 6.0\% + \beta_i (15.0\% - 6.0\%)$$

**Step 2: Isolate the systematic risk component**

$$24.0\% - 6.0\% = \beta_i (9.0\%)$$
$$18.0\% = \beta_i (9.0\%)$$

**Step 3: Solve for $\beta_i$**

$$\beta_i = \frac{18.0\%}{9.0\%} = 2.0$$

- **Interpretation:** The asset has a beta of $2.0$, meaning it exhibits twice the systematic sensitivity of the overall market.

### 5.6 Summary Comparison: Standard Deviation vs. Beta

|**Dimension**|**Standard Deviation (σ)**|**Beta (β)**|
|---|---|---|
|**Type of Risk Measured**|Total Risk (Systematic + Unsystematic)|Systematic Risk (Market Risk Only)|
|**Statistical Definition**|Dispersion of returns around their own mean|Covariance of returns with the market divided by market variance|
|**Eliminated by Diversification?**|Partially (unsystematic component drops to 0)|**No** (captures the irreducible market exposure)|
|**Role in Asset Pricing (CAPM)**|Does not determine asset expected return|**Direct determinant** of expected required return|
|**Best Used For**|Evaluating standalone portfolios or total risk|Evaluating individual assets added to a diversified portfolio|
