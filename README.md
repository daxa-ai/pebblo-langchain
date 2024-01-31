<p align="center">
  <img src="https://github.com/daxa-ai/pebblo/blob/main/docs/gh_pages/assets/img/pebblo-logo.png?raw=true" />
</p>

---
[![GitHub](https://img.shields.io/badge/GitHub-pebblo_langchain-blue?logo=github)](https://github.com/daxa-ai/pebblo-langchain)
[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/Documentation-pebblo-blue?logo=read-the-docs)](https://daxa-ai.github.io/pebblo-docs/)

[![PyPI](https://img.shields.io/pypi/v/pebblo-langchain?logo=pypi)](https://pypi.org/project/pebblo-langchain/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pebblo-langchain)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pebblo-langchain?logo=python&logoColor=gold)

[![Discord](https://img.shields.io/discord/1199861582776246403?logo=discord)](https://discord.gg/Qp5ZunuE)
[![Twitter Follow](https://img.shields.io/twitter/follow/daxa_ai)](https://twitter.com/daxa_ai)
---


**Pebblo** enables developers to safely load data and promote their Gen AI app to deployment without worrying about the organization’s compliance and security requirements. The project identifies semantic topics and entities found in the loaded data and summarizes them on the UI or a PDF report.

Pebblo has two components.

1. Pebblo Daemon - a REST api application with topic-classifier, entity-classifier and reporting features
1. Pebblo Safe DataLoader - a thin wrapper to Gen-AI framework's data loaders

This project hosts the `pebblo-langchain` package required for `Pebblo Safe DataLoader` for Langchain. See the main `Pebblo` project repository for more details on the `Pebblo Daemon` at [https://github.com/daxa-ai/pebblo](https://github.com/daxa-ai/pebblo)

## Pebblo Safe DataLoader for Langchain

`Pebblo Safe DataLoader` currently supports Langchain framework.

### Installation

Install `pebblo-langchain` package in the Python environment where the RAG application is running. Add it as one of the dependencies in `pyproject.toml` or any other methods used for dependency management.

```bash
pip install pebblo-langchain
```

### Enable Pebblo in Langchain

Add `PebbloSafeLoader` wrapper to the existing Langchain document loader(s) used in the RAG application. `PebbloSafeLoader` is interface compatible with Langchain `BaseLoader`. The application can continue to use `load()` and `lazy_load()` methods as it would on an Langchain document loader.

Here is the snippet of Lanchain RAG application using `CSVLoader` before enabling `PebbloSafeLoader`.

```python
    from langchain.document_loaders.csv_loader import CSVLoader

    loader = CSVLoader(file_path)
    documents = loader.load()
    vectordb = Chroma.from_documents(documents, OpenAIEmbeddings())
```

The Pebblo SafeLoader can be enabled with few lines of code change to the above snippet.

```python
    from langchain.document_loaders.csv_loader import CSVLoader
    from pebblo_langchain.langchain_community.document_loaders.pebblo import PebbloSafeLoader

    loader = PebbloSafeLoader(
                CSVLoader(file_path),
                name="acme-corp-rag-1", # App name (Mandatory)
                owner="Joe Smith", # Owner (Optional)
                description="Support productivity RAG application", # Description (Optional)
    )
    documents = loader.load()
    vectordb = Chroma.from_documents(documents, OpenAIEmbeddings())
```

See [here](https://github.com/srics/pebblo/tree/main/samples) for samples with Pebblo enabled RAG applications and [this](https://daxa-ai.github.io/pebblo-docs/rag.html) document for more details.

# Contribution

Pebblo is a open-source community project. If you want to contribute see [Contributor Guidelines](https://github.com/daxa-ai/pebblo/blob/main/CONTRIBUTING.md) for more details.

# License

Pebblo is released under the MIT License
