# Vulnerability Management System

## Description
The Vulnerability Management System is an AI-driven solution developed using Langchain and Ollama frameworks. It aims to ingest, analyze, and respond to vulnerability information, enhancing security posture and risk mitigation strategies.

## Components

### Document Ingestion and Analysis
- Utilized Langchain's document loaders to ingest vulnerability data from diverse sources, including CSV files, PDFs, HTML, and text documents.
- Employed HuggingFace's Transformer-based embeddings for high-dimensional representation of textual data.
- Implemented text splitting techniques to break down large documents into smaller chunks for efficient analysis.
- Processed and stored document embeddings in Chroma, a vector store optimized for similarity search.

### User Interaction
- Developed a user-facing interface using Tkinter for interaction with the vulnerability management system.
- Implemented functionality to retrieve a list of installed applications from the user's system, supporting both Windows and macOS environments.
- Generated queries based on the extracted application information and posed them to the Langchain-powered QA system.

## Workflow
1. **Data Ingestion:** Collect vulnerability data from various sources and preprocess for analysis.
2. **Embedding Generation:** Transform textual data into vector representations using pre-trained language models.
3. **Document Chunking:** Segment large documents into smaller chunks to facilitate analysis and storage.
4. **Vector Storage:** Store processed embeddings in Chroma for efficient retrieval and similarity search.
5. **User Interaction:** Interact with the system through a GUI to initiate vulnerability checks based on installed applications.
6. **Query Processing:** Construct queries based on user input and forward to the QA system for vulnerability assessment.
7. **Response Presentation:** Present vulnerability assessment results to the user, indicating the presence or absence of CVEs related to installed applications.

## Benefits
- Enhances security posture by proactively identifying and addressing vulnerabilities in installed applications.
- Streamlines vulnerability management workflows through automation and AI-driven analysis.
- Provides a user-friendly interface for easy interaction and accessibility.
