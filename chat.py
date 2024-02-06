# import spacy
# from haystack import Finder
# from haystack.preprocessor.cleaning import clean_wiki_text
# from haystack.preprocessor.utils import convert_files_to_dicts
# from haystack.reader.farm import FARMReader
# from haystack.reader.transformers import TransformersReader
# from haystack.utils import print_answers
# from converse import converse

# # Load Spacy model
# nlp = spacy.load("en_core_web_sm", disable=["ner"])

# # Load data from 'data' folder
# doc_dir = "data"
# docs = convert_files_to_dicts(dir_path=doc_dir, clean_func=clean_wiki_text, split_paragraphs=True)

# # Initialize reader and finder
# reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
# finder = Finder(reader, None)

# # Function to handle user input
# def handle_input(user_input):
#     if "..." in user_input:
#         # If the input ends with '...', generate a continuation of the sentence
#         doc = nlp(user_input)
#         last_sentence = list(doc.sents)[-1]
#         continuation = converse(last_sentence.text)
#         return continuation
#     else:
#         # Otherwise, use the input as a question and find an answer in the data
#         prediction = finder.get_answers(question=user_input, top_k_retriever=10, top_k_reader=5)
#         return prediction['answers'][0]['answer']

# # Main function
# def main():
#     user_input = input("Please enter something: ")
#     response = handle_input(user_input)
#     print(response)

# if __name__ == "__main__":
#     main()