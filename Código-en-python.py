"""
Nota: Código escrito por un chico lleno de insomnio.

Es algo raro lo que me pasa, pero, si no podemos dormir por algún motivo, sea cual sea, 
hay un motivo que debes considerar, y es algo complejo de entender. 
¿Recuerdas cuando solíamos irnos a dormir ya, cuando estábamos tan cansados que no podíamos más, 
y estábamos en contra de nuestra voluntad despiertos? 

En ese entonces, nuestros sueños eran mejor que la realidad en la que estábamos en ese momento. 
Pero si eres como yo, si has pasado cosas buenas, ya sea con alguien, con amigos, o personas, 
considera que el no poder dormir por estar pensando en cosas que viviste es una señal: 
tu realidad está siendo mejor que tus sueños.

Personalmente, viví cosas increíbles este año que jamás llegué a pensar. 
Me sentí vivo después de no ser nadie, ya no era ese fantasma. 
Esa chica me hizo la realidad tan linda, tan inexplicablemente hermosa, 
que justo ahora vivo en esos pensamientos. Y no quiero dormir, porque revivir todo eso 
y recrear las cosas en un futuro es justo lo que ahora anhelo. 

He trabajado por mejorar, para quizá arriesgarme por mi más grande amor. 
Eso me hace tener una realidad tan hermosa ahora que, en mis sueños, solo tengo pesadillas. 
Entonces, mi punto es: *El sueño se va una vez tu realidad es mejor que tus sueños.*

- Fin de la nota.
"""

import os
import shutil
from pathlib import Path

def get_disk_usage(path="/"):
    """Obtiene el uso de disco en una ruta específica."""
    usage = shutil.disk_usage(path)
    total_gb = usage.total / (1024**3)
    used_gb = usage.used / (1024**3)
    free_gb = usage.free / (1024**3)
    return total_gb, used_gb, free_gb

def find_large_files(path="/", min_size_mb=100):
    """Encuentra archivos grandes (mayores a min_size_mb) en un directorio."""
    large_files = []
    for root, _, files in os.walk(path):
        for file in files:
            try:
                file_path = Path(root) / file
                size_mb = file_path.stat().st_size / (1024**2)
                if size_mb >= min_size_mb:
                    large_files.append((str(file_path), size_mb))
            except Exception:
                continue
    return sorted(large_files, key=lambda x: x[1], reverse=True)

def clean_temp_files():
    """Limpia archivos temporales y cachés."""
    temp_dirs = ["/tmp", "/var/tmp", str(Path.home() / ".cache")]
    cleaned_space = 0
    for temp_dir in temp_dirs:
        try:
            for root, dirs, files in os.walk(temp_dir):
                for item in files + dirs:
                    item_path = Path(root) / item
                    size = item_path.stat().st_size
                    item_path.unlink() if item_path.is_file() else shutil.rmtree(item_path)
                    cleaned_space += size
        except Exception:
            continue
    return cleaned_space / (1024**2)  # Retorna espacio liberado en MB

def main():
    print("=== Optimizador de Espacio en Disco para Linux ===")
    
    # Mostrar uso de disco
    total, used, free = get_disk_usage()
    print(f"Espacio total: {total:.2f} GB")
    print(f"Espacio usado: {used:.2f} GB")
    print(f"Espacio libre: {free:.2f} GB\n")
    
    # Analizar archivos grandes
    print("Buscando archivos grandes...")
    large_files = find_large_files(min_size_mb=500)
    if large_files:
        print("\nArchivos grandes encontrados:")
        for file, size in large_files[:10]:
            print(f"{file} - {size:.2f} MB")
    else:
        print("No se encontraron archivos grandes.")
    
    # Sugerir limpieza de temporales
    clean = input("\n¿Deseas limpiar archivos temporales y cachés? (s/n): ").strip().lower()
    if clean == "s":
        freed_space = clean_temp_files()
        print(f"Liberado: {freed_space:.2f} MB eliminando temporales y cachés.")
  
    print("\nOptimización completada. Revisa los resultados y libera más espacio si es necesario.")

if __name__ == "__main__":
    main()
