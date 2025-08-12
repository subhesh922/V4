from agents.chunking_agent import ChunkingAgent
from utils.excel_parser import parse_excel_or_csv
from pathlib import Path
import json

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    kb_path = base_dir / "sample_files" / "dfmea_knowledge_bank.csv"
    fi_path = base_dir / "sample_files" / "field_reported_issues.xlsx"

    kb_data = parse_excel_or_csv(str(kb_path))
    fi_data = parse_excel_or_csv(str(fi_path))

    agent = ChunkingAgent(chunk_size=50)
    chunks = agent.run(kb_data, fi_data)

    print(f"Generated {len(chunks)} total chunks.")
    print(json.dumps(chunks[0:3], indent=2))  # Show a sample chunk
