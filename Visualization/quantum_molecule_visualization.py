#!/usr/bin/env python3
"""
Quantum Information Spreading in Molecules
Scientific Visualization for Research Presentation

This script creates a detailed 3D visualization showing how quantum information
spreads through a molecular structure following a small perturbation.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from datetime import datetime
import os

# Set style for scientific presentation
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

class QuantumMoleculeVisualizer:
    def __init__(self):
        self.fig = None
        self.ax = None
        self.molecule_data = None
        self.perturbation_point = None
        self.time_steps = 20
        self.current_time = 0
        
    def create_molecular_structure(self):
        """Create a realistic molecular structure (e.g., benzene ring with side chains)"""
        # Define atomic positions for a complex organic molecule
        # Benzene ring (6 carbon atoms)
        benzene_ring = []
        for i in range(6):
            angle = i * np.pi / 3
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            z = 0
            benzene_ring.append([x, y, z, 'C'])  # Carbon atoms
        
        # Add side chains and functional groups
        side_chains = [
            # Hydroxyl group
            [4, 0, 0, 'O'],
            [4.7, 0, 0, 'H'],
            # Methyl group
            [-4, 0, 0, 'C'],
            [-4.7, 0.5, 0, 'H'],
            [-4.7, -0.5, 0, 'H'],
            [-4.7, 0, 0.5, 'H'],
            # Nitrogen group
            [0, 4, 0, 'N'],
            [0, 4.7, 0, 'H'],
            [0.5, 4.3, 0, 'H'],
            # Additional complexity
            [2, 2, 1.5, 'C'],
            [2.7, 2.7, 1.5, 'H'],
            [1.3, 2.7, 1.5, 'H'],
            [2.7, 1.3, 1.5, 'H'],
            [-2, -2, -1.5, 'C'],
            [-2.7, -2.7, -1.5, 'H'],
            [-1.3, -2.7, -1.5, 'H'],
            [-2.7, -1.3, -1.5, 'H'],
        ]
        
        # Combine all atoms
        self.molecule_data = np.array(benzene_ring + side_chains)
        
        # Define perturbation point (electron position change)
        self.perturbation_point = np.array([2, 0, 0])  # On the benzene ring
        
        return self.molecule_data
    
    def calculate_quantum_correlations(self, time_step):
        """Calculate quantum correlations and information spreading"""
        correlations = {}
        positions = self.molecule_data[:, :3].astype(float)
        atom_types = self.molecule_data[:, 3]
        
        # Calculate distance from perturbation point
        distances = np.linalg.norm(positions - self.perturbation_point, axis=1)
        
        # Quantum information spreading follows exponential decay with oscillations
        # This simulates the OTOC behavior in molecular systems
        for i, (pos, atom_type, dist) in enumerate(zip(positions, atom_types, distances)):
            # Time-dependent correlation strength
            correlation_strength = np.exp(-dist / 3.0) * np.cos(2 * np.pi * time_step / 5.0 - dist)
            
            # Add quantum noise and entanglement effects
            entanglement_factor = 1.0 + 0.3 * np.sin(time_step * 0.5 + i * 0.2)
            
            # Different atom types have different correlation behaviors
            if atom_type == 'C':
                base_correlation = 0.8
            elif atom_type == 'N':
                base_correlation = 0.9
            elif atom_type == 'O':
                base_correlation = 0.7
            else:  # H
                base_correlation = 0.6
            
            correlations[i] = {
                'position': pos,
                'atom_type': atom_type,
                'correlation': base_correlation * correlation_strength * entanglement_factor,
                'distance': dist,
                'phase': time_step * 0.3 + i * 0.1
            }
        
        return correlations
    
    def create_quantum_wave_visualization(self, correlations, time_step):
        """Create glowing wave effects representing quantum information spread"""
        wave_effects = []
        
        # Create concentric wave rings from perturbation point
        center = self.perturbation_point
        max_radius = 8
        
        for radius in np.linspace(0.5, max_radius, 15):
            # Wave amplitude decreases with distance and time
            amplitude = np.exp(-radius / 4.0) * np.cos(2 * np.pi * time_step / 3.0 - radius)
            
            if abs(amplitude) > 0.1:  # Only show significant waves
                # Create wave ring
                theta = np.linspace(0, 2 * np.pi, 50)
                x_wave = center[0] + radius * np.cos(theta)
                y_wave = center[1] + radius * np.sin(theta)
                z_wave = center[2] + amplitude * 0.5
                
                wave_effects.append({
                    'x': x_wave,
                    'y': y_wave,
                    'z': z_wave,
                    'amplitude': amplitude,
                    'radius': radius
                })
        
        return wave_effects
    
    def create_entanglement_connections(self, correlations):
        """Create lines showing quantum entanglement between atoms"""
        connections = []
        positions = [correlations[i]['position'] for i in correlations]
        
        # Connect atoms with strong correlations
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                corr_i = correlations[i]['correlation']
                corr_j = correlations[j]['correlation']
                distance = np.linalg.norm(positions[i] - positions[j])
                
                # Connection strength based on correlation and distance
                connection_strength = (corr_i + corr_j) / 2 * np.exp(-distance / 3.0)
                
                if connection_strength > 0.3:  # Only show strong connections
                    connections.append({
                        'start': positions[i],
                        'end': positions[j],
                        'strength': connection_strength,
                        'phase': correlations[i]['phase'] + correlations[j]['phase']
                    })
        
        return connections
    
    def setup_plot(self):
        """Initialize the 3D plot with scientific styling"""
        self.fig = plt.figure(figsize=(16, 12))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Set up the plot appearance
        self.ax.set_xlabel('X Coordinate (Å)', fontsize=12, fontweight='bold')
        self.ax.set_ylabel('Y Coordinate (Å)', fontsize=12, fontweight='bold')
        self.ax.set_zlabel('Z Coordinate (Å)', fontsize=12, fontweight='bold')
        
        # Set equal aspect ratio
        self.ax.set_box_aspect([1, 1, 1])
        
        # Set viewing angle for best scientific presentation
        self.ax.view_init(elev=20, azim=45)
        
        # Set background
        self.ax.set_facecolor('black')
        self.fig.patch.set_facecolor('white')
        
        return self.fig, self.ax
    
    def plot_molecule_atoms(self, correlations):
        """Plot atoms as spheres with size and color based on correlation"""
        for i, data in correlations.items():
            pos = data['position']
            atom_type = data['atom_type']
            correlation = data['correlation']
            phase = data['phase']
            
            # Atom colors based on type
            color_map = {
                'C': '#404040',  # Dark gray for carbon
                'N': '#3050F8',  # Blue for nitrogen
                'O': '#FF0D0D',  # Red for oxygen
                'H': '#FFFFFF'   # White for hydrogen
            }
            
            # Atom sizes based on correlation strength
            size = 200 + 300 * abs(correlation)
            
            # Glowing effect based on correlation
            alpha = 0.7 + 0.3 * abs(correlation)
            
            # Add phase-dependent glow
            glow_intensity = 0.5 + 0.5 * np.sin(phase)
            
            self.ax.scatter(pos[0], pos[1], pos[2], 
                          c=color_map[atom_type], s=size, alpha=alpha,
                          edgecolors='white', linewidth=1)
            
            # Add glow effect
            if abs(correlation) > 0.5:
                self.ax.scatter(pos[0], pos[1], pos[2], 
                              c=color_map[atom_type], s=size*2, alpha=0.2*glow_intensity)
    
    def plot_quantum_waves(self, wave_effects):
        """Plot quantum information waves as glowing rings"""
        for wave in wave_effects:
            alpha = 0.3 * abs(wave['amplitude'])
            color_intensity = abs(wave['amplitude'])
            
            # Color based on wave amplitude
            if wave['amplitude'] > 0:
                color = 'cyan'
            else:
                color = 'magenta'
            
            self.ax.plot(wave['x'], wave['y'], wave['z'], 
                        color=color, alpha=alpha, linewidth=2)
    
    def plot_entanglement_lines(self, connections):
        """Plot quantum entanglement as glowing lines"""
        for conn in connections:
            start = conn['start']
            end = conn['end']
            strength = conn['strength']
            phase = conn['phase']
            
            # Line color and intensity based on strength
            alpha = 0.4 + 0.6 * strength
            linewidth = 1 + 3 * strength
            
            # Pulsing effect
            pulse = 0.5 + 0.5 * np.sin(phase)
            alpha *= pulse
            
            # Color gradient based on strength
            if strength > 0.7:
                color = 'yellow'
            elif strength > 0.5:
                color = 'orange'
            else:
                color = 'red'
            
            self.ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
                        color=color, alpha=alpha, linewidth=linewidth)
    
    def add_perturbation_highlight(self):
        """Highlight the initial perturbation point"""
        # Add a bright marker at the perturbation point
        self.ax.scatter(self.perturbation_point[0], self.perturbation_point[1], 
                       self.perturbation_point[2], c='yellow', s=500, alpha=0.8,
                       edgecolors='red', linewidth=3, label='Initial Perturbation')
        
        # Add pulsing effect
        for i in range(3):
            radius = 0.5 + i * 0.3
            alpha = 0.3 - i * 0.1
            self.ax.scatter(self.perturbation_point[0], self.perturbation_point[1], 
                           self.perturbation_point[2], c='yellow', s=500*radius, 
                           alpha=alpha)
    
    def add_timeline_effect(self, time_step):
        """Add timeline visualization showing propagation"""
        # Create timeline bar
        timeline_x = np.linspace(-6, 6, self.time_steps)
        timeline_y = np.full_like(timeline_x, -5)
        timeline_z = np.full_like(timeline_x, -5)
        
        # Highlight current time step
        current_x = timeline_x[time_step]
        self.ax.scatter(current_x, -5, -5, c='white', s=200, alpha=0.9)
        
        # Add timeline labels
        self.ax.text(0, -6, -5, 'Time Progression', ha='center', va='center',
                    fontsize=10, color='white', fontweight='bold')
    
    def create_animation_frame(self, time_step):
        """Create a single frame of the animation"""
        self.ax.clear()
        
        # Recalculate correlations for this time step
        correlations = self.calculate_quantum_correlations(time_step)
        wave_effects = self.create_quantum_wave_visualization(correlations, time_step)
        connections = self.create_entanglement_connections(correlations)
        
        # Plot all elements
        self.plot_molecule_atoms(correlations)
        self.plot_quantum_waves(wave_effects)
        self.plot_entanglement_lines(connections)
        self.add_perturbation_highlight()
        self.add_timeline_effect(time_step)
        
        # Update title with time information
        self.ax.set_title(f'Quantum Information Spreading in Molecular System\n'
                         f'Time Step: {time_step}/{self.time_steps-1} | '
                         f'Correlation Strength: {np.mean([c["correlation"] for c in correlations.values()]):.3f}',
                         fontsize=14, fontweight='bold', pad=20)
        
        # Set axis limits
        self.ax.set_xlim(-6, 6)
        self.ax.set_ylim(-6, 6)
        self.ax.set_zlim(-3, 3)
        
        # Add legend
        self.ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0))
    
    def create_static_visualization(self):
        """Create a static multi-panel visualization"""
        self.create_molecular_structure()
        self.setup_plot()
        
        # Create multiple time steps
        time_steps_to_show = [0, 3, 6, 9, 12, 15]
        
        fig, axes = plt.subplots(2, 3, figsize=(20, 12), subplot_kw={'projection': '3d'})
        axes = axes.flatten()
        
        for idx, time_step in enumerate(time_steps_to_show):
            ax = axes[idx]
            
            # Calculate correlations for this time step
            correlations = self.calculate_quantum_correlations(time_step)
            wave_effects = self.create_quantum_wave_visualization(correlations, time_step)
            connections = self.create_entanglement_connections(correlations)
            
            # Plot atoms
            for i, data in correlations.items():
                pos = data['position']
                atom_type = data['atom_type']
                correlation = data['correlation']
                
                color_map = {
                    'C': '#404040', 'N': '#3050F8', 'O': '#FF0D0D', 'H': '#FFFFFF'
                }
                
                size = 200 + 300 * abs(correlation)
                alpha = 0.7 + 0.3 * abs(correlation)
                
                ax.scatter(pos[0], pos[1], pos[2], 
                          c=color_map[atom_type], s=size, alpha=alpha,
                          edgecolors='white', linewidth=1)
            
            # Plot waves
            for wave in wave_effects:
                alpha = 0.3 * abs(wave['amplitude'])
                color = 'cyan' if wave['amplitude'] > 0 else 'magenta'
                ax.plot(wave['x'], wave['y'], wave['z'], 
                       color=color, alpha=alpha, linewidth=2)
            
            # Plot connections
            for conn in connections:
                start, end = conn['start'], conn['end']
                strength = conn['strength']
                alpha = 0.4 + 0.6 * strength
                linewidth = 1 + 3 * strength
                color = 'yellow' if strength > 0.7 else 'orange' if strength > 0.5 else 'red'
                
                ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
                       color=color, alpha=alpha, linewidth=linewidth)
            
            # Highlight perturbation
            ax.scatter(self.perturbation_point[0], self.perturbation_point[1], 
                      self.perturbation_point[2], c='yellow', s=500, alpha=0.8,
                      edgecolors='red', linewidth=3)
            
            ax.set_title(f'Time Step {time_step}', fontsize=12, fontweight='bold')
            ax.set_xlim(-6, 6)
            ax.set_ylim(-6, 6)
            ax.set_zlim(-3, 3)
            ax.set_xlabel('X (Å)')
            ax.set_ylabel('Y (Å)')
            ax.set_zlabel('Z (Å)')
        
        plt.suptitle('Quantum Information Spreading: Chain Reaction Visualization', 
                    fontsize=16, fontweight='bold', y=0.95)
        plt.tight_layout()
        
        # Save the visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quantum_molecule_chain_reaction_{timestamp}.png"
        filepath = os.path.join("Visualization", filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"💾 Quantum molecule visualization saved: {filepath}")
        
        return fig
    
    def create_animated_visualization(self):
        """Create an animated visualization"""
        self.create_molecular_structure()
        self.setup_plot()
        
        def animate(frame):
            self.create_animation_frame(frame)
            return []
        
        # Create animation
        anim = FuncAnimation(self.fig, animate, frames=self.time_steps, 
                           interval=500, blit=False, repeat=True)
        
        # Save animation
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quantum_molecule_animation_{timestamp}.gif"
        filepath = os.path.join("Visualization", filename)
        anim.save(filepath, writer='pillow', fps=2)
        print(f"🎬 Quantum molecule animation saved: {filepath}")
        
        return anim

def main():
    """Main function to create the quantum molecule visualization"""
    print("🧬 Creating Quantum Information Spreading Visualization...")
    print("=" * 60)
    
    # Create visualizer
    visualizer = QuantumMoleculeVisualizer()
    
    # Create static multi-panel visualization
    print("📊 Generating static visualization...")
    static_fig = visualizer.create_static_visualization()
    
    # Create animated visualization
    print("🎬 Generating animated visualization...")
    anim = visualizer.create_animated_visualization()
    
    print("\n✅ Quantum molecule visualizations completed!")
    print("📁 Check the Visualization/ folder for generated files")
    
    # Show the static plot
    plt.show()
    
    return visualizer

if __name__ == "__main__":
    visualizer = main()
