from agents.chunking_agent import ChunkingAgent
from agents.embedding_agent import EmbeddingAgent
from utils.excel_parser import parse_excel_or_csv
from pathlib import Path

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    kb_path = base_dir / "sample_files" / "dfmea_knowledge_bank.csv"
    fi_path = base_dir / "sample_files" / "field_reported_issues.xlsx"

    kb_data = parse_excel_or_csv(str(kb_path))
    fi_data = parse_excel_or_csv(str(fi_path))

    chunker = ChunkingAgent(chunk_size=50, overlap=5)
    chunks = chunker.run(kb_data, fi_data)

    embedder = EmbeddingAgent()
    embedded_chunks = embedder.embed_chunks(chunks[:10])  # Test with 5 chunks first

    print(f"\nEmbedded {len(embedded_chunks)} chunks.")
