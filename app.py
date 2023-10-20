import os 
from haystack import Document
from haystack import pipelines
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever

class MultiModSearch:
    def __init__(self):
        self.document_sotores = InMemoryDocumentStore(embedding_dim=512)
        doc_dir = "new_data"
        