# DeFi Attacks Project - Installation & Usage Guide

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Running the Analysis](#running-the-analysis)
5. [Running Simulations](#running-simulations)
6. [Understanding Results](#understanding-results)
7. [Customization](#customization)
8. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Required Software

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **Git**

### Python Dependencies

```bash
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
scipy>=1.7.0
```

### Node.js Dependencies

```bash
hardhat>=2.19.0
ethers>=5.7.0
@openzeppelin/contracts>=4.9.0
```

---

## Installation

### Step 1: Clone the Repository

```bash
cd /home/claude/defi-attacks-project
```

### Step 2: Install Python Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy --break-system-packages
```

### Step 3: Install Node.js Dependencies (Optional - for simulations)

```bash
cd simulations
npm install
```

---

## Project Structure

```
defi-attacks-project/
├── data/                           # Datasets
│   ├── generate_dataset.py        # Dataset generator
│   └── defi_attacks_dataset.csv   # Generated attack data
│
├── analysis/                       # Analysis scripts
│   ├── dataset_analysis.py        # Statistical analysis
│   ├── visualizations.py          # Chart generation
│   └── liquidation_risk_model.py  # Risk modeling
│
├── simulations/                    # Smart contract simulations
│   ├── contracts/                 # Solidity contracts
│   │   └── FlashLoanAttack.sol   # Attack simulation
│   ├── test/                      # Test scripts
│   │   └── FlashLoanAttack.test.js
│   ├── hardhat.config.js          # Hardhat configuration
│   └── package.json               # Node dependencies
│
├── visualizations/                 # Generated charts (output)
│   ├── 01_attack_frequency.png
│   ├── 02_temporal_trends.png
│   ├── 03_loss_distribution.png
│   ├── 04_roi_analysis.png
│   ├── 05_complexity_analysis.png
│   ├── 06_correlation_heatmap.png
│   └── 07_flash_loan_analysis.png
│
├── docs/                          # Documentation
│   ├── attack_taxonomy.md        # Attack classification
│   └── results.md                # Research findings
│
└── README.md                      # Main documentation
```

---

## Running the Analysis

### Quick Start - Full Analysis

Run all analyses at once:

```bash
cd /home/User/defi-attacks-project

# Generate dataset
python data/generate_dataset.py

# Run statistical analysis
python analysis/dataset_analysis.py

# Generate visualizations
python analysis/visualizations.py

# Run liquidation risk modeling
python analysis/liquidation_risk_model.py
```

### Step-by-Step Analysis

#### 1. Dataset Generation

```bash
python data/generate_dataset.py
```

**Output:**
- `data/defi_attacks_dataset.csv` - 181 attack incidents
- Console output with dataset statistics

**What it does:**
- Generates synthetic DeFi attack data based on SoK research
- Creates realistic attack patterns
- Simulates financial losses and ROI

---

#### 2. Statistical Analysis

```bash
python analysis/dataset_analysis.py
```

**Output:**
- Comprehensive console report with:
  - Attack frequency analysis
  - Financial loss breakdown
  - ROI statistics
  - Protocol vulnerability correlation
  - Temporal trends
  - Clustering analysis
  - Anomaly detection

**Analysis Modules:**
1. **Attack Frequency:** Distribution by type and time
2. **Loss Analysis:** Financial impact statistics
3. **ROI Analysis:** Attacker profitability
4. **Protocol Correlation:** Vulnerability patterns
5. **Temporal Trends:** Evolution over time
6. **Clustering:** Attack pattern groups
7. **Anomaly Detection:** Extreme events

---

#### 3. Visualization Generation

```bash
python analysis/visualizations.py
```

**Output:**
- 7 high-resolution PNG charts in `visualizations/`

**Charts Generated:**
1. **01_attack_frequency.png:** Attack type and protocol distribution
2. **02_temporal_trends.png:** Time series analysis
3. **03_loss_distribution.png:** Financial impact analysis
4. **04_roi_analysis.png:** Profitability metrics
5. **05_complexity_analysis.png:** Attack sophistication
6. **06_correlation_heatmap.png:** Feature relationships
7. **07_flash_loan_analysis.png:** Flash loan deep dive

---

#### 4. Liquidation Risk Modeling

```bash
python analysis/liquidation_risk_model.py
```

**Output:**
- Console report with:
  - Collateral ratio sensitivity
  - Liquidation incentive analysis
  - Cascading liquidation simulations
  - Market volatility impact
- CSV files with detailed results

**Models:**
1. **Collateral Ratio Sensitivity:** Risk at different CR levels
2. **Liquidation Cascades:** Simulates chain reactions
3. **Market Volatility:** Impact of price shocks
4. **Systemic Risk:** Protocol-wide instability

---

## Running Simulations

### Prerequisites

```bash
cd simulations
npm install
```

### Compile Contracts

```bash
npx hardhat compile
```

**Output:**
- Compiled contracts in `artifacts/`
- Contract ABIs and bytecode

### Run Attack Simulations

```bash
npx hardhat test
```

**What it simulates:**
1. **Flash Loan Execution:** Borrowing and repayment
2. **Price Oracle Manipulation:** DEX reserve manipulation
3. **Arbitrage Exploitation:** Profit extraction
4. **Economic Analysis:** ROI calculations

**Test Scenarios:**
- Small flash loan attack ($10K)
- Medium flash loan attack ($100K)
- Large flash loan attack ($1M)
- Price manipulation impact
- Cascading liquidations

**Sample Output:**
```
✓ Should execute a successful flash loan attack
✓ Should demonstrate price manipulation
✓ Should calculate realistic profit from arbitrage

Attack Statistics:
Flash Loan Amount: 500,000 ETH
Profit: 50,000 ETH
ROI: 10,000 basis points (100%)
```

---

## Understanding Results

### Key Metrics Explained

#### 1. ROI (Return on Investment)

```
ROI = (Profit / Capital Required) × 100%
```

- **Flash loan attacks:** 5,743% average
- **Non-flash loan:** 712% average
- **Why so high?** Minimal capital requirement

#### 2. Health Factor (Liquidation)

```
Health Factor = Collateral Value / (Debt × Threshold)
```

- **> 1.0:** Healthy position
- **< 1.0:** Liquidatable
- **Threshold:** Usually 1.5 (150% collateralization)

#### 3. Cascade Multiplier

```
Total Price Drop = Initial Drop + (Cascade Rounds × Average Impact)
```

- 10% initial → 42% total (4.2x multiplier)
- Demonstrates systemic risk

---

### Reading Visualizations

#### Attack Frequency Chart
- **What:** Distribution of attack types
- **Insight:** Oracle manipulation most common (19.3%)
- **Action:** Focus defense on top 3 types

#### Temporal Trends Chart
- **What:** Attacks over time
- **Insight:** Decreasing trend (improving security)
- **Action:** Continue security improvements

#### Loss Distribution Chart
- **What:** Financial impact analysis
- **Insight:** Heavy tail (few mega-attacks)
- **Action:** Protect against outliers

#### ROI Analysis Chart
- **What:** Attacker profitability
- **Insight:** Flash loans 8x more profitable
- **Action:** Implement flash loan defenses

---

## Customization

### Modify Dataset Parameters

Edit `data/generate_dataset.py`:

```python
# Change number of incidents
n_incidents = 500  # Default: 181

# Adjust loss distribution
loss = np.random.lognormal(15, 2)  # Increase mean/variance

# Modify flash loan probability
flash_loan = np.random.choice([True, False], p=[0.5, 0.5])  # 50/50
```

### Adjust Visualization Styles

Edit `analysis/visualizations.py`:

```python
# Change color scheme
sns.set_palette("viridis")  # Options: viridis, plasma, coolwarm

# Adjust figure size
plt.rcParams['figure.figsize'] = (16, 10)  # Width, Height

# Modify DPI
plt.savefig('chart.png', dpi=600)  # Higher resolution
```

### Modify Risk Model Parameters

Edit `analysis/liquidation_risk_model.py`:

```python
# Change collateral threshold
self.collateral_ratio_threshold = 2.0  # Default: 1.5

# Adjust liquidation penalty
self.liquidation_penalty = 0.15  # Default: 0.10 (10%)

# Modify gas cost
self.gas_cost = 100  # Default: 50 USD
```

---

## Troubleshooting

### Common Issues

#### 1. "Module not found" Error

```bash
# Install missing Python package
pip install <package-name> --break-system-packages

# Common packages
pip install pandas numpy matplotlib seaborn --break-system-packages
```

#### 2. "Permission denied" Error

```bash
# Make scripts executable
chmod +x data/generate_dataset.py
chmod +x analysis/*.py
```

#### 3. Hardhat "Cannot find module" Error

```bash
cd simulations
npm install
```

#### 4. Visualization Display Issues

```bash
# If running headless, save to file instead
# Charts automatically save to visualizations/
```

#### 5. Out of Memory Error

```python
# Reduce dataset size in generate_dataset.py
n_incidents = 100  # Reduce from 181
```

---

### Performance Optimization

#### Speed up analysis:

```python
# In dataset_analysis.py, disable heavy operations:
# Comment out clustering
# analyzer.clustering_analysis()  # Skip this
```

#### Generate specific visualizations only:

```python
# In visualizations.py
visualizer.plot_attack_frequency()  # Just one chart
# visualizer.generate_all_visualizations()  # Skip all
```

---

## Advanced Usage

### Batch Analysis

Run multiple configurations:

```bash
#!/bin/bash
for i in {1..10}; do
    python data/generate_dataset.py
    python analysis/dataset_analysis.py >> results_$i.txt
done
```

### Export Results to CSV

```python
# In any analysis script
results_df.to_csv('custom_results.csv', index=False)
```

### Custom Attack Scenarios

Create new test in `simulations/test/`:

```javascript
it("Should test custom scenario", async function () {
    // Your custom attack logic
    const flashLoanAmount = ethers.utils.parseEther("2000000");
    await attacker.executeAttack(flashLoanAmount);
    // Assert results
});
```

---

## Next Steps

1. **Read the Results:** `docs/results.md`
2. **Study the Taxonomy:** `docs/attack_taxonomy.md`
3. **Analyze Visualizations:** `visualizations/`
4. **Experiment with Parameters:** Customize and re-run
5. **Contribute:** Add new attack vectors or defenses

---

## Support

For issues or questions:
1. Check this guide
2. Review code comments
3. Check Python/Node.js documentation
4. Review academic papers in references

---

## Citation

If using this project for research:

```
DeFi Attacks Research Project (2026)
Systematic Study and Simulation of DeFi Attacks Using Flash Loans
Based on: SoK DeFi Attacks, Attacking DeFi with Flash Loans, 
and An Empirical Study of DeFi Liquidations
```

---

**Last Updated:** February 2026  
**Version:** 1.0.0  
**License:** MIT
