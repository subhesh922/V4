from pipeline.dfmea_pipeline import DFMEAPipeline
from pathlib import Path
import json

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    kb_path = base_dir / "server" / "sample_files" / "dfmea_knowledge_bank.csv"
    issues_path = base_dir / "server" / "sample_files" / "field_reported_issues.xlsx"

    pipeline = DFMEAPipeline(
        knowledge_path=str(kb_path),
        issues_path=str(issues_path)
    )

    result = pipeline.run()
    print(json.dumps(result, indent=2))
