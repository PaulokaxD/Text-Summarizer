from datasets import load_dataset


# book_data = load_dataset("ubaada/booksum-complete-cleaned", "books")
book_data = load_dataset("ubaada/booksum-complete-cleaned", "chapters")

# print(book_data.shape)
print(book_data['train'])



# # Process the dataset - add a column with the length of the context texts
# dataset_with_length = squad_dataset.map(lambda x: {"length": len(x["context"])})

# # Process the dataset - tokenize the context texts (using a tokenizer from the 🤗 Transformers library)
# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

# tokenized_dataset = squad_dataset.map(lambda x: tokenizer(x['context']), batched=True)