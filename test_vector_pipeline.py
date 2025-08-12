# server/test_vector_pipeline.py

from pathlib import Path
from agents.chunking_agent import ChunkingAgent
from agents.embedding_agent import EmbeddingAgent
from agents.vectorstore_agent import VectorStoreAgent
from agents.extraction_agent import ExtractionAgent

if __name__ == "__main__":
    print("[Pipeline] Starting full RAG pipeline...")

    # Load data via ExtractionAgent
    extractor = ExtractionAgent()
    kb_data = extractor.load_knowledge_bank()
    fi_data = extractor.load_field_issues()

    # Chunk
    chunker = ChunkingAgent()
    chunks = chunker.run(kb_data, fi_data)
    print(f"Chunked {len(chunks)} blocks.")

    # Embed locally with sentence-transformers
    embedder = EmbeddingAgent()
    embedded_chunks = embedder.embed_chunks(chunks, batch_size=64)
    print(f"✅ Embedded {len(embedded_chunks)} chunks.")

    if not embedded_chunks:
        print("❌ No chunks embedded due to rate limits or errors. Exiting pipeline.")
        exit(1)

    # Vector store
    vectorstore = VectorStoreAgent()
    vector_dim = len(embedded_chunks[0]["embedding"])
    vectorstore.create_collection(vector_dim)
    vectorstore.add_embeddings(embedded_chunks, batch_size=500)

    # Optional: semantic search
    results = vectorstore.search("cracked display", top_k=3)
    for r in results:
        print(f"\n🔍 Score: {r['score']:.4f}\nSOURCE: {r['metadata'].get('source')}\nTEXT: {r['text'][:300]}...")

    print("🎉 [Pipeline] Test run complete.")
