from server.pipeline.dfmea_pipeline import DFMEAPipeline

if __name__ == "__main__":
    print("[Test] Running DFMEA Pipeline...")

    collection_name = "dfmea_collection_b49e36ed"

    pipeline = DFMEAPipeline(collection_name=collection_name)
    pipeline.run()

    print("[Test] DFMEA pipeline test complete.")
