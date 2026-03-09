"""
DeFi Attacks Visualization Suite
Generate comprehensive charts and graphs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

class DeFiVisualizer:
    def __init__(self, dataset_path):
        """Initialize visualizer with dataset"""
        self.df = pd.read_csv(dataset_path)
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.output_dir = '/home/User/defi-attacks-project/visualizations'
        
    def plot_attack_frequency(self):
        """Plot attack type frequency distribution"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Attack type distribution
        attack_counts = self.df['attack_type'].value_counts()
        colors = sns.color_palette("husl", len(attack_counts))
        ax1.barh(range(len(attack_counts)), attack_counts.values, color=colors)
        ax1.set_yticks(range(len(attack_counts)))
        ax1.set_yticklabels(attack_counts.index, fontsize=9)
        ax1.set_xlabel('Number of Attacks', fontweight='bold')
        ax1.set_title('DeFi Attack Type Distribution', fontsize=14, fontweight='bold')
        ax1.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, v in enumerate(attack_counts.values):
            ax1.text(v + 0.5, i, str(v), va='center', fontweight='bold')
        
        # Protocol type distribution
        protocol_counts = self.df['protocol_type'].value_counts()
        ax2.bar(range(len(protocol_counts)), protocol_counts.values, 
                color=sns.color_palette("muted", len(protocol_counts)))
        ax2.set_xticks(range(len(protocol_counts)))
        ax2.set_xticklabels(protocol_counts.index, rotation=45, ha='right', fontsize=9)
        ax2.set_ylabel('Number of Attacks', fontweight='bold')
        ax2.set_title('Attacks by Protocol Type', fontsize=14, fontweight='bold')
        ax2.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for i, v in enumerate(protocol_counts.values):
            ax2.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/01_attack_frequency.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 01_attack_frequency.png")
        plt.close()
    
    def plot_temporal_trends(self):
        """Plot temporal attack trends"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Yearly attack count
        yearly = self.df.groupby('year').size()
        axes[0, 0].plot(yearly.index, yearly.values, marker='o', linewidth=2, 
                        markersize=8, color='#e74c3c')
        axes[0, 0].fill_between(yearly.index, yearly.values, alpha=0.3, color='#e74c3c')
        axes[0, 0].set_xlabel('Year', fontweight='bold')
        axes[0, 0].set_ylabel('Number of Attacks', fontweight='bold')
        axes[0, 0].set_title('Attack Frequency Over Time', fontsize=12, fontweight='bold')
        axes[0, 0].grid(alpha=0.3)
        
        # Yearly losses
        yearly_loss = self.df.groupby('year')['loss_usd'].sum() / 1e6  # Convert to millions
        axes[0, 1].bar(yearly_loss.index, yearly_loss.values, color='#3498db', alpha=0.7)
        axes[0, 1].set_xlabel('Year', fontweight='bold')
        axes[0, 1].set_ylabel('Total Losses (Million USD)', fontweight='bold')
        axes[0, 1].set_title('Total Financial Losses by Year', fontsize=12, fontweight='bold')
        axes[0, 1].grid(axis='y', alpha=0.3)
        
        # Monthly trend
        monthly = self.df.groupby(self.df['date'].dt.to_period('M')).size()
        axes[1, 0].plot(range(len(monthly)), monthly.values, linewidth=2, color='#2ecc71')
        axes[1, 0].fill_between(range(len(monthly)), monthly.values, alpha=0.3, color='#2ecc71')
        axes[1, 0].set_xlabel('Time (Months)', fontweight='bold')
        axes[1, 0].set_ylabel('Attacks per Month', fontweight='bold')
        axes[1, 0].set_title('Monthly Attack Frequency', fontsize=12, fontweight='bold')
        axes[1, 0].grid(alpha=0.3)
        
        # Flash loan usage over time
        flash_yearly = self.df.groupby('year')['flash_loan_used'].sum()
        total_yearly = self.df.groupby('year').size()
        flash_pct = (flash_yearly / total_yearly * 100)
        axes[1, 1].plot(flash_pct.index, flash_pct.values, marker='s', 
                        linewidth=2, markersize=8, color='#9b59b6')
        axes[1, 1].set_xlabel('Year', fontweight='bold')
        axes[1, 1].set_ylabel('Flash Loan Usage (%)', fontweight='bold')
        axes[1, 1].set_title('Flash Loan Attack Prevalence Over Time', 
                             fontsize=12, fontweight='bold')
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/02_temporal_trends.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 02_temporal_trends.png")
        plt.close()
    
    def plot_loss_distribution(self):
        """Plot loss distribution analysis"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Log-scale histogram
        losses = self.df['loss_usd']
        axes[0, 0].hist(np.log10(losses), bins=30, color='#e67e22', alpha=0.7, edgecolor='black')
        axes[0, 0].set_xlabel('Log10(Loss in USD)', fontweight='bold')
        axes[0, 0].set_ylabel('Frequency', fontweight='bold')
        axes[0, 0].set_title('Loss Distribution (Log Scale)', fontsize=12, fontweight='bold')
        axes[0, 0].grid(alpha=0.3)
        
        # Box plot by attack type
        top_attacks = self.df['attack_type'].value_counts().head(6).index
        data_to_plot = [self.df[self.df['attack_type'] == at]['loss_usd'] for at in top_attacks]
        bp = axes[0, 1].boxplot(data_to_plot, labels=top_attacks, patch_artist=True)
        for patch in bp['boxes']:
            patch.set_facecolor('#3498db')
            patch.set_alpha(0.7)
        axes[0, 1].set_xticklabels(top_attacks, rotation=45, ha='right', fontsize=8)
        axes[0, 1].set_ylabel('Loss (USD)', fontweight='bold')
        axes[0, 1].set_title('Loss Distribution by Attack Type', fontsize=12, fontweight='bold')
        axes[0, 1].set_yscale('log')
        axes[0, 1].grid(alpha=0.3)
        
        # Cumulative loss
        sorted_losses = np.sort(losses)[::-1]
        cumulative = np.cumsum(sorted_losses) / sorted_losses.sum() * 100
        axes[1, 0].plot(range(len(cumulative)), cumulative, linewidth=2, color='#e74c3c')
        axes[1, 0].axhline(y=80, color='gray', linestyle='--', alpha=0.5)
        axes[1, 0].set_xlabel('Number of Attacks', fontweight='bold')
        axes[1, 0].set_ylabel('Cumulative Loss (%)', fontweight='bold')
        axes[1, 0].set_title('Cumulative Loss Distribution (Pareto Analysis)', 
                             fontsize=12, fontweight='bold')
        axes[1, 0].grid(alpha=0.3)
        
        # Loss by protocol type
        loss_by_protocol = self.df.groupby('protocol_type')['loss_usd'].sum().sort_values(ascending=True)
        axes[1, 1].barh(range(len(loss_by_protocol)), loss_by_protocol.values / 1e6,
                        color=sns.color_palette("viridis", len(loss_by_protocol)))
        axes[1, 1].set_yticks(range(len(loss_by_protocol)))
        axes[1, 1].set_yticklabels(loss_by_protocol.index, fontsize=9)
        axes[1, 1].set_xlabel('Total Loss (Million USD)', fontweight='bold')
        axes[1, 1].set_title('Total Losses by Protocol Type', fontsize=12, fontweight='bold')
        axes[1, 1].grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/03_loss_distribution.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 03_loss_distribution.png")
        plt.close()
    
    def plot_roi_analysis(self):
        """Plot ROI analysis"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        valid_roi = self.df[self.df['roi_percent'] > 0]
        
        # ROI distribution
        axes[0, 0].hist(np.log10(valid_roi['roi_percent']), bins=30, 
                        color='#16a085', alpha=0.7, edgecolor='black')
        axes[0, 0].set_xlabel('Log10(ROI %)', fontweight='bold')
        axes[0, 0].set_ylabel('Frequency', fontweight='bold')
        axes[0, 0].set_title('Attack ROI Distribution', fontsize=12, fontweight='bold')
        axes[0, 0].grid(alpha=0.3)
        
        # ROI by attack type
        roi_by_type = valid_roi.groupby('attack_type')['roi_percent'].mean().sort_values(ascending=True)
        axes[0, 1].barh(range(len(roi_by_type)), roi_by_type.values,
                        color=sns.color_palette("coolwarm", len(roi_by_type)))
        axes[0, 1].set_yticks(range(len(roi_by_type)))
        axes[0, 1].set_yticklabels(roi_by_type.index, fontsize=9)
        axes[0, 1].set_xlabel('Average ROI (%)', fontweight='bold')
        axes[0, 1].set_title('Average ROI by Attack Type', fontsize=12, fontweight='bold')
        axes[0, 1].grid(axis='x', alpha=0.3)
        
        # Capital required vs ROI scatter
        axes[1, 0].scatter(valid_roi['attacker_capital_required'], 
                          valid_roi['roi_percent'],
                          alpha=0.5, c=valid_roi['flash_loan_used'].map({True: '#e74c3c', False: '#3498db'}),
                          s=50)
        axes[1, 0].set_xlabel('Capital Required (USD)', fontweight='bold')
        axes[1, 0].set_ylabel('ROI (%)', fontweight='bold')
        axes[1, 0].set_xscale('log')
        axes[1, 0].set_yscale('log')
        axes[1, 0].set_title('Capital Required vs ROI', fontsize=12, fontweight='bold')
        axes[1, 0].grid(alpha=0.3)
        axes[1, 0].legend(['Flash Loan', 'No Flash Loan'], loc='best')
        
        # Flash loan vs non-flash loan ROI comparison
        flash_roi = valid_roi[valid_roi['flash_loan_used']]['roi_percent']
        non_flash_roi = valid_roi[~valid_roi['flash_loan_used']]['roi_percent']
        
        bp = axes[1, 1].boxplot([flash_roi, non_flash_roi], 
                                 labels=['Flash Loan', 'No Flash Loan'],
                                 patch_artist=True)
        bp['boxes'][0].set_facecolor('#e74c3c')
        bp['boxes'][1].set_facecolor('#3498db')
        for box in bp['boxes']:
            box.set_alpha(0.7)
        axes[1, 1].set_ylabel('ROI (%)', fontweight='bold')
        axes[1, 1].set_title('ROI Comparison: Flash Loan vs Non-Flash Loan', 
                             fontsize=12, fontweight='bold')
        axes[1, 1].set_yscale('log')
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/04_roi_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 04_roi_analysis.png")
        plt.close()
    
    def plot_complexity_analysis(self):
        """Plot attack complexity and sophistication"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Complexity distribution
        complexity_counts = self.df['complexity'].value_counts()
        colors = {'Low': '#2ecc71', 'Medium': '#f39c12', 'High': '#e67e22', 'Critical': '#e74c3c'}
        axes[0, 0].pie(complexity_counts.values, labels=complexity_counts.index,
                       autopct='%1.1f%%', startangle=90,
                       colors=[colors[c] for c in complexity_counts.index])
        axes[0, 0].set_title('Attack Complexity Distribution', fontsize=12, fontweight='bold')
        
        # Exploit chain length
        axes[0, 1].hist(self.df['exploit_chain_length'], bins=range(1, 10), 
                        color='#9b59b6', alpha=0.7, edgecolor='black')
        axes[0, 1].set_xlabel('Exploit Chain Length (# of Protocols)', fontweight='bold')
        axes[0, 1].set_ylabel('Frequency', fontweight='bold')
        axes[0, 1].set_title('Exploit Chain Length Distribution', fontsize=12, fontweight='bold')
        axes[0, 1].grid(alpha=0.3)
        
        # Time to detection
        axes[1, 0].hist(np.log10(self.df['time_to_detection_hours'] + 0.01), bins=30,
                        color='#1abc9c', alpha=0.7, edgecolor='black')
        axes[1, 0].set_xlabel('Log10(Detection Time in Hours)', fontweight='bold')
        axes[1, 0].set_ylabel('Frequency', fontweight='bold')
        axes[1, 0].set_title('Time to Detection Distribution', fontsize=12, fontweight='bold')
        axes[1, 0].grid(alpha=0.3)
        
        # Complexity evolution over time
        complexity_yearly = pd.crosstab(self.df['year'], self.df['complexity'], normalize='index') * 100
        complexity_yearly.plot(kind='bar', stacked=True, ax=axes[1, 1],
                              color=[colors[c] for c in complexity_yearly.columns])
        axes[1, 1].set_xlabel('Year', fontweight='bold')
        axes[1, 1].set_ylabel('Percentage (%)', fontweight='bold')
        axes[1, 1].set_title('Attack Complexity Evolution Over Time', 
                             fontsize=12, fontweight='bold')
        axes[1, 1].legend(title='Complexity', bbox_to_anchor=(1.05, 1), loc='upper left')
        axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=0)
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/05_complexity_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 05_complexity_analysis.png")
        plt.close()
    
    def plot_correlation_heatmap(self):
        """Plot correlation heatmap of numerical features"""
        fig, ax = plt.subplots(figsize=(12, 10))
        
        # Select numerical columns
        numerical_cols = ['loss_usd', 'attacker_capital_required', 'roi_percent',
                         'exploit_chain_length', 'protocols_involved', 
                         'time_to_detection_hours']
        
        corr_matrix = self.df[numerical_cols].corr()
        
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                   ax=ax)
        ax.set_title('Feature Correlation Heatmap', fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/06_correlation_heatmap.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 06_correlation_heatmap.png")
        plt.close()
    
    def plot_flash_loan_analysis(self):
        """Detailed flash loan attack analysis"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        flash_df = self.df[self.df['flash_loan_used']]
        non_flash_df = self.df[~self.df['flash_loan_used']]
        
        # Flash loan vs non-flash loan attack count
        categories = ['Flash Loan', 'No Flash Loan']
        counts = [len(flash_df), len(non_flash_df)]
        axes[0, 0].bar(categories, counts, color=['#e74c3c', '#3498db'], alpha=0.7)
        axes[0, 0].set_ylabel('Number of Attacks', fontweight='bold')
        axes[0, 0].set_title('Flash Loan Usage Distribution', fontsize=12, fontweight='bold')
        axes[0, 0].grid(axis='y', alpha=0.3)
        for i, v in enumerate(counts):
            axes[0, 0].text(i, v + 1, str(v), ha='center', fontweight='bold', fontsize=12)
        
        # Average loss comparison
        avg_losses = [flash_df['loss_usd'].mean(), non_flash_df['loss_usd'].mean()]
        axes[0, 1].bar(categories, avg_losses, color=['#e74c3c', '#3498db'], alpha=0.7)
        axes[0, 1].set_ylabel('Average Loss (USD)', fontweight='bold')
        axes[0, 1].set_title('Average Loss: Flash Loan vs Non-Flash Loan', 
                             fontsize=12, fontweight='bold')
        axes[0, 1].grid(axis='y', alpha=0.3)
        
        # Flash loan attack types
        flash_attack_types = flash_df['attack_type'].value_counts()
        axes[1, 0].barh(range(len(flash_attack_types)), flash_attack_types.values,
                        color=sns.color_palette("Reds_r", len(flash_attack_types)))
        axes[1, 0].set_yticks(range(len(flash_attack_types)))
        axes[1, 0].set_yticklabels(flash_attack_types.index, fontsize=9)
        axes[1, 0].set_xlabel('Number of Attacks', fontweight='bold')
        axes[1, 0].set_title('Flash Loan Attack Types', fontsize=12, fontweight='bold')
        axes[1, 0].grid(axis='x', alpha=0.3)
        
        # Atomicity comparison
        flash_atomic = flash_df['atomic_transaction'].sum()
        flash_non_atomic = len(flash_df) - flash_atomic
        non_flash_atomic = non_flash_df['atomic_transaction'].sum()
        non_flash_non_atomic = len(non_flash_df) - non_flash_atomic
        
        x = np.arange(2)
        width = 0.35
        axes[1, 1].bar(x - width/2, [flash_atomic, non_flash_atomic], width, 
                      label='Atomic', color='#2ecc71', alpha=0.7)
        axes[1, 1].bar(x + width/2, [flash_non_atomic, non_flash_non_atomic], width,
                      label='Non-Atomic', color='#95a5a6', alpha=0.7)
        axes[1, 1].set_ylabel('Number of Attacks', fontweight='bold')
        axes[1, 1].set_title('Atomicity: Flash Loan vs Non-Flash Loan', 
                             fontsize=12, fontweight='bold')
        axes[1, 1].set_xticks(x)
        axes[1, 1].set_xticklabels(categories)
        axes[1, 1].legend()
        axes[1, 1].grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/07_flash_loan_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Generated: 07_flash_loan_analysis.png")
        plt.close()
    
    def generate_all_visualizations(self):
        """Generate all visualizations"""
        print("\n" + "="*80)
        print("GENERATING VISUALIZATIONS")
        print("="*80 + "\n")
        
        self.plot_attack_frequency()
        self.plot_temporal_trends()
        self.plot_loss_distribution()
        self.plot_roi_analysis()
        self.plot_complexity_analysis()
        self.plot_correlation_heatmap()
        self.plot_flash_loan_analysis()
        
        print("\n" + "="*80)
        print("All visualizations generated successfully!")
        print(f"Output directory: {self.output_dir}")
        print("="*80)

def main():
    """Main visualization workflow"""
    visualizer = DeFiVisualizer('/home/User/defi-attacks-project/data/defi_attacks_dataset.csv')
    visualizer.generate_all_visualizations()

if __name__ == '__main__':
    main()
