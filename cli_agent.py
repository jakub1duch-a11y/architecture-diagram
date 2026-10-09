#!/usr/bin/env python3
"""
Command-line interface for the Mermaid Diagram AI Agent
"""

import argparse
import sys
from pathlib import Path
from mermaid_agent import MermaidDiagramAgent


def save_diagram(code: str, filename: str = None) -> str:
    """Save diagram code to a file"""
    if filename is None:
        filename = "diagram.md"
    
    filepath = Path(filename)
    with open(filepath, "w") as f:
        f.write("```mermaid\n")
        f.write(code)
        f.write("\n```")
    
    return str(filepath.absolute())


def main():
    parser = argparse.ArgumentParser(
        description="AI Agent for generating and managing Mermaid diagrams"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Propose command
    propose_parser = subparsers.add_parser("propose", help="Propose a diagram structure")
    propose_parser.add_argument("description", help="Description of the diagram to propose")
    propose_parser.add_argument("-o", "--output", help="Save output to file")
    
    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate Mermaid diagram code")
    generate_parser.add_argument("description", help="Description of the diagram to generate")
    generate_parser.add_argument("-o", "--output", help="Save diagram to file")
    
    # Edit command
    edit_parser = subparsers.add_parser("edit", help="Edit an existing diagram")
    edit_parser.add_argument("file", help="Path to diagram file or code")
    edit_parser.add_argument("request", help="Edit request description")
    edit_parser.add_argument("-o", "--output", help="Save updated diagram to file")
    
    # Review command
    review_parser = subparsers.add_parser("review", help="Review and improve a diagram")
    review_parser.add_argument("file", help="Path to diagram file")
    review_parser.add_argument("description", help="Context description for the diagram")
    review_parser.add_argument("-o", "--output", help="Save review to file")
    
    # Workflow command
    workflow_parser = subparsers.add_parser("workflow", help="Execute full workflow (propose -> generate -> review)")
    workflow_parser.add_argument("description", help="Description of the diagram")
    workflow_parser.add_argument("-o", "--output", help="Save results to file")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    agent = MermaidDiagramAgent()
    
    try:
        if args.command == "propose":
            print("📋 Proposing diagram structure...")
            result = agent.propose_diagram(args.description)
            print("\n" + result)
            
            if args.output:
                with open(args.output, "w") as f:
                    f.write(result)
                print(f"\n✅ Saved to {args.output}")
        
        elif args.command == "generate":
            print("🔧 Generating Mermaid diagram...")
            result = agent.generate_diagram(args.description)
            print("\n```mermaid")
            print(result)
            print("```")
            
            if args.output:
                save_diagram(result, args.output)
                print(f"\n✅ Saved to {args.output}")
        
        elif args.command == "edit":
            print("✏️ Editing diagram...")
            
            # Read diagram from file
            if Path(args.file).exists():
                with open(args.file, "r") as f:
                    diagram_code = f.read()
                    # Extract code from markdown if needed
                    if "```mermaid" in diagram_code:
                        diagram_code = diagram_code.split("```mermaid")[1].split("```")[0].strip()
            else:
                diagram_code = args.file
            
            result = agent.edit_diagram(diagram_code, args.request)
            print("\n```mermaid")
            print(result)
            print("```")
            
            if args.output:
                save_diagram(result, args.output)
                print(f"\n✅ Saved to {args.output}")
        
        elif args.command == "review":
            print("👁️ Reviewing diagram...")
            
            # Read diagram from file
            with open(args.file, "r") as f:
                diagram_code = f.read()
                # Extract code from markdown if needed
                if "```mermaid" in diagram_code:
                    diagram_code = diagram_code.split("```mermaid")[1].split("```")[0].strip()
            
            result = agent.review_diagram(diagram_code, args.description)
            print("\n" + result)
            
            if args.output:
                with open(args.output, "w") as f:
                    f.write(result)
                print(f"\n✅ Saved to {args.output}")
        
        elif args.command == "workflow":
            print("🔄 Executing full workflow (propose -> generate -> review)...")
            result = agent.full_workflow(args.description)
            
            output = f"""# Generated Architecture Diagram

## Description
{result['description']}

## Proposal
{result['proposal']}

## Generated Mermaid Diagram
\`\`\`mermaid
{result['diagram_code']}
\`\`\`

## Review & Improvements
{result['review']}
"""
            
            print(output)
            
            if args.output:
                with open(args.output, "w") as f:
                    f.write(output)
                print(f"\n✅ Saved to {args.output}")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
