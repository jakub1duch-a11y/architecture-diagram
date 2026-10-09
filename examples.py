#!/usr/bin/env python3
"""
Examples demonstrating the MermaidDiagramAgent capabilities
"""

from mermaid_agent import MermaidDiagramAgent


def example_propose():
    """Example: Propose a new diagram"""
    print("\n" + "="*80)
    print("EXAMPLE 1: PROPOSE DIAGRAM")
    print("="*80 + "\n")
    
    agent = MermaidDiagramAgent()
    description = "A cloud infrastructure with VPC, subnets, EC2 instances, RDS database, and S3 storage"
    
    print(f"Proposing: {description}\n")
    result = agent.propose_diagram(description)
    print(result)


def example_generate():
    """Example: Generate diagram code"""
    print("\n" + "="*80)
    print("EXAMPLE 2: GENERATE DIAGRAM CODE")
    print("="*80 + "\n")
    
    agent = MermaidDiagramAgent()
    description = "A CI/CD pipeline with GitHub, Docker, Kubernetes, and monitoring"
    
    print(f"Generating: {description}\n")
    result = agent.generate_diagram(description)
    print("\nGenerated Mermaid Code:")
    print("```mermaid")
    print(result)
    print("```")


def example_edit():
    """Example: Edit existing diagram"""
    print("\n" + "="*80)
    print("EXAMPLE 3: EDIT EXISTING DIAGRAM")
    print("="*80 + "\n")
    
    agent = MermaidDiagramAgent()
    
    diagram = """graph TD
    A[User] -->|Login| B[Auth Service]
    B -->|Token| A
    A -->|Request| C[API Gateway]
    C -->|Route| D[Product Service]
    C -->|Route| E[Order Service]"""
    
    edit_request = "Add a Payment Service node and connect Order Service to it"
    
    print("Current diagram:")
    print(diagram)
    print(f"\nEdit request: {edit_request}\n")
    
    result = agent.edit_diagram(diagram, edit_request)
    print("Updated diagram:")
    print(result)


def example_review():
    """Example: Review diagram"""
    print("\n" + "="*80)
    print("EXAMPLE 4: REVIEW DIAGRAM")
    print("="*80 + "\n")
    
    agent = MermaidDiagramAgent()
    
    diagram = """graph LR
    A[Start] --> B[Process 1]
    B --> C[Process 2]
    C --> D[End]"""
    
    description = "A simple data processing pipeline"
    
    print("Reviewing diagram for:")
    print(description)
    print("\nDiagram code:")
    print(diagram)
    print()
    
    result = agent.review_diagram(diagram, description)
    print("Review result:")
    print(result)


def example_full_workflow():
    """Example: Full workflow"""
    print("\n" + "="*80)
    print("EXAMPLE 5: FULL WORKFLOW (PROPOSE → GENERATE → REVIEW)")
    print("="*80 + "\n")
    
    agent = MermaidDiagramAgent()
    description = """
    A distributed system for real-time analytics with:
    - Data collectors
    - Message broker
    - Stream processing engine
    - Time-series database
    - Visualization dashboard
    """
    
    result = agent.full_workflow(description)
    
    print("\n📋 PROPOSAL:")
    print(result['proposal'])
    print("\n🔧 GENERATED CODE:")
    print(result['diagram_code'])
    print("\n👁️ REVIEW:")
    print(result['review'])


if __name__ == "__main__":
    # Run all examples
    # Uncomment the ones you want to run:
    
    # example_propose()
    # example_generate()
    # example_edit()
    # example_review()
    example_full_workflow()
