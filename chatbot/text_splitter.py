## SINCE OUR FETCHED POSTS COULD BE OF LONGER SIZE, WE WILL USE THE RECURSIVECHARACTERTEXTSPLITTER TO SPLIT THE POSTS INTO SMALLER CHUNKS##
#


from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    @staticmethod
    def split_texts(texts: List[str], chunk_size: int = 30000, chunk_overlap: int = 500) -> List[str]:
        """Split texts into smaller chunks"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )
        split_texts = []
        for text in texts:
            chunks = text_splitter.split_text(text)
            split_texts.extend(chunks)
        return split_texts