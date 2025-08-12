from utils.excel_parser import parse_excel_or_csv
from pathlib import Path
import json

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent  # go up to project root
    file_path = base_dir / "server" / "sample_files" / "field_reported_issues.xlsx"

    data = parse_excel_or_csv(str(file_path))
    
    # ✅ Convert to valid JSON string
    json_output = json.dumps(data, indent=2)

    # ✅ Print nicely
    print(json_output)

