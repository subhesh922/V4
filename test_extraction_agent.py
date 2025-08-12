from agents.extraction_agent import ExtractionAgent
from pathlib import Path

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent  # go up to project root
    knowledge_path = base_dir / "server" / "sample_files" / "dfmea_knowledge_bank.csv"
    issues_path = base_dir / "server" / "sample_files" / "field_reported_issues.xlsx"

    agent = ExtractionAgent(
        knowledge_file_path=str(knowledge_path),
        issues_file_path=str(issues_path)
    )

    result = agent.run()
    print("[Test] Extracted Knowledge Entries:", len(result["knowledge_bank_data"]))
    print("[Test] Extracted Issue Entries:", len(result["field_issues_data"]))
    print("[Sample Row - Knowledge Bank]", result["knowledge_bank_data"][0])
    print("[Sample Row - Field Reported Issues]", result["field_issues_data"][0])
