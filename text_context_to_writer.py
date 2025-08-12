# server/test_context_to_writer.py
from server.agents.context_agent import ContextAgent
from server.agents.writer_agent import WriterAgent

if __name__ == "__main__":
    print("\n🔁 [Integration Test] Running ContextAgent → WriterAgent pipeline...")

    collection_name = "dfmea_collection_449401a1"
    context_agent = ContextAgent(collection_name=collection_name, batch_size=1)

    dfmea_json = context_agent.run(
        query="Generate DFMEA entries for recent field failures from the field_issues data",
        top_k=300  # Increase to fetch more chunks = more DFMEA entries
    )

    if not dfmea_json:
        print("❌ No DFMEA entries generated.")
        exit(1)

    writer = WriterAgent(output_path="output/dfmea_output.xlsx")
    excel_path = writer.run(dfmea_json)

    print(f"\n✅ [Success] DFMEA Excel file created: {excel_path}")
