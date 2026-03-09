# DeFi Attack Taxonomy

## Classification Framework

This taxonomy classifies DeFi attacks across multiple dimensions to enable systematic analysis and defense development.

## Attack Categories

### 1. Flash Loan Attacks

**Description:** Attacks leveraging uncollateralized loans that must be repaid within a single transaction.

**Capital Requirement:** Minimal (gas costs only)  
**Atomicity:** High (single transaction)  
**Protocol Dependency:** Medium (requires flash loan provider)  
**Economic Impact:** High ($3M+ average)

**Characteristics:**
- Zero capital requirement (excluding gas)
- Executed within single block
- Repayment guaranteed by transaction revert
- Often combined with other attack vectors

**Known Incidents:**
- bZx Protocol (Feb 2020): $1.1M
- Harvest Finance (Oct 2020): $24M
- Cream Finance (Aug 2021): $18.8M

**Attack Flow:**
```
1. Borrow large amount via flash loan
2. Manipulate protocol state (price, reserves, etc.)
3. Exploit manipulated state for profit
4. Restore state (partially)
5. Repay flash loan + fee
6. Keep profit
```

---

### 2. Price Oracle Manipulation

**Description:** Attacks exploiting vulnerable price feeds to manipulate asset valuations.

**Capital Requirement:** Medium to High  
**Atomicity:** Variable  
**Protocol Dependency:** High (oracle-dependent protocols)  
**Economic Impact:** Very High ($500K+ average)

**Vulnerability Types:**
- Single DEX source oracles
- Non-TWAP implementations
- Low liquidity price sources
- Composable oracle vulnerabilities

**Attack Vectors:**
- Large DEX swaps to manipulate reserves
- Flash loans to amplify capital
- Arbitrage between manipulated and true price
- Liquidation of healthy positions

**Mitigation:**
- Time-Weighted Average Price (TWAP)
- Multiple oracle sources
- Chainlink / Band Protocol integration
- Circuit breakers on price deviation

---

### 3. Governance Attacks

**Description:** Manipulation of protocol governance mechanisms for malicious purposes.

**Capital Requirement:** Very High (requires governance tokens)  
**Atomicity:** Low (multi-block)  
**Protocol Dependency:** High (governance-enabled protocols)  
**Economic Impact:** Catastrophic (protocol control)

**Types:**
- Flash loan governance attacks
- Proposal spam attacks
- Vote buying
- Sybil attacks

**Notable Cases:**
- Beanstalk Farms (Apr 2022): $182M
- Tornado Cash governance manipulation

**Defense Mechanisms:**
- Timelock on governance changes
- Vote delegation restrictions
- Minimum proposal threshold
- Quadratic voting

---

### 4. Liquidation Exploits

**Description:** Attacks exploiting liquidation mechanisms in lending protocols.

**Capital Requirement:** Medium  
**Atomicity:** Variable  
**Protocol Dependency:** High (lending protocols)  
**Economic Impact:** Medium to High

**Exploit Scenarios:**
- Cascading liquidations
- False liquidations via oracle manipulation
- MEV extraction from liquidations
- Liquidation penalty arbitrage

**Risk Factors:**
- Low collateral ratios
- High market volatility
- Concentrated positions
- Oracle vulnerabilities

---

### 5. Re-entrancy Attacks

**Description:** Exploiting external calls to re-enter contract before state updates.

**Capital Requirement:** Low to Medium  
**Atomicity:** High  
**Protocol Dependency:** Low  
**Economic Impact:** Medium

**Famous Incidents:**
- The DAO (2016): $60M
- Various DeFi protocols (2018-2022)

**Prevention:**
- Checks-Effects-Interactions pattern
- Re-entrancy guards
- Pull over push payments

---

### 6. MEV (Maximal Extractable Value) Attacks

**Description:** Profit extraction through transaction ordering manipulation.

**Capital Requirement:** Low to High  
**Atomicity:** High  
**Protocol Dependency:** Low  
**Economic Impact:** Variable

**Types:**
- Front-running
- Back-running
- Sandwich attacks
- Time-bandit attacks

**Characteristics:**
- Requires mempool access
- Bot/searcher infrastructure
- Block space competition
- Gas price wars

---

### 7. Smart Contract Logic Errors

**Description:** Exploitation of bugs in smart contract code.

**Capital Requirement:** Variable  
**Atomicity:** Variable  
**Protocol Dependency:** High  
**Economic Impact:** Variable

**Common Errors:**
- Integer overflow/underflow
- Access control failures
- Unhandled edge cases
- Incorrect assumptions

---

### 8. Access Control Violations

**Description:** Unauthorized access to privileged functions.

**Capital Requirement:** Minimal  
**Atomicity:** High  
**Protocol Dependency:** High  
**Economic Impact:** Catastrophic

**Vulnerabilities:**
- Missing function modifiers
- Incorrect permission checks
- Default visibility issues
- Proxy pattern vulnerabilities

---

## Attack Complexity Matrix

| Attack Type | Technical Complexity | Capital Required | Detection Difficulty | Mitigation Complexity |
|-------------|---------------------|------------------|---------------------|----------------------|
| Flash Loan | High | Very Low | Medium | High |
| Oracle Manipulation | High | Medium-High | Medium | Medium |
| Governance | Medium | Very High | High | Medium |
| Liquidation Exploit | Medium | Medium | Low | Low |
| Re-entrancy | Medium | Low-Medium | Low | Low |
| MEV | Very High | Variable | High | Very High |
| Logic Error | Variable | Variable | Variable | Variable |
| Access Control | Low | Minimal | Low | Low |

---

## Attack Success Factors

### Economic Factors
1. **Profitability Threshold:** Attack profit > (Capital Cost + Gas Cost + Risk Premium)
2. **Capital Efficiency:** Flash loans enable infinite capital efficiency
3. **Slippage Tolerance:** Large trades create market impact
4. **Liquidity Depth:** Low liquidity = easier manipulation

### Technical Factors
1. **Atomicity:** Single-transaction attacks minimize risk
2. **Composability:** Multi-protocol attacks amplify impact
3. **Information Asymmetry:** Mempool access provides advantage
4. **Execution Speed:** Block time constraints

### Protocol Factors
1. **Oracle Design:** Centralized vs decentralized
2. **Governance Model:** Timelock vs immediate execution
3. **Collateralization Ratios:** Safety margin
4. **Emergency Controls:** Circuit breakers, pausing

---

## Defense Taxonomy

### Preventive Controls
- Formal verification
- Extensive testing
- Security audits
- Bug bounties

### Detective Controls
- Real-time monitoring
- Anomaly detection
- On-chain analytics
- Alert systems

### Corrective Controls
- Emergency pause mechanisms
- Governance intervention
- Insurance protocols
- Recovery procedures

---

## Key Insights

1. **Capital Efficiency Revolution:** Flash loans fundamentally changed DeFi attack economics by eliminating capital requirements.

2. **Composability Double-Edged Sword:** Protocol composability enables attacks spanning multiple platforms in single transaction.

3. **Oracle Dependency Risk:** Reliance on external price feeds creates systematic vulnerability.

4. **Economic Rationality:** Most attacks are economically rational - defense must make attacks unprofitable.

5. **Speed Advantage:** Atomic attacks execute faster than human response time, requiring automated defenses.

---

## Statistical Summary (From Dataset)

- **Total Attacks Analyzed:** 181
- **Most Common:** Price Oracle Manipulation (19.3%)
- **Highest ROI:** Flash Loan Attacks (5,743% average)
- **Total Losses:** $75 Million
- **Flash Loan Prevalence:** 27.1% of all attacks
- **Atomic Transaction Rate:** 55.2%
- **Recovery Rate:** 14.9%

---

## References

- SoK: Decentralized Finance (DeFi) Attacks
- Attacking the DeFi Ecosystem with Flash Loans for Fun and Profit
- An Empirical Study of DeFi Liquidations
- Real-world incident database (181 cases)
