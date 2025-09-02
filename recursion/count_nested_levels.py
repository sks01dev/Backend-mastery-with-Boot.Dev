def count_nested_levels(nested_documents, target_document_id, level=1):
    # Loop over document_ids in the nested_documents dictionary
    for document_id, children in nested_documents.items():
        # return current level of nesting if matches the target
        if document_id == target_document_id:
            return level
        # recurse if children existeed
        result = count_nested_levels(children, target_document_id, level+1)
        if result != -1:
            return result
        
    # if not found return -1
    return -1
