from agents.context_agent import ContextAgent
from agents.extraction_agent import ExtractionAgent
from pathlib import Path
import json

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    kb_path = base_dir / "server" / "sample_files" / "dfmea_knowledge_bank.csv"
    issues_path = base_dir / "server" / "sample_files" / "field_reported_issues.xlsx"

    extracted = ExtractionAgent(str(kb_path), str(issues_path)).run()

    agent = ContextAgent(
        knowledge_bank_data=extracted["knowledge_bank_data"][:10],
        field_issues_data=extracted["field_issues_data"][:10]
    )

    summary = agent.run()
    print(summary)
