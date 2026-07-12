from config import CHUNK_SIZE

def create_chunks(text:str)->list[str]:
    chunks=[text[i:i+CHUNK_SIZE]
            for i in range (0,len(text),CHUNK_SIZE)]
    return chunks
