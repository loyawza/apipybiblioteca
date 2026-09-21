from fastapi import FastAPI, HTTPException
from models import Libro, Editorial

app = FastAPI()
ed1 = Editorial(idEd=1, nombre="O'Reilly", pais="Estados Unidos")
ed2 = Editorial(idEd=2, nombre="McGraw Hill", pais="Estados Unidos")
ed3 = Editorial(idEd=3, nombre="Alfaomega", pais="México")
ed4 = Editorial(idEd=4, nombre="Marcombo", pais="España")

lib1 = Libro(ISBN="978-1", titulo="Introducción a Python", autor="Guido van Rossum", precio=450.50)
lib2 = Libro(ISBN="978-2", titulo="Bases de Datos Relacionales", autor="C.J. Date", precio=520.00)
lib3 = Libro(ISBN="978-3", titulo="Desarrollo con FastAPI", autor="Sebastián Ramírez", precio=380.00)
lib4 = Libro(ISBN="978-4", titulo="Estructuras de Datos", autor="Luis Joyanes", precio=410.20)
lib5 = Libro(ISBN="978-5", titulo="Redes de Computadoras", autor="Andrew S. Tanenbaum", precio=600.00)

editoriales_db = {1: ed1, 2: ed2, 3: ed3, 4: ed4}
libros_db = {"978-1": lib1, "978-2": lib2, "978-3": lib3, "978-4": lib4, "978-5": lib5}

@app.get("/libros/{isbn}", response_model=Libro)
async def obtener_libro(isbn: str):
    if isbn not in libros_db:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libros_db[isbn]

@app.get("/editoriales/{id_ed}", response_model=Editorial)
async def obtener_editorial(id_ed: int):
    if id_ed not in editoriales_db:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return editoriales_db[id_ed]
