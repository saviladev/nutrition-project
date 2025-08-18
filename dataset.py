import kagglehub
import os
import shutil
from pathlib import Path

# Descargar la última versión del dataset.
path_descarga = kagglehub.dataset_download("kmader/food41") 

print("Ruta del dataset descargado (en caché):", path_descarga)

# La carpeta base para reorganizar es el directorio 'prueba'
trainings_path = Path("./trainings")
# Asegúrate de que la carpeta de destino exista
trainings_path.mkdir(exist_ok=True)

# El dataset se descarga en una subcarpeta específica dentro de la ruta devuelta
dataset_content_path = Path(path_descarga)

# Mover la carpeta images
images_source = dataset_content_path / "images"
if images_source.exists():
    images_dest = trainings_path / "images"
    if images_dest.exists():
        shutil.rmtree(images_dest)
    shutil.move(str(images_source), str(images_dest))
    print("Carpeta 'images' movida a prueba/")

# Mover la carpeta meta
meta_source = dataset_content_path / "meta"
if meta_source.exists():
    meta_dest = trainings_path / "meta"
    if meta_dest.exists():
        shutil.rmtree(meta_dest)
    shutil.move(str(meta_source), str(meta_dest))
    print("Carpeta 'meta' movida a prueba/")
    
print("Dataset reorganizado correctamente. Solo quedan las carpetas 'images' y 'meta' en prueba/")