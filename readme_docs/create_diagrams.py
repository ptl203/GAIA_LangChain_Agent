#!/usr/bin/env python3
"""
Script to generate architectural diagrams for the GAIA LangChain Agent README
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Set up the style for professional diagrams
plt.style.use('default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

def create_agent_architecture_diagram():
    """Create the LangGraph agent architecture diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(5, 7.5, 'GAIA LangChain Agent Architecture', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Input layer
    input_box = FancyBboxPatch((0.5, 6), 2, 0.8, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.5, 6.4, 'User Question\n(GAIA Benchmark)', ha='center', va='center', fontweight='bold')
    
    # State Management
    state_box = FancyBboxPatch((4, 6), 2, 0.8, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#F3E5F5', edgecolor='#7B1FA2', linewidth=2)
    ax.add_patch(state_box)
    ax.text(5, 6.4, 'AgentState\n(Messages)', ha='center', va='center', fontweight='bold')
    
    # Assistant Node (LLM)
    llm_box = FancyBboxPatch((2, 4.5), 3, 1, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=2)
    ax.add_patch(llm_box)
    ax.text(3.5, 5, 'Assistant Node\nGoogle Gemini 2.5 Pro', ha='center', va='center', fontweight='bold')
    
    # Tools Node
    tools_box = FancyBboxPatch((6.5, 4.5), 2.5, 1, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#E8F5E8', edgecolor='#388E3C', linewidth=2)
    ax.add_patch(tools_box)
    ax.text(7.75, 5, 'Tools Node\n6 Specialized Tools', ha='center', va='center', fontweight='bold')
    
    # Individual Tools
    tools = [
        ('Google Search', 1, 2.5),
        ('Wikipedia', 2.5, 2.5),
        ('YouTube Transcript', 4, 2.5),
        ('Python Execution', 5.5, 2.5),
        ('Excel Reader', 7, 2.5),
        ('File Contents', 8.5, 2.5)
    ]
    
    for tool_name, x, y in tools:
        tool_box = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor='#E1F5FE', edgecolor='#0277BD', linewidth=1)
        ax.add_patch(tool_box)
        ax.text(x, y, tool_name, ha='center', va='center', fontsize=8)
    
    # Output
    output_box = FancyBboxPatch((3.5, 0.5), 3, 0.8, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#E8F5E8', edgecolor='#2E7D32', linewidth=2)
    ax.add_patch(output_box)
    ax.text(5, 0.9, 'Final Answer\n(Submitted to GAIA API)', ha='center', va='center', fontweight='bold')
    
    # Arrows
    # Input to State
    ax.arrow(2.5, 6.4, 1.3, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # State to Assistant
    ax.arrow(5, 5.8, 0, -0.2, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.arrow(4.8, 5.5, -1.1, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Assistant to Tools (conditional)
    con = ConnectionPatch((5, 5), (6.5, 5), "data", "data",
                         arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=20, fc="red", ec="red")
    ax.add_artist(con)
    ax.text(5.75, 5.3, 'tools_condition', ha='center', fontsize=8, color='red')
    
    # Tools back to Assistant
    con = ConnectionPatch((6.5, 4.7), (5, 4.7), "data", "data",
                         arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=20, fc="green", ec="green")
    ax.add_artist(con)
    
    # Tools to individual tools
    for _, x, y in tools:
        ax.arrow(7.5, 4.5, x-7.5, y-4.5+0.3, head_width=0.05, head_length=0.05, fc='gray', ec='gray', alpha=0.7)
    
    # Assistant to Output
    ax.arrow(3.5, 4.5, 0, -3.2, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Add START indicator
    start_circle = plt.Circle((1.5, 5), 0.3, color='#4CAF50', alpha=0.8)
    ax.add_patch(start_circle)
    ax.text(1.5, 5, 'START', ha='center', va='center', fontweight='bold', fontsize=8, color='white')
    
    plt.tight_layout()
    plt.savefig('/home/paul/git/GAIA_LangChain_Agent/readme_docs/agent_architecture.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()

def create_tools_ecosystem_diagram():
    """Create the tools ecosystem diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    # Title
    ax.text(5, 8.5, 'GAIA Agent Tools Ecosystem', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Central Agent
    agent_circle = plt.Circle((5, 5), 1, color='#FF9800', alpha=0.8)
    ax.add_patch(agent_circle)
    ax.text(5, 5, 'GAIA\nAgent', ha='center', va='center', fontweight='bold', fontsize=12, color='white')
    
    # Tool definitions with positions
    tools_info = [
        ('Google Search\nAPI', 2, 7.5, '#4285F4', 'Real-time web search\nfor current information'),
        ('Wikipedia\nLookup', 1, 5.5, '#000000', 'Encyclopedic knowledge\nretrieval'),
        ('YouTube\nTranscript', 2, 3, '#FF0000', 'Video content analysis\nand transcription'),
        ('Python Code\nExecution', 5, 2, '#306998', 'Dynamic code execution\nand analysis'),
        ('Excel File\nReader', 8, 3, '#217346', 'Spreadsheet data\nprocessing'),
        ('File Contents\nReader', 8.5, 5.5, '#6C757D', 'Text file content\nextraction'),
    ]
    
    for tool_name, x, y, color, description in tools_info:
        # Tool circle
        tool_circle = plt.Circle((x, y), 0.7, color=color, alpha=0.7)
        ax.add_patch(tool_circle)
        ax.text(x, y, tool_name, ha='center', va='center', fontweight='bold', fontsize=9, color='white')
        
        # Connection to agent
        dx = 5 - x
        dy = 5 - y
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length * 0.7  # Start from circle edge
        dy_norm = dy / length * 0.7
        
        ax.arrow(x + dx_norm, y + dy_norm, 
                dx - 2*dx_norm, dy - 2*dy_norm,
                head_width=0.1, head_length=0.1, fc='gray', ec='gray', alpha=0.6)
        
        # Description boxes
        if x < 5:  # Left side tools
            desc_x = x - 1.5
        else:  # Right side tools
            desc_x = x + 1.5
            
        desc_box = FancyBboxPatch((desc_x-0.8, y-0.3), 1.6, 0.6, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor='white', edgecolor=color, linewidth=1, alpha=0.9)
        ax.add_patch(desc_box)
        ax.text(desc_x, y, description, ha='center', va='center', fontsize=7, color='black')
    
    # Add capability labels
    capabilities = [
        ('Web Knowledge', 1.5, 6.5, '#E3F2FD'),
        ('Media Processing', 2, 2, '#FFF3E0'),
        ('Code Analysis', 5, 1, '#E8F5E8'),
        ('Data Processing', 8.2, 4, '#F3E5F5')
    ]
    
    for cap_name, x, y, color in capabilities:
        cap_box = FancyBboxPatch((x-0.6, y-0.2), 1.2, 0.4, 
                                boxstyle="round,pad=0.05", 
                                facecolor=color, edgecolor='gray', linewidth=1)
        ax.add_patch(cap_box)
        ax.text(x, y, cap_name, ha='center', va='center', fontsize=8, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/paul/git/GAIA_LangChain_Agent/readme_docs/tools_ecosystem.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()

def create_workflow_diagram():
    """Create the agent workflow flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(4, 11.5, 'GAIA Agent Workflow', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Workflow steps
    steps = [
        ('Receive GAIA\nQuestion', 4, 10.5, '#E3F2FD', '#1976D2'),
        ('Initialize\nAgentState', 4, 9.5, '#F3E5F5', '#7B1FA2'),
        ('LLM Analysis\n& Tool Selection', 4, 8.5, '#FFF3E0', '#F57C00'),
        ('Execute\nSelected Tools', 4, 7.5, '#E8F5E8', '#388E3C'),
        ('Process Tool\nResults', 4, 6.5, '#E1F5FE', '#0277BD'),
        ('Generate\nFinal Answer', 4, 5.5, '#FFF8E1', '#FBC02D'),
        ('Submit to\nGAIA API', 4, 4.5, '#E8F5E8', '#2E7D32'),
        ('Evaluate\nPerformance', 4, 3.5, '#FCE4EC', '#C2185B')
    ]
    
    for i, (step_name, x, y, bg_color, border_color) in enumerate(steps):
        # Create step box
        step_box = FancyBboxPatch((x-1, y-0.3), 2, 0.6, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=bg_color, edgecolor=border_color, linewidth=2)
        ax.add_patch(step_box)
        ax.text(x, y, step_name, ha='center', va='center', fontweight='bold')
        
        # Add arrow to next step (except for last step)
        if i < len(steps) - 1:
            ax.arrow(x, y-0.4, 0, -0.4, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Add decision diamond for tool execution
    decision_points = [
        (1.5, 8.5, 'Need\nTools?'),
        (6.5, 8.5, 'Tools\nComplete?'),
        (1.5, 6.5, 'Answer\nComplete?')
    ]
    
    for x, y, text in decision_points:
        diamond = patches.RegularPolygon((x, y), 4, radius=0.5, 
                                       orientation=np.pi/4, 
                                       facecolor='#FFECB3', edgecolor='#FF8F00', linewidth=2)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Add decision flow arrows
    # From LLM to decision
    ax.arrow(3, 8.5, -1, 0, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
    ax.text(2.2, 8.7, 'Yes', fontsize=8, color='blue')
    
    # From decision back to LLM (if tools needed)
    ax.arrow(1.5, 8, 0, 0.3, head_width=0.1, head_length=0.1, fc='red', ec='red')
    ax.arrow(1.5, 8.8, 2.3, 0, head_width=0.1, head_length=0.1, fc='red', ec='red')
    ax.text(0.8, 8.2, 'No', fontsize=8, color='red')
    
    plt.tight_layout()
    plt.savefig('/home/paul/git/GAIA_LangChain_Agent/readme_docs/agent_workflow.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    print("Creating agent architecture diagram...")
    create_agent_architecture_diagram()
    print("✅ Agent architecture diagram saved")
    
    print("Creating tools ecosystem diagram...")  
    create_tools_ecosystem_diagram()
    print("✅ Tools ecosystem diagram saved")
    
    print("Creating workflow diagram...")
    create_workflow_diagram()
    print("✅ Workflow diagram saved")
    
    print("\n🎉 All diagrams created successfully!")
    print("Files saved in readme_docs/ directory:")
    print("- agent_architecture.png")
    print("- tools_ecosystem.png") 
    print("- agent_workflow.png")