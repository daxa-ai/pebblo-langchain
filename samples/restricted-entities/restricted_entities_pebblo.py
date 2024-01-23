from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.llms import OpenAI
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.vectorstores.utils import filter_complex_metadata
from typing import List

from pebblo_langchain.langchain_community.document_loaders.pebblo import PebbloSafeLoader

# Fill-in OPENAI_API_KEY and DAXA_API_KEY in .env file
# in this directory before proceeding

from dotenv import load_dotenv
load_dotenv()

class RestrictedEntitiesMD:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.app_name = "restricted-entities-1"

        # Load documents

        print(f"Loading RAG documents ...")
        self.loader = PebbloSafeLoader(
            UnstructuredMarkdownLoader(self.file_path, mode="elements"),
            self.app_name,
            "Joe Smith"
        )
        self.documents = self.loader.load()
        self.filtered_docs = filter_complex_metadata(self.documents)
        print(f"Loaded {len(self.documents)} documents ...\n")

        # Load documents into VectorDB

        print(f"Hydrating Vector DB ...")
        self.vectordb = self.embeddings(self.filtered_docs)
        print(f"Finished hydrating Vector DB ...\n")

        # Prepare retriever QA chain

        llm = OpenAI()
        self.retriever = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vectordb.as_retriever(),
            verbose=True
        )

    @staticmethod
    def embeddings(docs: List[Document]):
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(docs, embeddings)
        return vectordb

    def ask(self, query: str):
        return self.retriever.run(query)


if __name__ == "__main__":
    rag_app = RestrictedEntitiesMD("./data/personel_dump.md")
    prompt = "What is Jonathan's passport ID?"
    print(f"Query:\n{prompt}")
    response = rag_app.ask(prompt)
    print(f"Response:\n{response}")
