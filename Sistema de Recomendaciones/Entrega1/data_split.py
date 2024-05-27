import pandas as pd
import os

# Define el tamaño del chunk, por ejemplo 100000 líneas por archivo
chunksize = 100000

# Directorio donde se guardarán los archivos divididos
output_dir = './data/chunks'
os.makedirs(output_dir, exist_ok=True)

# Leer el archivo en chunks
chunk_iter = pd.read_json('./data/yelp_academic_dataset_review.json', lines=True, chunksize=chunksize)

# Guardar cada chunk en un archivo separado
for i, chunk in enumerate(chunk_iter):
    chunk.to_json(os.path.join(output_dir, f'yelp_review_chunk_{i}.json'), orient='records', lines=True)

print("Archivo dividido exitosamente.")