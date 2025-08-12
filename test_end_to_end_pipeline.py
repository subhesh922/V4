# server/test_end_to_end_pipeline.py

from server.pipeline.end_to_end_pipeline import DFMEAEndToEndPipeline

if __name__ == "__main__":
    print("[Test] Running DFMEA End-to-End Pipeline...")

    kb_path = "server/sample_files/dfmea_knowledge_bank_3.csv"
    fi_path = "server/sample_files/field_reported_issues_3.xlsx"
    query = "Generate DFMEA entries for recent field failures"

    pipeline = DFMEAEndToEndPipeline(kb_path=kb_path, fi_path=fi_path, query=query, top_k=100)
    pipeline.run()

    print("[Test] End-to-End DFMEA pipeline test complete.")
