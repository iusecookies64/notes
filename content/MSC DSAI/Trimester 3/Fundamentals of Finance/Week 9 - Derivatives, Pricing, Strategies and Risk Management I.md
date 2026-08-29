## 1. Introduction to Derivatives and Options

A **derivative** is a financial contract whose value is derived from the performance of an underlying entity, such as an asset (stocks, bonds, commodities, currencies), an interest rate, or an index. Derivatives are fundamentally tools for **risk transfer**, enabling market participants to either hedge existing risks or speculate on future price movements.

```
+-------------------------------------------------------------+
|                      Underlying Asset                       |
|           (e.g., Apple Stock, Crude Oil, S&P 500)           |
+-------------------------------------------------------------+
                               |
                               v (determines value of)
+-------------------------------------------------------------+
|                     Derivative Contract                     |
|           (Forwards, Futures, Swaps, and Options)           |
+-------------------------------------------------------------+
```

### Forwards/Futures vs. Options

|**Feature**|**Forwards & Futures**|**Options Contracts**|
|---|---|---|
|**Obligation**|**Mutual Obligation:** Both parties _must_ execute the transaction at expiration.|**Asymmetric Obligation:** The buyer has the _right_, the seller has the _obligation_.|
|**Upfront Cost**|Usually zero initial exchange of capital (margin deposits only).|The buyer pays a non-refundable **premium** to the seller upfront.|
|**Payoff Profile**|Symmetrical (linear profit and loss).|Asymmetrical (non-linear: limited risk for buyer, unlimited/capped risk for seller).|

### Core Concept of an Option

An **option** is a binding contract that grants the **holder (buyer)** the right, but not the obligation, to buy or sell a specific quantity of an underlying asset at a predetermined price on or before a specified date. The **writer (seller)** receives an upfront fee (the **premium**) and takes on the legal obligation to fulfill the contract if the buyer chooses to exercise it.

---  

## 2. Introduction to Stock Options & Contract Mechanics

In equity markets, standardized exchange-traded options share uniform structural parameters.

### Core Parameters

- **Underlying Asset ($S$):** The specific stock (e.g., Microsoft, Tesla). Standard equity contracts represent **100 shares** of the underlying stock.
    
- **Strike Price ($K$ or $X$):** The fixed price at which the contract holder can buy or sell the underlying shares.
    
- **Expiration Date ($T$):** The exact date and time when the contract expires and becomes void.
    
- **Option Premium ($C$ for Call, $P$ for Put):** The market price paid per share by the buyer to the seller. For a standard 100-share contract, the total cash outlay is $\text{Premium} \times 100$.

### Exercise Styles

- **American Style:** Can be exercised at **any time** up to and including the expiration date. Most single-stock options trade as American style.
    
- **European Style:** Can be exercised **only on the expiration date**. Most index options trade as European style.

### Moneyness

Moneyness describes the intrinsic relationship between the current stock price ($S_t$) and the strike price ($K$).

```
        Current Stock Price (S) vs. Strike Price (K)
                     
      CALL OPTION:                   PUT OPTION:
  +------------------+           +------------------+
  |  S > K  --> ITM  |           |  S < K  --> ITM  |
  |  S = K  --> ATM  |           |  S = K  --> ATM  |
  |  S < K  --> OTM  |           |  S > K  --> OTM  |
  +------------------+           +------------------+
```

- **In-the-Money (ITM):** Exercising the option yields an immediate positive cash value.
       
    - Call: $S_t > K$ (Buy below current market price).
         
    - Put: $S_t < K$ (Sell above current market price).
         
- **At-the-Money (ATM):** The stock price equals the strike price ($S_t = K$).
     
- **Out-of-the-Money (OTM):** Exercising the option yields no financial benefit.
       
    - Call: $S_t < K$ (Market price is cheaper than strike).
        
     - Put: $S_t > K$ (Market price is higher than strike).

---

## 3. Trading a Call Option: The Long Call

A **Call Option** grants the holder the right to **buy** the underlying asset at the strike price $K$.

A **Long Call** is an explicitly **bullish strategy** used when an investor expects the stock price to rise significantly before expiration.

### Financial Characteristics of a Long Call

- **Maximum Loss:** Capped at the total premium paid ($C$). This occurs when the stock finishes OTM ($S_T \le K$).
    
- **Maximum Profit:** Theoretically **unlimited**, as the stock price can rise indefinitely.
    
- **Breakeven Point at Expiration ($S_T^*$):**
    $$S_T^* = K + C$$

### Numerical Walkthrough

- **Current Stock Price ($S_0$):** $100
    
- **Call Strike Price ($K$):** $100 (ATM)
    
- **Call Premium ($C$):** $5 per share ($500 total for 1 contract)
    
- **Breakeven Price:** $\$100 + \$5 = \$105$

|**Stock Price at Expiration (ST​)**|**Decision**|**Gross Payoff per share max(0,ST​−K)**|**Net Profit/Loss per share (Payoff−C)**|**Total Profit/Loss (100 shares)**|
|---|---|---|---|---|
|**$80**|Let Expire|$0|-$5|-$500 (Max Loss)|
|**$100**|Let Expire|$0|-$5|-$500 (Max Loss)|
|**$105**|Exercise|$5|$0|$0 (Breakeven)|
|**$120**|Exercise|$20|+$15|+$1,500|
|**$150**|Exercise|$50|+$45|+$4,500|

---

## 4. Calculating Option Premium & Price Drivers

The total market price of an option is partitioned into two distinct components:

$$\text{Option Premium} = \text{Intrinsic Value} + \text{Time Value (Extrinsic Value)}$$

```
+-----------------------------------------------------------------------+
|                             Option Premium                            |
+-----------------------------------+-----------------------------------+
|          Intrinsic Value          |             Time Value            |
|  (Immediate economic value if     |  (Premium for uncertainty, time   |
|      exercised right now)         |     remaining, and volatility)    |
+-----------------------------------+-----------------------------------+
```

### 1. Intrinsic Value

The payoff realized if the option were exercised immediately:

- **Call Intrinsic Value:** $\max(0, S_t - K)$
    
- **Put Intrinsic Value:** $\max(0, K - S_t)$

_Intrinsic value can never be negative; if an option is OTM, its intrinsic value is exactly zero._

### 2. Time Value (Extrinsic Value)

The excess value of the option over its intrinsic value:

$$\text{Time Value} = \text{Option Premium} - \text{Intrinsic Value}$$

Time value reflects the probability that the option will move further into the money prior to expiration. It undergoes **time decay ($\Theta$, Theta)**, eroding at an accelerating rate as expiration approaches ($T \to 0$).

### Key Determinants of Option Premiums

|**Variable**|**Symbol**|**Impact on Call Price**|**Impact on Put Price**|**Economic Intuition**|
|---|---|---|---|---|
|**Stock Price**|$S_0$|**$\uparrow$ Increases**|**$\downarrow$ Decreases**|Higher stock price raises Call payoff ($S-K$) and lowers Put payoff ($K-S$).|
|**Strike Price**|$K$|**$\downarrow$ Decreases**|**$\uparrow$ Increases**|Lower strike makes Calls cheaper to buy through; higher strike makes Puts more lucrative to sell into.|
|**Time to Expiry**|$T$|**$\uparrow$ Increases**|**$\uparrow$ Increases**|More time allows greater opportunity for favorable price swings.|
|**Volatility**|$\sigma$|**$\uparrow$ Increases**|**$\uparrow$ Increases**|Higher dispersion expands the probability of extreme positive payoffs while downside is protected by limited loss.|
|**Risk-Free Rate**|$r$|**$\uparrow$ Increases**|**$\downarrow$ Decreases**|Buying a call delays cash outlay for stock purchases (saving interest); buying a put delays receiving stock proceeds.|
|**Dividends**|$q$|**$\downarrow$ Decreases**|**$\uparrow$ Increases**|The stock price drops on the ex-dividend date, harming Call holders and helping Put holders.|

---

## 5. Call Option Payoff and Profit/Loss Diagrams

An option trade has two complementary counterparties: the **Long Position (Buyer)** and the **Short Position (Seller/Writer)**.

### Mathematical Definitions at Expiration ($T$)

- **Long Call Payoff (Gross):**
    $$\text{Payoff}_{\text{Long Call}} = \max(0, S_T - K)$$
    
- **Long Call Profit (Net):**
    $$\Pi_{\text{Long Call}} = \max(0, S_T - K) - C$$
    
- **Short Call Payoff (Gross):**
    $$\text{Payoff}_{\text{Short Call}} = -\max(0, S_T - K)$$
    
- **Short Call Profit (Net):**
    $$\Pi_{\text{Short Call}} = C - \max(0, S_T - K)$$

### Payoff and Profit Comparison

```
   Profit ($)
       ^
       |                                   /  Long Call Profit: Slope = +1
  +40  |                                  /
  +20  |                                 /
    0 -+-------------------------+------/------------> Stock Price (S_T)
       |                        K|     / Breakeven (K + C)
   -C -+-------------------------+----/
       |  \
       |   \
   +C -+----\--------------------+-------------------  Short Call Profit
    0 -+-----\-------------------+------------------->
             Breakeven (K + C)   K\
                                   \
                                    \ Slope = -1 (Unlimited Downside Risk)
```

### Key Differences Between Buyer and Seller

- **Long Call (Buyer):** Limited risk ($-C$), unlimited upside potential.
     
- **Short Call (Seller):** Limited gain ($+C$), unlimited downside risk. The seller earns income by taking on the obligation to sell shares at $K$ even if the market price surges to extreme levels.

---

## 6. Introduction to Put Options

A **Put Option** grants the holder the right to **sell** the underlying stock at the strike price $K$.

A **Long Put** is a **bearish strategy** used to profit from falling prices or to protect existing share holdings.

```
+--------------------------------------------------------------------------+
|                             LONG PUT POSITION                            |
+------------------------------------+-------------------------------------+
| Goal                               | Profit from a decline in stock price|
| Maximum Profit                     | Strike Price - Premium ($K - P$)    |
|                                    | (Achieved if stock drops to $0)     |
| Maximum Loss                       | Premium Paid ($P$)                  |
| Breakeven Point ($S_T^*$)          | Strike Price - Premium ($K - P$)    |
+------------------------------------+-------------------------------------+
```

### Mathematical Definitions

- **Gross Payoff:** $\text{Payoff} = \max(0, K - S_T)$
    
- **Net Profit:** $\Pi = \max(0, K - S_T) - P$

### Numerical Example

- **Strike Price ($K$):** $50
    
- **Put Premium ($P$):** $4
    
- **Breakeven Point:** $\$50 - \$4 = \$46$
    
- If $S_T = \$30$: Exercise at $\$50$. Buy at market for $\$30$. Gross payoff = $\$20$. Net profit = $\$20 - \$4 = +\$16$ per share ($+\$1,600$ total).
    
- If $S_T = \$46$: Exercise at $\$50$. Gross payoff = $\$4$. Net profit = $\$4 - \$4 = \$0$ (Breakeven).
    
- If $S_T \ge \$50$: Do not exercise. Gross payoff = $\$0$. Net loss = $-\$4$ per share ($-\$400$ total).

---

## 7. Protective Put and Short Put

### Strategy A: The Protective Put

A **Protective Put** combines owning shares of stock with a Long Put on the same shares:

$$\text{Portfolio Value} = \text{Long 100 Shares of Stock} + \text{Long 1 Put Option Contract}$$

```
Stock Position           Long Put Position          Protective Put
 (Linear Risk)             (Downside Hedge)       (Synthetic Long Call)

     /                          \                        /
    /                            \                      /
   /                              \____             ___/ (Floor on losses)
```

#### Strategic Objective

Acts as an insurance policy. It guarantees that the investor can sell the stock for at least $K$, establishing a **maximum loss floor** while preserving **unlimited upside** if the stock rallies.

- **Gross Payoff at Expiration:**
    $$\text{Payoff} = S_T + \max(0, K - S_T) = \max(S_T, K)$$
    
- **Floor Value:** The combined position will never be worth less than $K$.
    
- **Net Cost:** The investor pays the put premium $P$, which reduces the net return across all outcomes.

### Strategy B: The Short Put (Selling/Writing a Put)

A **Short Put** involves selling a put option to another party without holding an offsetting short stock position.

- **Outlook:** Neutral to mildly bullish.
    
- **Maximum Profit:** The initial premium collected ($+P$), achieved when $S_T \ge K$.
    
- **Maximum Loss:** Substantial: $K - P$ per share (occurs if the stock falls to $0$).
    
- **Breakeven Point:** $K - P$.

```
   Profit ($)
       ^
   +P -+-------------------+
       |                    \
    0 -+---------------------\----+-------------> Stock Price (S_T)
       |                      \   |
       |          Breakeven (K-P) K
       |                        \
       |                         \  Slope = +1 (Substantial downside risk)
```

---

## 8. Calculating Put Options & Put-Call Parity

### Step-by-Step Put Pricing Breakdown

Consider a stock trading at $S_0 = \$42$, with a 6-month European Put option ($K = \$45$) trading for $P = \$5.50$.

1. **Calculate Intrinsic Value:**
    $$\text{Intrinsic Value} = \max(0, K - S_0) = \max(0, 45 - 42) = \$3.00$$
    
2. **Calculate Time Value:**
    $$\text{Time Value} = \text{Premium} - \text{Intrinsic Value} = \$5.50 - \$3.00 = \$2.50$$

### Put-Call Parity

**Put-Call Parity** is one of the most fundamental structural relationships in derivatives finance. It defines a no-arbitrage equilibrium between European call and put options with identical strikes ($K$) and expiration dates ($T$).

#### The Parity Equation

$$C_t + \frac{K}{(1 + r)^T} = P_t + S_t$$

Using continuous compounding:

$$C_t + K e^{-rT} = P_t + S_t$$

Where:

- $C_t$: Price of the European Call
     
- $P_t$: Price of the European Put
     
- $S_t$: Current price of the underlying stock
     
- $K e^{-rT}$: Present value of the strike price discounted at risk-free rate $r$ over time $T$

#### The Underlying Logic: Synthetic Replicating Portfolios

Consider two distinct investment portfolios constructed today:

- **Portfolio A:** 1 Long Call ($C$) $+$ Cash equal to the present value of the strike price ($K e^{-rT}$).
     
- **Portfolio B:** 1 Long Put ($P$) $+$ 1 Share of Stock ($S$).
 
At expiration date $T$, consider both market conditions:

| **Market Scenario**              | **Value of Portfolio A (C+K)** | **Value of Portfolio B (P+S)** |
| -------------------------------- | ------------------------------ | ------------------------------ |
| **If $S_T > K$ (Stock rises)**   | $(S_T - K) + K = \mathbf{S_T}$ | $0 + S_T = \mathbf{S_T}$       |
| **If $S_T \le K$ (Stock falls)** | $0 + K = \mathbf{K}$           | $(K - S_T) + S_T = \mathbf{K}$ |

Because Portfolio A and Portfolio B produce **identical payoffs in all future states of the world**, the **Law of One Price** dictates that their initial purchase prices today must be equal:

$$C_0 + K e^{-rT} = P_0 + S_0$$

If this equality does not hold, a riskless **arbitrage opportunity** emerges: traders will buy the undervalued portfolio and short-sell the overvalued portfolio, locking in risk-free profit until prices return to parity.

### Summary Reference Table for Option Positions

|**Position**|**Market View**|**Max Profit**|**Max Loss**|**Breakeven (ST∗​)**|**Payoff Formula Payoff(ST​)**|
|---|---|---|---|---|---|
|**Long Call**|Bullish|Unlimited|Premium ($C$)|$K + C$|$\max(0, S_T - K)$|
|**Short Call**|Bearish/Neutral|Premium ($C$)|Unlimited|$K + C$|$-\max(0, S_T - K)$|
|**Long Put**|Bearish|$K - P$|Premium ($P$)|$K - P$|$\max(0, K - S_T)$|
|**Short Put**|Bullish/Neutral|Premium ($P$)|$K - P$|$K - P$|$-\max(0, K - S_T)$|