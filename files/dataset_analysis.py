"""
Comprehensive DeFi Attacks Dataset Analysis
Statistical analysis, clustering, and visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

class DeFiAttackAnalyzer:
    def __init__(self, dataset_path):
        """Initialize analyzer with dataset"""
        self.df = pd.read_csv(dataset_path)
        self.df['date'] = pd.to_datetime(self.df['date'])
        print(f"Loaded {len(self.df)} attack incidents")
        
    def attack_frequency_analysis(self):
        """Analyze attack frequency by type and over time"""
        print("\n" + "="*80)
        print("ATTACK FREQUENCY ANALYSIS")
        print("="*80)
        
        # Attack type distribution
        attack_counts = self.df['attack_type'].value_counts()
        print("\n📊 Attack Type Distribution:")
        for attack, count in attack_counts.items():
            pct = (count / len(self.df)) * 100
            print(f"  {attack:.<40} {count:>4} ({pct:>5.1f}%)")
        
        # Temporal analysis
        yearly_attacks = self.df.groupby('year').size()
        print("\n📈 Attacks by Year:")
        for year, count in yearly_attacks.items():
            print(f"  {year}: {count} attacks")
        
        # Flash loan usage over time
        flash_loan_yearly = self.df.groupby('year')['flash_loan_used'].sum()
        print("\n⚡ Flash Loan Attacks by Year:")
        for year, count in flash_loan_yearly.items():
            print(f"  {year}: {count} flash loan attacks")
        
        return attack_counts, yearly_attacks
    
    def loss_distribution_analysis(self):
        """Analyze financial losses"""
        print("\n" + "="*80)
        print("FINANCIAL LOSS ANALYSIS")
        print("="*80)
        
        total_loss = self.df['loss_usd'].sum()
        mean_loss = self.df['loss_usd'].mean()
        median_loss = self.df['loss_usd'].median()
        max_loss = self.df['loss_usd'].max()
        
        print(f"\n💰 Total Losses: ${total_loss:,.2f}")
        print(f"📊 Mean Loss per Attack: ${mean_loss:,.2f}")
        print(f"📊 Median Loss: ${median_loss:,.2f}")
        print(f"🔴 Maximum Single Loss: ${max_loss:,.2f}")
        
        # Loss by attack type
        print("\n💸 Average Loss by Attack Type:")
        loss_by_type = self.df.groupby('attack_type')['loss_usd'].agg(['mean', 'sum', 'count'])
        loss_by_type = loss_by_type.sort_values('sum', ascending=False)
        for idx, row in loss_by_type.iterrows():
            print(f"  {idx:.<40} ${row['mean']:>12,.2f} avg (${row['sum']:>12,.0f} total)")
        
        # Loss by protocol type
        print("\n🏦 Average Loss by Protocol Type:")
        loss_by_protocol = self.df.groupby('protocol_type')['loss_usd'].agg(['mean', 'sum'])
        loss_by_protocol = loss_by_protocol.sort_values('sum', ascending=False)
        for idx, row in loss_by_protocol.iterrows():
            print(f"  {idx:.<40} ${row['mean']:>12,.2f} avg (${row['sum']:>12,.0f} total)")
        
        # Top 10 largest attacks
        print("\n🎯 Top 10 Largest Attacks:")
        top_attacks = self.df.nlargest(10, 'loss_usd')[['incident_id', 'date', 'attack_type', 
                                                          'protocol_name', 'loss_usd']]
        for idx, row in top_attacks.iterrows():
            print(f"  #{row['incident_id']:3} | {row['date'].strftime('%Y-%m-%d')} | "
                  f"{row['attack_type']:<25} | {row['protocol_name']:<15} | ${row['loss_usd']:>12,.2f}")
        
        return loss_by_type
    
    def roi_analysis(self):
        """Analyze Return on Investment for attackers"""
        print("\n" + "="*80)
        print("ATTACKER ROI ANALYSIS")
        print("="*80)
        
        # Filter valid ROI values
        valid_roi = self.df[self.df['roi_percent'] > 0]
        
        mean_roi = valid_roi['roi_percent'].mean()
        median_roi = valid_roi['roi_percent'].median()
        max_roi = valid_roi['roi_percent'].max()
        
        print(f"\n📈 Average ROI: {mean_roi:,.1f}%")
        print(f"📊 Median ROI: {median_roi:,.1f}%")
        print(f"🚀 Maximum ROI: {max_roi:,.1f}%")
        
        # ROI by attack type
        print("\n💵 Average ROI by Attack Type:")
        roi_by_type = valid_roi.groupby('attack_type')['roi_percent'].mean().sort_values(ascending=False)
        for attack, roi in roi_by_type.items():
            print(f"  {attack:.<40} {roi:>10,.1f}%")
        
        # High ROI attacks (>100,000%)
        high_roi = valid_roi[valid_roi['roi_percent'] > 100000]
        print(f"\n🎰 Super High ROI Attacks (>100,000%): {len(high_roi)}")
        
        # Flash loan ROI comparison
        flash_roi = self.df[self.df['flash_loan_used']]['roi_percent'].mean()
        non_flash_roi = self.df[~self.df['flash_loan_used']]['roi_percent'].mean()
        print(f"\n⚡ Flash Loan Attack ROI: {flash_roi:,.1f}%")
        print(f"🔒 Non-Flash Loan Attack ROI: {non_flash_roi:,.1f}%")
        
        return valid_roi
    
    def protocol_vulnerability_correlation(self):
        """Analyze correlation between protocol types and vulnerabilities"""
        print("\n" + "="*80)
        print("PROTOCOL VULNERABILITY CORRELATION")
        print("="*80)
        
        # Attack type vs protocol type cross-tabulation
        crosstab = pd.crosstab(self.df['protocol_type'], self.df['attack_type'])
        print("\n📋 Attack Type Distribution by Protocol Type:")
        print(crosstab)
        
        # Most vulnerable protocol types
        vulnerability_score = self.df.groupby('protocol_type').agg({
            'incident_id': 'count',
            'loss_usd': 'sum',
            'complexity': lambda x: (x == 'Critical').sum()
        }).rename(columns={'incident_id': 'attack_count', 'complexity': 'critical_attacks'})
        
        vulnerability_score = vulnerability_score.sort_values('attack_count', ascending=False)
        
        print("\n🎯 Protocol Vulnerability Ranking:")
        for idx, row in vulnerability_score.iterrows():
            print(f"  {idx:.<30} Attacks: {row['attack_count']:>3} | "
                  f"Loss: ${row['loss_usd']:>12,.0f} | Critical: {row['critical_attacks']:>2}")
        
        return crosstab
    
    def temporal_trend_analysis(self):
        """Time series analysis of attacks"""
        print("\n" + "="*80)
        print("TEMPORAL TREND ANALYSIS")
        print("="*80)
        
        # Monthly attack frequency
        monthly_attacks = self.df.groupby([self.df['date'].dt.to_period('M')]).size()
        print(f"\n📅 Monthly Attack Frequency Stats:")
        print(f"  Mean attacks per month: {monthly_attacks.mean():.1f}")
        print(f"  Max attacks in single month: {monthly_attacks.max()}")
        
        # Quarterly analysis
        quarterly = self.df.groupby([self.df['date'].dt.to_period('Q')]).agg({
            'incident_id': 'count',
            'loss_usd': 'sum'
        }).rename(columns={'incident_id': 'attacks', 'loss_usd': 'total_loss'})
        
        print("\n📊 Quarterly Trends (Last 8 quarters):")
        for idx, row in quarterly.tail(8).iterrows():
            print(f"  {idx} | Attacks: {row['attacks']:>3} | Loss: ${row['total_loss']:>12,.2f}")
        
        # Attack sophistication over time
        yearly_complexity = pd.crosstab(self.df['year'], self.df['complexity'])
        print("\n🔬 Attack Complexity Evolution:")
        print(yearly_complexity)
        
        return monthly_attacks, quarterly
    
    def clustering_analysis(self):
        """Perform clustering on attack patterns"""
        print("\n" + "="*80)
        print("ATTACK PATTERN CLUSTERING")
        print("="*80)
        
        # Prepare features for clustering
        features = self.df[[
            'loss_usd', 
            'attacker_capital_required',
            'exploit_chain_length',
            'protocols_involved',
            'time_to_detection_hours'
        ]].copy()
        
        # Handle any infinities or NaNs
        features = features.replace([np.inf, -np.inf], np.nan)
        features = features.fillna(features.median())
        
        # Standardize features
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        
        # K-means clustering
        n_clusters = 4
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(features_scaled)
        
        self.df['cluster'] = clusters
        
        # Analyze clusters
        print(f"\n🔍 Identified {n_clusters} Attack Clusters:")
        for i in range(n_clusters):
            cluster_data = self.df[self.df['cluster'] == i]
            print(f"\n  Cluster {i} ({len(cluster_data)} attacks):")
            print(f"    Avg Loss: ${cluster_data['loss_usd'].mean():,.2f}")
            print(f"    Avg Capital Required: ${cluster_data['attacker_capital_required'].mean():,.2f}")
            print(f"    Avg Chain Length: {cluster_data['exploit_chain_length'].mean():.1f}")
            print(f"    Most Common Attack: {cluster_data['attack_type'].mode().values[0]}")
            print(f"    Flash Loan Usage: {cluster_data['flash_loan_used'].sum()/len(cluster_data)*100:.1f}%")
        
        return clusters, kmeans
    
    def anomaly_detection(self):
        """Detect anomalous attacks"""
        print("\n" + "="*80)
        print("ANOMALY DETECTION")
        print("="*80)
        
        # Define anomalies based on multiple criteria
        
        # 1. Extreme loss events (>3 standard deviations)
        loss_mean = self.df['loss_usd'].mean()
        loss_std = self.df['loss_usd'].std()
        extreme_loss = self.df[self.df['loss_usd'] > loss_mean + 3*loss_std]
        
        print(f"\n🚨 Extreme Loss Events ({len(extreme_loss)}):")
        for idx, row in extreme_loss.iterrows():
            print(f"  Incident #{row['incident_id']}: ${row['loss_usd']:,.2f} - "
                  f"{row['attack_type']} on {row['protocol_name']}")
        
        # 2. Extremely high ROI (>500,000%)
        extreme_roi = self.df[self.df['roi_percent'] > 500000]
        print(f"\n💎 Extreme ROI Events ({len(extreme_roi)}):")
        for idx, row in extreme_roi.head(5).iterrows():
            print(f"  Incident #{row['incident_id']}: {row['roi_percent']:,.0f}% ROI - "
                  f"{row['attack_type']}")
        
        # 3. Complex multi-protocol attacks
        complex_attacks = self.df[self.df['exploit_chain_length'] >= 6]
        print(f"\n🔗 Complex Chain Attacks ({len(complex_attacks)}):")
        for idx, row in complex_attacks.head(5).iterrows():
            print(f"  Incident #{row['incident_id']}: {row['exploit_chain_length']} protocols - "
                  f"{row['attack_type']}")
        
        return extreme_loss, extreme_roi, complex_attacks
    
    def generate_summary_report(self):
        """Generate comprehensive summary report"""
        print("\n" + "="*80)
        print("EXECUTIVE SUMMARY REPORT")
        print("="*80)
        
        print(f"""
 Dataset Overview:
  • Total Incidents Analyzed: {len(self.df)}
  • Date Range: {self.df['date'].min().strftime('%Y-%m-%d')} to {self.df['date'].max().strftime('%Y-%m-%d')}
  • Total Financial Losses: ${self.df['loss_usd'].sum():,.2f}
  
 Key Findings:
  • Most Common Attack: {self.df['attack_type'].mode().values[0]} ({(self.df['attack_type'].value_counts().iloc[0]/len(self.df)*100):.1f}%)
  • Most Vulnerable Protocol Type: {self.df['protocol_type'].value_counts().index[0]}
  • Flash Loan Attack Prevalence: {self.df['flash_loan_used'].sum()/len(self.df)*100:.1f}%
  • Atomic Transaction Rate: {self.df['atomic_transaction'].sum()/len(self.df)*100:.1f}%
  
 Financial Impact:
  • Average Loss per Incident: ${self.df['loss_usd'].mean():,.2f}
  • Median Loss: ${self.df['loss_usd'].median():,.2f}
  • Largest Single Attack: ${self.df['loss_usd'].max():,.2f}
  • Average Attacker ROI: {self.df['roi_percent'].mean():,.0f}%
  
 Flash Loan Insights:
  • Flash Loan Attacks: {self.df['flash_loan_used'].sum()}
  • Average Flash Loan Attack Loss: ${self.df[self.df['flash_loan_used']]['loss_usd'].mean():,.2f}
  • Flash Loan Attack ROI: {self.df[self.df['flash_loan_used']]['roi_percent'].mean():,.0f}%
  
 Attack Sophistication:
  • Critical Complexity Attacks: {(self.df['complexity'] == 'Critical').sum()}
  • Average Exploit Chain Length: {self.df['exploit_chain_length'].mean():.1f} protocols
  • Average Detection Time: {self.df['time_to_detection_hours'].mean():.1f} hours
  
 Recovery Statistics:
  • Incidents with Partial/Full Recovery: {self.df['recovered'].sum()} ({self.df['recovered'].sum()/len(self.df)*100:.1f}%)
  • Unrecovered Losses: ${self.df[~self.df['recovered']]['loss_usd'].sum():,.2f}
        """)

def main():
    """Main analysis workflow"""
    # Initialize analyzer
    analyzer = DeFiAttackAnalyzer('files/defi_attacks_dataset.csv')
    
    # Run all analyses
    analyzer.attack_frequency_analysis()
    analyzer.loss_distribution_analysis()
    analyzer.roi_analysis()
    analyzer.protocol_vulnerability_correlation()
    analyzer.temporal_trend_analysis()
    analyzer.clustering_analysis()
    analyzer.anomaly_detection()
    analyzer.generate_summary_report()
    
    print("\n" + "="*80)
    print("Analysis complete! Results saved.")
    print("="*80)

if __name__ == '__main__':
    main()
