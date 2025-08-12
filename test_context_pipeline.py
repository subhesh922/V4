# test_context_pipeline.py

from pathlib import Path
from utils.excel_parser import parse_excel_or_csv
from agents.chunking_agent import ChunkingAgent
from agents.embedding_agent import EmbeddingAgent
from agents.vectorstore_agent import VectorStoreAgent
from agents.context_agent import ContextAgent

if __name__ == "__main__":
    print("\n🔁 [ContextPipeline] Starting full DFMEA RAG flow...")

    # 1. Load input files
    base_dir = Path(__file__).resolve().parent
    kb_path = base_dir / "sample_files" / "dfmea_knowledge_bank.csv"
    fi_path = base_dir / "sample_files" / "field_reported_issues.xlsx"

    kb_data = parse_excel_or_csv(str(kb_path))
    fi_data = parse_excel_or_csv(str(fi_path))

    # 2. Chunking
    chunker = ChunkingAgent(chunk_size=50, overlap=5)
    chunks = chunker.run(kb_data, fi_data)
    print(f"✅ Chunked {len(chunks)} blocks.")

    # 3. Embedding
    embedder = EmbeddingAgent()
    embedded_chunks = embedder.embed_chunks(chunks[:50])  # To avoid rate limit overload
    print(f"✅ Embedded {len(embedded_chunks)} chunks.")

    # 4. Store in Qdrant
    vectorstore = VectorStoreAgent()
    dim = len(embedded_chunks[0]["embedding"])
    vectorstore.create_collection(vector_dim=dim)
    vectorstore.add_embeddings(embedded_chunks)

    # 5. RAG + Reasoning
    context_agent = ContextAgent(collection_name=vectorstore.collection_name, batch_size=2)
    output = context_agent.run(
        query="Generate DFMEA entries for recent field failures",
        top_k=5
    )

    # 6. Output
    print("\n📄 Final DFMEA JSON Output:")
    for idx, entry in enumerate(output):
        print(f"\n🔹 Entry {idx+1}:\n{entry}")

    # Optional cleanup
    cleanup = False
    if cleanup:
        vectorstore.delete_collection()
