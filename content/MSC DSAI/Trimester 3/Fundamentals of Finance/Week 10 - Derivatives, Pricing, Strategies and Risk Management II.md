## 1. The Day a Barrel of Oil Was Worth Minus Forty Dollars

On **April 20, 2020**, the front-month May 2020 West Texas Intermediate (WTI) crude oil futures contract on the New York Mercantile Exchange (NYMEX) traded down to an unprecedented **-$37.63 per barrel**. Market participants were effectively paying counterparties more than $37 per barrel to take delivery of physical crude.

```
                  THE APRIL 20, 2020 WTI LIQUIDITY SPIRAL
                  
   COVID-19 Lockdowns        OPEC+ Price War          Cushing, OK Hub
(Global Demand -30%)    +   (Supply Glut)       +  (Physical Storage Full)
          │
          ▼
   WTI Contract Expiration (April 21, 2020)
   - Retail ETFs (e.g., USO) & Speculators held long contracts.
   - Physical delivery mandatory for contracts held past expiry.
   - Commercial storage unavailable to financial players.
          │
          ▼
   Forced Fire-Sale Liquidation at Any Cost
   Price plummeted from +$18/bbl -> $0 -> -$37.63/bbl (Settlement)
```

### First Principles: Physical vs. Financial Settlement

Derivative contracts settle in one of two ways at expiration:

1. **Cash Settlement:** No physical goods change hands. Counterparties exchange the net cash difference between the contract price and the final spot price (common in index futures like the S&P 500).
    
2. **Physical Delivery:** The contract holder is legally obligated to deliver or accept delivery of the actual physical commodity at a specified terminal.

WTI futures require physical delivery at **Cushing, Oklahoma**—a pipeline hub with finite tank capacity. When storage at Cushing filled to capacity, the cost of storing incremental oil effectively approached infinity.

### Why Prices Turned Negative

- **The Long Speculator's Trap:** Financial speculators and passive index funds hold futures for price exposure, not industrial consumption. They cannot take delivery of 1,000 barrels per contract.
    
- **The Obligation Constraint:** Contract rules dictate that if a long position is not closed or rolled over to the next month (June 2020) before expiration, the buyer must take delivery at Cushing.
    
- **The No-Arbitrage Breakdown:** Arbitrageurs normally step in to buy undervalued contracts and store the physical oil for future sale. Because all commercial storage was leased or operational, no arbitrageur could accept physical crude, causing the pricing floor to collapse entirely.

The price of a physically delivered commodity futures contract reflects not just intrinsic energy value, but the **cost of carry** (transportation, handling, and storage). When holding and storage costs exceed the future economic value of the asset, the market clearing price can turn negative.

---  

## 2. Structure of a Futures Contract and Futures Valuation

A **futures contract** is a standardized, legally binding agreement traded on a centralized exchange to buy or sell a specified quantity and quality of an underlying asset at a predetermined price on a specified future date.

### Anatomy of a Futures Contract

- **Underlying Asset:** Standardized grade (e.g., Light Sweet Crude Oil, 5,000 bushels of corn, 100 troy ounces of gold).
    
- **Contract Size (Notional Multiplier):** The unit volume per contract.
    
- **Settlement Mechanism:** Physical delivery vs. Cash-settled.
    
- **Clearinghouse Intermediation:** The clearinghouse acts as the central counterparty (buyer to every seller, seller to every buyer), eliminating bilateral counterparty default risk.

```
Bilateral Forward:       [ Buyer ] <------------------------> [ Seller ]
                                    (Direct Credit Risk)

Exchange-Traded Futures: [ Buyer ] <---> [ Clearinghouse ] <---> [ Seller ]
                                       (Zero Counterparty Risk)
```

### Futures Valuation: The Cost of Carry Model

Under the **No-Arbitrage Principle**, the price of a futures contract ($F_0$) must equal the compounded spot price ($S_0$) plus all net costs incurred to hold the physical asset until maturity ($T$).

#### 1. Investment Assets Without Income (e.g., Non-dividend stocks, Gold)

Using continuous compounding:

$$F_0 = S_0 e^{rT}$$

Where $r$ is the continuously compounded annualized risk-free rate.

#### 2. Investment Assets With Known Dividend/Yield ($q$)

For equity indices or foreign currencies providing an income yield $q$:

$$F_0 = S_0 e^{(r - q)T}$$

#### 3. Consumption Commodities (Storage Costs and Convenience Yield)

Physical commodities incur storage costs ($u$) and provide a non-monetary **convenience yield** ($y$)—the embedded operational advantage of having physical inventory on hand during shortages:

$$F_0 = S_0 e^{(r + u - y)T}$$

### Term Structure: Contango vs. Backwardation

```
Price ($)                                   Price ($)
  ^                                           ^
  |          / Futures Curve (F > S)          |   S_0 +--\
  |         /                                 |           \  Futures Curve (F < S)
  |        /                                  |            \
S_0 +-----/                                   |             \
  +------------------> Time to Expiry (T)     +------------------> Time to Expiry (T)
           CONTANGO                                   BACKWARDATION
   Cost of Carry > Convenience Yield          Convenience Yield > Cost of Carry
```

- **Contango ($F_0 > S_0$):** Normal market condition for storable assets where financing and storage costs dominate ($r + u > y$).
     
- **Backwardation ($F_0 < S_0$):** Occurs when near-term physical shortages drive the convenience yield higher than carrying costs ($y > r + u$).
 
### Proof via Cash-and-Carry Arbitrage

If $F_0 > S_0 (1 + r)^T$, a trader executes an arbitrage trade at $t = 0$:

1. Borrow cash $S_0$ at rate $r$.
    
2. Buy the underlying physical asset at spot price $S_0$.
    
3. Sell (short) the futures contract at $F_0$.

At maturity $T$:

- Deliver the physical asset to settle the futures contract, receiving $F_0$.
    
- Repay the loan balance: $S_0 (1 + r)^T$.
    
- **Risk-Free Arbitrage Profit:** $\Pi = F_0 - S_0 (1 + r)^T > 0$.

Selling pressure on $F_0$ and buying pressure on $S_0$ instantly restore parity.

---

## 3. The Futures Payoff Diagram

Futures contracts exhibit a **linear (symmetric)** payoff. Both the buyer and seller face unbounded gains or losses proportional to the difference between the spot price at expiration ($S_T$) and the locked-in futures delivery price ($F_0$).

$$\text{Long Futures Payoff per unit} = S_T - F_0$$
$$\text{Short Futures Payoff per unit} = F_0 - S_T$$

```
   Payoff ($)
       ^
       |                               / Long Futures (Slope = +1)
       |                              /
       |                             /
   0 --+----------------------------/-------------> Spot Price at Maturity (S_T)
       |                           / 
       |                          / Strike / Futures Price (F_0)
       |       Short Futures     /
       |      (Slope = -1) \    /
       |                    \  /
       v                     \/
```

### Linear vs. Non-Linear Payoffs

```
Futures (Symmetric / Obligation)            Options (Asymmetric / Right)
        Payoff                                      Payoff
          ^      /                                    ^          /
          |     /                                     |         /
          |    /                                      |        /
    0 ----+---/-----> Spot                      0 ----+-------/-----> Spot
         /|  /                                     -P |______/ (Limited Loss)
        / | /                                         |
```

- **Futures (Linear):** Entering a contract costs $\$0$ upfront. Every $\$1$ change in spot price creates a corresponding $\$1$ gain for one party and a $\$1$ loss for the other (a strict zero-sum game).
    
- **Options (Non-linear):** The buyer pays an upfront, non-refundable premium to cap downside risk while preserving upside.

---

## 4. Futures vs. Options: Comprehensive Comparison

|**Dimension**|**Futures Contract**|**Options Contract**|
|---|---|---|
|**Nature of Obligation**|**Bilateral:** Both parties are legally bound to execute the trade.|**Unilateral:** Buyer has the right; seller has the binding obligation.|
|**Initial Capital Outlay**|**$0 initial cost** (only a refundable performance margin is deposited).|**Option Premium** paid upfront by the buyer to the seller (sunk cost).|
|**Payoff Profile**|**Linear / Symmetric:** Gains and losses move 1:1 with the asset.|**Non-Linear / Kinked:** Asymmetric risk-reward distribution.|
|**Downside Risk for Buyer**|**Substantial/Unlimited:** Long can lose far more than initial margin.|**Strictly Limited:** Cannot lose more than the initial premium paid.|
|**Upside for Seller**|**Unlimited:** Profit increases linearly if price moves in favor.|**Capped:** Maximum return is the initial premium collected.|
|**Pricing Variables**|Spot price ($S$), interest rate ($r$), carry costs ($u$), yield ($y$).|Spot ($S$), Strike ($K$), Expiry ($T$), Volatility ($\sigma$), Rate ($r$).|

---

## 5. Futures Margins & Daily Settlement (Mark-to-Market)

Because futures involve symmetrical forward commitments without upfront cost, counterparty default risk is managed through **daily mark-to-market margins**.

```
+-------------------------------------------------------------------------+
|                  FUTURES MARGIN WATERFALL STRUCTURE                     |
+-------------------------------------------------------------------------+
| Initial Margin Deposit (e.g., $6,000)                                   |
|   ▲                                                                     |
|   │ Daily Mark-to-Market (Profits added / Losses deducted daily)        |
|   ▼                                                                     |
| Maintenance Margin Threshold (e.g., $4,500)                            |
| ─────────────────────────────────────────────────────────────────────── |
|   ▼ (If Account Balance drops BELOW Maintenance Margin)                 |
| MARGIN CALL TRIGGERED:                                                  |
| Trader MUST deposit variation margin to restore account back to the     |
| INITIAL MARGIN level ($6,000), not just the maintenance level.          |
+-------------------------------------------------------------------------+
```

### Margin Definitions

- **Initial Margin:** The minimum cash balance required to open a futures position (typically 3% to 12% of the contract's total notional value).
     
- **Maintenance Margin:** The critical equity floor (usually 70% to 80% of the initial margin).
     
- **Variation Margin:** The cash required to bring the margin account back up to the **Initial Margin** level following a loss.
 
### Step-by-Step Numerical Walkthrough

- **Contract:** 1 Gold Futures Contract = 100 troy ounces
     
- **Purchase Price ($F_0$):** $2,000/oz (Notional Value = $200,000)
     
- **Initial Margin Requirement:** $10,000
     
- **Maintenance Margin Requirement:** $7,500
 
|**Day**|**Settlement Price**|**Daily Price Change**|**Daily Gain / Loss (Δ×100)**|**Account Balance Before Action**|**Margin Call?**|**Cash Required (Variation Margin)**|**Ending Balance**|
|---|---|---|---|---|---|---|---|
|**0**|$2,000|—|—|$10,000|No|$0|$10,000|
|**1**|$1,980|-$20|-$2,000|$8,000|No ($8,000 > $7,500)|$0|$8,000|
|**2**|$1,960|-$20|-$2,000|$6,000|**YES** ($6,000 < $7,500)|**+$4,000**|$10,000|
|**3**|$1,990|+$30|+$3,000|$13,000|No ($13,000 > $7,500)|$0|$13,000|

_On Day 2, the balance dropped to $6,000 (below the $7,500 maintenance threshold). The margin call demanded **$4,000** to reset the balance to the initial margin of $10,000._

---

## 6. Hedging Using Futures

Hedging locks in cash flows and neutralizes price risk in an underlying physical asset.

### Short Hedge vs. Long Hedge

- **Short Hedge (Producer/Owner):** An entity owns or produces an asset and fears a price drop.
      
    - _Action:_ **Sell (Short) Futures today.**
        
    - _Example:_ A wheat farmer shorts wheat futures at harvest planting. If wheat prices collapse, losses in the physical crop are offset by gains in the short futures position.
        
- **Long Hedge (Consumer/Processor):** An entity must purchase an asset in the future and fears a price increase.
      
    - _Action:_ **Buy (Long) Futures today.**
        
    - _Example:_ An airline buys jet fuel / crude oil futures. If oil spikes, higher fuel operating costs are offset by gains on the long futures position.

### Basis and Basis Risk

The **basis** is the difference between the local physical spot price ($S_t$) and the futures price ($F_t$):

$$\text{Basis}_t = S_t - F_t$$

- **Convergence Property:** At delivery ($t = T$), arbitrage forces the basis to zero: $\text{Basis}_T = S_T - F_T = 0$.
    
- **Basis Risk:** The risk that the basis will fluctuate unexpectedly between hedge initiation and liquidation. This occurs when:
      
    1. The asset being hedged is not identical to the futures contract grade (**cross-hedging**, e.g., jet fuel hedged with crude oil).
        
    2. The maturity of the futures contract does not match the date of the physical transaction.

```
Effective Price Received (Short Hedge) = S_2 + (F_1 - F_2) = F_1 + Basis_2
```

### The Minimum-Variance Hedge Ratio ($h^*$)

When cross-hedging, price movements between the physical asset ($\Delta S$) and the futures contract ($\Delta F$) are not perfectly correlated. The optimal proportion of the asset position to hedge is calculated via linear regression:

$$h^* = \rho \frac{\sigma_S}{\sigma_F} = \frac{\text{Cov}(\Delta S, \Delta F)}{\sigma_F^2}$$

Where:

- $\rho$: Correlation coefficient between $\Delta S$ and $\Delta F$
    
- $\sigma_S$: Standard deviation of $\Delta S$
    
- $\sigma_F$: Standard deviation of $\Delta F$

#### Calculating the Number of Contracts ($N^*$)

$$N^* = h^* \times \frac{Q_A}{Q_F}$$

- $Q_A$: Total quantity of the physical asset being hedged.
    
- $Q_F$: Standardized quantity size of one futures contract.

---

## 7. Options Moneyness: Mechanics and Greeks

**Moneyness** describes the intrinsic payoff available if an option were exercised immediately at the prevailing spot price ($S$) relative to the strike price ($K$).

```
                      CALL OPTION                      PUT OPTION
             +---------------------------+    +---------------------------+
  ITM        |   Spot > Strike (S > K)   |    |   Spot < Strike (S < K)   |
             +---------------------------+    +---------------------------+
  ATM        |   Spot = Strike (S = K)   |    |   Spot = Strike (S = K)   |
             +---------------------------+    +---------------------------+
  OTM        |   Spot < Strike (S < K)   |    |   Spot > Strike (S > K)   |
             +---------------------------+    +---------------------------+
```

### Moneyness, Delta ($\Delta$), and Extrinsic Value

$$\text{Delta } (\Delta) = \frac{\partial \text{Option Price}}{\partial S}$$

Delta measures the sensitivity of the option price to changes in the underlying stock price. Under risk-neutral pricing, $\vert{}\Delta\vert{}$ approximates the probability of the option expiring In-The-Money (ITM).

```
Delta Profile:
  Deep OTM Call       ATM Call       Deep ITM Call
  Delta ~ 0.05       Delta ~ 0.50     Delta ~ 0.95
       |------------------|----------------|
     S << K             S = K            S >> K
```

|**Moneyness Classification**|**Intrinsic Value**|**Extrinsic (Time) Value**|**Delta Range (ΔCall​)**|**Delta Range (ΔPut​)**|
|---|---|---|---|---|
|**Deep Out-of-the-Money (OTM)**|$\$0$|Low|$0.00 \le \Delta < 0.20$|$-0.20 < \Delta \le 0.00$|
|**At-the-Money (ATM)**|$\$0$|**Maximum**|$\Delta \approx +0.50$|$\Delta \approx -0.50$|
|**Deep In-the-Money (ITM)**|High ($\vert{}S - K\vert{}$)|Low|$0.80 < \Delta \le 1.00$|$-1.00 \le \Delta < -0.80$|

_Extrinsic (time) value peaks when an option is At-the-Money (ATM) because the uncertainty regarding whether it will expire ITM or OTM is highest at that price point._

## 8. Options as Insurance: Financial Engineering in Action

Option contracts are the analytical equivalents of commercial insurance policies.

```
       INSURANCE POLICY                          PUT OPTION CONTRACT
+-----------------------------+             +-----------------------------+
| Homeowner pays a Premium    | <=========> | Investor pays Put Premium P |
+-----------------------------+             +-----------------------------+
| Deductible (Floor on Value) | <=========> | Strike Price K              |
+-----------------------------+             +-----------------------------+
| Property Damages Covered    | <=========> | Payoff: max(0, K - S_T)     |
+-----------------------------+             +-----------------------------+
```

### Protective Put vs. Stop-Loss Order

A **Stop-Loss Order** instructs a broker to sell an asset if the price hits a threshold. However, stop orders do not guarantee execution price in discontinuous markets:

- **Gap-Down Risk:** If a stock closes at $\$100$ and opens at $\$70$ after catastrophic overnight news, a $\$90$ stop-loss executes at the prevailing market price of $\$70$.
    
- **The Put Option Advantage:** A $\$90$ Strike Put option legally guarantees execution at $\$90$, regardless of market liquidity or price gaps.

```
Payoff ($)
    ^
    |                                   / Protective Put Portfolio Payoff
    |                                  /  (Floor at K, Unlimited Upside)
  K + - - - - - - - - - - - - - - - - /
    |                                /
    |                               /  Slope = +1
    |                              /
    0-----------------------------+------------------> Stock Price (S_T)
                                  K
```

### Synthetic Positions via Put-Call Parity

Using the foundational Put-Call Parity relationship:

$$C + K e^{-rT} = P + S$$

We can isolate individual legs to engineer **synthetic assets**:

- **Synthetic Long Stock ($S$):** Buy a Call, Sell a Put at the same strike, invest the present value of the strike:
    $$S = C - P + K e^{-rT}$$
    
- **Synthetic Long Call ($C$):** Buy the Stock, Buy a Protective Put, borrow the present value of the strike:
    $$C = S + P - K e^{-rT}$$
    
- **Synthetic Protective Put ($P + S$):** Equal to a **Fiduciary Call** ($C + K e^{-rT}$).

---

## 9. Betting on Movement Itself: Straddle and Strangle

Standard stock positions bet on **direction**. Volatility strategies bet on the **magnitude** of price movement, regardless of whether the price rises or falls.

  

```
      LONG STRADDLE PAYOFF                       LONG STRANGLE PAYOFF
         (Strike = K)                           (Strikes: K_1 < K_2)
       Profit                                     Profit
         ^    \       /                             ^   \             /
         |     \     /                              |    \           /
         |      \   /                               |     \         /
       0 +-------\-/-------> S_T                  0 +------\_______/-------> S_T
         |        V                                 |       |     |
      -(C+P)     S=K                             -(C+P)    K_1   K_2
```

### Strategy 1: The Long Straddle

- **Construction:** Buy 1 ATM Call ($K$) $+$ Buy 1 ATM Put ($K$) with identical expiration dates ($T$).
    
- **Market Outlook:** Expects high volatility or a major price catalyst (e.g., earnings report, FDA drug trial verdict, Supreme Court ruling), but direction is unknown.
    
- **Cost (Max Loss):** Total premiums paid: $C + P$ (incurred if the stock settles exactly at strike $K$).
    
- **Breakeven Points:**
    $$\text{Upper Breakeven} = K + (C + P)$$
    $$\text{Lower Breakeven} = K - (C + P)$$
    
- **Payoff Formula:**
    $$\Pi_{\text{Straddle}} = \max(S_T - K, 0) + \max(K - S_T, 0) - (C + P) = \vert{}S_T - K\vert{} - (C + P)$$
    

### Strategy 2: The Long Strangle

- **Construction:** Buy 1 Out-of-the-Money Put ($K_1$) $+$ Buy 1 Out-of-the-Money Call ($K_2$), where $K_1 < K_2$.
    
- **Market Outlook:** Expects extreme price movement; cheaper alternative to a straddle.
    
- **Cost (Max Loss):** Total premiums paid: $C + P$ (incurred if the stock finishes anywhere between $K_1$ and $K_2$).
    
- **Breakeven Points:**
    $$\text{Upper Breakeven} = K_2 + (C + P)$$
    $$\text{Lower Breakeven} = K_1 - (C + P)$$
    
- **Payoff Formula:**
     $$\Pi_{\text{Strangle}} = \max(K_1 - S_T, 0) + \max(S_T - K_2, 0) - (C + P)$$
    

### Comparative Analysis: Straddle vs. Strangle

|**Feature**|**Long Straddle**|**Long Strangle**|
|---|---|---|
|**Strikes Used**|1 Strike ($K_{\text{Call}} = K_{\text{Put}} = \text{ATM}$)|2 Distinct Strikes ($K_{\text{Put}} < S_0 < K_{\text{Call}}$)|
|**Initial Upfront Cost**|**Higher** (buying ATM options with maximum time value).|**Lower** (buying OTM options with cheaper premiums).|
|**Required Price Move to Profit**|**Moderate:** Stock must move more than $(C + P)$.|**Substantial:** Stock must move past $K_1$ or $K_2$ by $(C + P)$.|
|**Maximum Loss Zone**|Occurs at a single point ($S_T = K$).|Occurs across a wide interval ($K_1 \le S_T \le K_2$).|
|**Ideal Market Environment**|High volatility expected, narrower expected range.|Explosive volatility expected at minimal capital commitment.|

### Strategy 3: The Short (Written) Straddle and Strangle

Traders take the opposite side by **selling both options** when they expect range-bound markets or implied volatility contraction:

- **Outlook:** Neutral, low volatility (e.g., quiet holiday trading periods).
    
- **Maximum Gain:** Total upfront premiums collected ($C + P$).
    
- **Risk Profile:** **Unlimited** losses if the stock experiences an unexpected breakout in either direction.