def new_collection(initial_docs):
    # Make a copy so the original list is not modified
    docs = initial_docs.copy()

    def add_doc(doc):
        docs.append(doc)
        return docs

    return add_doc
