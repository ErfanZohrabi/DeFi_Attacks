# Systematic Study and Simulation of DeFi Attacks Using Flash Loans

## 🎯 Project Overview

This project provides a comprehensive analysis of Decentralized Finance (DeFi) attacks, focusing on flash loan exploits and liquidation instabilities. It includes:

- **Attack Systematization**: Taxonomy and classification of DeFi attack vectors
- **Attack Simulation**: Reproduction of real-world flash loan attacks
- **Dataset Analysis**: Statistical analysis of 181 real-world DeFi incidents
- **Liquidation Risk Modeling**: Economic instability analysis
- **Defense Mechanisms**: Evaluation of mitigation strategies

## 📊 Key Statistics

- **$3.24 Billion** lost between 2018-2022
- **181** real-world incidents analyzed
- **77** academic papers reviewed
- **ROI > 500,000%** achievable in some flash loan attacks

## 🗂️ Project Structure

```
defi-attacks-project/
├── data/                   # Dataset and raw data
├── simulations/            # Smart contract attack simulations
├── analysis/               # Statistical analysis scripts
├── visualizations/         # Charts and graphs
├── docs/                   # Documentation
└── README.md
```

## 🔬 Components

### 1. Attack Taxonomy
Classification of DeFi attacks by:
- Attack vector
- Capital requirements
- Atomicity
- Protocol dependency
- Economic impact

### 2. Flash Loan Attack Simulation
Reproduction of:
- bZx Protocol exploit
- Price oracle manipulation
- Arbitrage opportunities
- Liquidation cascades

### 3. Dataset Analysis
- Attack frequency analysis
- Loss distribution
- Temporal trends
- Protocol vulnerability correlation

### 4. Liquidation Risk Modeling
- Collateral ratio sensitivity
- Cascading liquidation effects
- Market volatility impact

## 🚀 Getting Started

### Prerequisites
```bash
# Python dependencies
pip install pandas numpy matplotlib seaborn web3 scikit-learn networkx --break-system-packages

# Blockchain development tools
npm install --save-dev hardhat @nomiclabs/hardhat-ethers ethers @openzeppelin/contracts
```

### Installation
```bash
git clone <repository-url>
cd defi-attacks-project
npm install
```

### Running Analysis
```bash
# Dataset analysis
python analysis/dataset_analysis.py

# Attack simulation
cd simulations
npx hardhat test

# Generate visualizations
python analysis/visualizations.py
```

## 📈 Results Summary

See detailed results in `/docs/results.md`

## 🛡️ Defense Mechanisms Evaluated

1. Time-Weighted Average Price (TWAP) oracles
2. Flash loan resistant governance
3. Circuit breakers
4. Liquidity caps
5. Oracle decentralization

## 📚 References

- [SoK: DeFi Attacks Dataset](https://github.com/Research-Imperium/SoKDeFiAttacks)
- [Attacking the DeFi Ecosystem with Flash Loans](https://arxiv.org/abs/2003.03810)
- [DeFi Liquidations Study](https://arxiv.org/pdf/2106.06389.pdf)

## 📝 License

MIT License

## 👥 Author

Research Project - MSc Thesis on DeFi Security
