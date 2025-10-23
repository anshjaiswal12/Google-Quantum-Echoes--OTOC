#!/usr/bin/env python3
"""
Quantum Information Spreading in Molecules - Simplified Version
Scientific Visualization for Research Presentation
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
from datetime import datetime
import os

def create_quantum_molecule_visualization():
    """Create a detailed scientific visualization of quantum information spreading"""
    
    # Set up the plot with larger figure size
    fig = plt.figure(figsize=(24, 18))
    
    # Create 6 subplots showing different time steps
    time_steps = [0, 2, 4, 6, 8, 10]
    axes = []
    
    for i in range(6):
        ax = fig.add_subplot(2, 3, i+1, projection='3d')
        axes.append(ax)
    
    # Define molecular structure (benzene-like with side chains)
    def create_molecule():
        # Benzene ring
        benzene_ring = []
        for i in range(6):
            angle = i * np.pi / 3
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            z = 0
            benzene_ring.append([x, y, z, 'C'])
        
        # Add side chains and functional groups
        side_chains = [
            [4, 0, 0, 'O'],      # Hydroxyl
            [4.7, 0, 0, 'H'],
            [-4, 0, 0, 'C'],     # Methyl
            [-4.7, 0.5, 0, 'H'],
            [-4.7, -0.5, 0, 'H'],
            [-4.7, 0, 0.5, 'H'],
            [0, 4, 0, 'N'],      # Amino
            [0, 4.7, 0, 'H'],
            [0.5, 4.3, 0, 'H'],
            [2, 2, 1.5, 'C'],    # Additional complexity
            [2.7, 2.7, 1.5, 'H'],
            [1.3, 2.7, 1.5, 'H'],
            [2.7, 1.3, 1.5, 'H'],
            [-2, -2, -1.5, 'C'],
            [-2.7, -2.7, -1.5, 'H'],
            [-1.3, -2.7, -1.5, 'H'],
            [-2.7, -1.3, -1.5, 'H'],
        ]
        
        return np.array(benzene_ring + side_chains)
    
    # Calculate quantum correlations
    def calculate_correlations(molecule, time_step, perturbation_point):
        correlations = {}
        positions = molecule[:, :3].astype(float)
        atom_types = molecule[:, 3]
        
        for i, (pos, atom_type) in enumerate(zip(positions, atom_types)):
            dist = np.linalg.norm(pos - perturbation_point)
            
            # Quantum information spreading with oscillations
            correlation = np.exp(-dist / 3.0) * np.cos(2 * np.pi * time_step / 5.0 - dist)
            
            # Different atom types have different behaviors
            if atom_type == 'C':
                base = 0.8
            elif atom_type == 'N':
                base = 0.9
            elif atom_type == 'O':
                base = 0.7
            else:  # H
                base = 0.6
            
            correlations[i] = {
                'position': pos,
                'atom_type': atom_type,
                'correlation': base * correlation,
                'distance': dist
            }
        
        return correlations
    
    # Create quantum waves
    def create_waves(perturbation_point, time_step):
        waves = []
        center = perturbation_point
        
        for radius in np.linspace(0.5, 6, 10):
            amplitude = np.exp(-radius / 4.0) * np.cos(2 * np.pi * time_step / 3.0 - radius)
            
            if abs(amplitude) > 0.1:
                theta = np.linspace(0, 2 * np.pi, 30)
                x = center[0] + radius * np.cos(theta)
                y = center[1] + radius * np.sin(theta)
                z = center[2] + amplitude * 0.5
                waves.append({'x': x, 'y': y, 'z': z, 'amplitude': amplitude})
        
        return waves
    
    # Create entanglement connections
    def create_connections(correlations):
        connections = []
        positions = [correlations[i]['position'] for i in correlations]
        
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                corr_i = correlations[i]['correlation']
                corr_j = correlations[j]['correlation']
                distance = np.linalg.norm(positions[i] - positions[j])
                
                strength = (corr_i + corr_j) / 2 * np.exp(-distance / 3.0)
                
                if strength > 0.3:
                    connections.append({
                        'start': positions[i],
                        'end': positions[j],
                        'strength': strength
                    })
        
        return connections
    
    # Main visualization
    molecule = create_molecule()
    perturbation_point = np.array([2, 0, 0])  # Initial perturbation
    
    for idx, (ax, time_step) in enumerate(zip(axes, time_steps)):
        # Calculate quantum state
        correlations = calculate_correlations(molecule, time_step, perturbation_point)
        waves = create_waves(perturbation_point, time_step)
        connections = create_connections(correlations)
        
        # Plot atoms
        for i, data in correlations.items():
            pos = data['position']
            atom_type = data['atom_type']
            correlation = data['correlation']
            
            # Atom colors and sizes
            colors = {'C': '#404040', 'N': '#3050F8', 'O': '#FF0D0D', 'H': '#FFFFFF'}
            size = 200 + 400 * abs(correlation)
            alpha = 0.6 + 0.4 * abs(correlation)
            
            ax.scatter(pos[0], pos[1], pos[2], 
                      c=colors[atom_type], s=size, alpha=alpha,
                      edgecolors='white', linewidth=1)
        
        # Plot quantum waves
        for wave in waves:
            alpha = 0.4 * abs(wave['amplitude'])
            color = 'cyan' if wave['amplitude'] > 0 else 'magenta'
            ax.plot(wave['x'], wave['y'], wave['z'], 
                   color=color, alpha=alpha, linewidth=3)
        
        # Plot entanglement connections
        for conn in connections:
            start, end = conn['start'], conn['end']
            strength = conn['strength']
            
            alpha = 0.3 + 0.7 * strength
            linewidth = 1 + 4 * strength
            
            if strength > 0.7:
                color = 'yellow'
            elif strength > 0.5:
                color = 'orange'
            else:
                color = 'red'
            
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
                   color=color, alpha=alpha, linewidth=linewidth)
        
        # Highlight perturbation point
        ax.scatter(perturbation_point[0], perturbation_point[1], perturbation_point[2],
                  c='yellow', s=600, alpha=0.9, edgecolors='red', linewidth=4)
        
        # Add pulsing effect around perturbation
        for i in range(3):
            radius = 0.5 + i * 0.4
            alpha = 0.2 - i * 0.05
            ax.scatter(perturbation_point[0], perturbation_point[1], perturbation_point[2],
                      c='yellow', s=600*radius, alpha=alpha)
        
        # Set plot properties
        ax.set_title(f'Time Step {time_step}\nCorrelation: {np.mean([c["correlation"] for c in correlations.values()]):.3f}', 
                    fontsize=12, fontweight='bold', pad=20)
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.set_zlim(-3, 3)
        ax.set_xlabel('X (Å)', fontsize=11)
        ax.set_ylabel('Y (Å)', fontsize=11)
        ax.set_zlabel('Z (Å)', fontsize=11)
        
        # Set viewing angle
        ax.view_init(elev=20, azim=45)
        ax.set_facecolor('black')
    
    # Add main title and explanation
    fig.suptitle('Quantum Information Spreading in Molecular Systems\n'
                'Chain Reaction Visualization: Small Perturbation → Global Correlation', 
                fontsize=16, fontweight='bold', y=0.95)
    
    # Add color legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#404040', 
                   markersize=10, label='Carbon (C)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#3050F8', 
                   markersize=10, label='Nitrogen (N)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF0D0D', 
                   markersize=10, label='Oxygen (O)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFFFFF', 
                   markersize=10, label='Hydrogen (H)'),
        plt.Line2D([0], [0], color='yellow', linewidth=3, label='Strong Entanglement'),
        plt.Line2D([0], [0], color='orange', linewidth=3, label='Medium Entanglement'),
        plt.Line2D([0], [0], color='red', linewidth=3, label='Weak Entanglement'),
        plt.Line2D([0], [0], color='cyan', linewidth=3, label='Quantum Waves'),
    ]
    
    fig.legend(handles=legend_elements, loc='center', bbox_to_anchor=(0.5, 0.02), 
              ncol=4, fontsize=12)
    
    # Adjust layout to prevent overlapping with more space
    plt.subplots_adjust(top=0.90, bottom=0.15, left=0.05, right=0.95, hspace=0.3, wspace=0.2)
    plt.tight_layout()
    
    # Save the visualization
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"quantum_molecule_chain_reaction_{timestamp}.png"
    filepath = os.path.join(".", filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Quantum molecule visualization saved: {filepath}")
    
    return fig

def create_single_frame_visualization():
    """Create a single detailed frame showing the quantum information spreading"""
    
    fig = plt.figure(figsize=(18, 14))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create molecule structure
    def create_complex_molecule():
        # Main benzene ring
        benzene = []
        for i in range(6):
            angle = i * np.pi / 3
            x = 3 * np.cos(angle)
            y = 3 * np.sin(angle)
            z = 0
            benzene.append([x, y, z, 'C'])
        
        # Add complex side chains
        side_chains = [
            # Hydroxyl group
            [5, 0, 0, 'O'], [5.7, 0, 0, 'H'],
            # Methyl group  
            [-5, 0, 0, 'C'], [-5.7, 0.5, 0, 'H'], [-5.7, -0.5, 0, 'H'], [-5.7, 0, 0.5, 'H'],
            # Amino group
            [0, 5, 0, 'N'], [0, 5.7, 0, 'H'], [0.5, 5.3, 0, 'H'],
            # Additional complexity
            [3, 3, 2, 'C'], [3.7, 3.7, 2, 'H'], [2.3, 3.7, 2, 'H'], [3.7, 2.3, 2, 'H'],
            [-3, -3, -2, 'C'], [-3.7, -3.7, -2, 'H'], [-2.3, -3.7, -2, 'H'], [-3.7, -2.3, -2, 'H'],
            # More side chains
            [0, -5, 0, 'C'], [0, -5.7, 0.5, 'H'], [0, -5.7, -0.5, 'H'], [0.5, -5.3, 0, 'H'],
            [5, 0, 0, 'C'], [5.7, 0.5, 0, 'H'], [5.7, -0.5, 0, 'H'], [5.7, 0, 0.5, 'H'],
        ]
        
        return np.array(benzene + side_chains)
    
    molecule = create_complex_molecule()
    perturbation_point = np.array([3, 0, 0])
    time_step = 5  # Show intermediate time step
    
    # Calculate quantum state
    positions = molecule[:, :3].astype(float)
    atom_types = molecule[:, 3]
    
    correlations = {}
    for i, (pos, atom_type) in enumerate(zip(positions, atom_types)):
        dist = np.linalg.norm(pos - perturbation_point)
        correlation = np.exp(-dist / 4.0) * np.cos(2 * np.pi * time_step / 6.0 - dist)
        
        if atom_type == 'C':
            base = 0.8
        elif atom_type == 'N':
            base = 0.9
        elif atom_type == 'O':
            base = 0.7
        else:
            base = 0.6
        
        correlations[i] = {
            'position': pos,
            'atom_type': atom_type,
            'correlation': base * correlation,
            'distance': dist
        }
    
    # Plot atoms with correlation-based properties
    colors = {'C': '#404040', 'N': '#3050F8', 'O': '#FF0D0D', 'H': '#FFFFFF'}
    
    for i, data in correlations.items():
        pos = data['position']
        atom_type = data['atom_type']
        correlation = data['correlation']
        
        size = 300 + 500 * abs(correlation)
        alpha = 0.7 + 0.3 * abs(correlation)
        
        ax.scatter(pos[0], pos[1], pos[2], 
                  c=colors[atom_type], s=size, alpha=alpha,
                  edgecolors='white', linewidth=2)
        
        # Add glow effect for high correlation
        if abs(correlation) > 0.6:
            ax.scatter(pos[0], pos[1], pos[2], 
                      c=colors[atom_type], s=size*1.5, alpha=0.3)
    
    # Create quantum wave effects
    for radius in np.linspace(0.5, 8, 15):
        amplitude = np.exp(-radius / 5.0) * np.cos(2 * np.pi * time_step / 4.0 - radius)
        
        if abs(amplitude) > 0.1:
            theta = np.linspace(0, 2 * np.pi, 40)
            x = perturbation_point[0] + radius * np.cos(theta)
            y = perturbation_point[1] + radius * np.sin(theta)
            z = perturbation_point[2] + amplitude * 0.8
            
            alpha = 0.4 * abs(amplitude)
            color = 'cyan' if amplitude > 0 else 'magenta'
            ax.plot(x, y, z, color=color, alpha=alpha, linewidth=4)
    
    # Create entanglement connections
    positions = [correlations[i]['position'] for i in correlations]
    
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            corr_i = correlations[i]['correlation']
            corr_j = correlations[j]['correlation']
            distance = np.linalg.norm(positions[i] - positions[j])
            
            strength = (corr_i + corr_j) / 2 * np.exp(-distance / 4.0)
            
            if strength > 0.2:
                start, end = positions[i], positions[j]
                alpha = 0.2 + 0.8 * strength
                linewidth = 1 + 5 * strength
                
                if strength > 0.7:
                    color = 'yellow'
                elif strength > 0.5:
                    color = 'orange'
                else:
                    color = 'red'
                
                ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
                       color=color, alpha=alpha, linewidth=linewidth)
    
    # Highlight perturbation point
    ax.scatter(perturbation_point[0], perturbation_point[1], perturbation_point[2],
              c='yellow', s=800, alpha=1.0, edgecolors='red', linewidth=5)
    
    # Add pulsing rings around perturbation
    for i in range(5):
        radius = 0.8 + i * 0.3
        alpha = 0.3 - i * 0.05
        ax.scatter(perturbation_point[0], perturbation_point[1], perturbation_point[2],
                  c='yellow', s=800*radius, alpha=alpha)
    
    # Set plot properties
    ax.set_title('Quantum Information Spreading in Complex Molecular System\n'
                'Single Electron Perturbation → Global Quantum Correlation', 
                fontsize=18, fontweight='bold', pad=25)
    
    ax.set_xlabel('X Coordinate (Å)', fontsize=15, fontweight='bold')
    ax.set_ylabel('Y Coordinate (Å)', fontsize=15, fontweight='bold')
    ax.set_zlabel('Z Coordinate (Å)', fontsize=15, fontweight='bold')
    
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_zlim(-4, 4)
    
    ax.view_init(elev=25, azim=45)
    ax.set_facecolor('black')
    
    # Add text annotations with better positioning
    ax.text2D(0.02, 0.95, 'Initial Perturbation\n(Electron Position Change)', 
              transform=ax.transAxes, fontsize=13, fontweight='bold',
              bbox=dict(boxstyle="round,pad=0.4", facecolor="yellow", alpha=0.8))
    
    ax.text2D(0.02, 0.05, 'Quantum Entanglement\n(Glowing Lines)', 
              transform=ax.transAxes, fontsize=13, fontweight='bold',
              bbox=dict(boxstyle="round,pad=0.4", facecolor="cyan", alpha=0.8))
    
    plt.tight_layout()
    
    # Save the visualization
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"quantum_molecule_detailed_{timestamp}.png"
    filepath = os.path.join(".", filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Detailed quantum molecule visualization saved: {filepath}")
    
    return fig

def main():
    """Main function to create quantum molecule visualizations"""
    print("Creating Quantum Information Spreading Visualizations...")
    print("=" * 60)
    
    # Create multi-panel visualization
    print("Generating multi-panel chain reaction visualization...")
    fig1 = create_quantum_molecule_visualization()
    
    # Create detailed single frame
    print("Generating detailed single-frame visualization...")
    fig2 = create_single_frame_visualization()
    
    print("\nQuantum molecule visualizations completed!")
    print("Check the Visualization/ folder for generated files")
    
    # Show the plots
    plt.show()
    
    return fig1, fig2

if __name__ == "__main__":
    fig1, fig2 = main()
