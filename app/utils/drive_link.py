def convert_drive_link(link: str) -> str:
    """
    Convierte un enlace de Google Drive a formato de descarga directa.
    Lanza ValueError si el enlace no es válido o no es convertible.
    """
    link = link.strip()
    if not link:
        raise ValueError("El enlace no puede estar vacío.")
    if "drive.google.com" not in link:
        raise ValueError("El enlace debe ser de Google Drive.")
    if "uc?id=" in link:
        raise ValueError("El enlace ya está convertido.")

    if "open?id=" in link:
        return link.replace("open?id=", "uc?id=")
    elif "file/d/" in link:
        # Extraer el ID del archivo
        import re
        match = re.search(r"file/d/([\w-]+)", link)
        if match:
            file_id = match.group(1)
            return f"https://drive.google.com/uc?id={file_id}"
        else:
            raise ValueError("No se pudo extraer el ID del archivo.")
    elif "drive.google.com/file/d/" in link:
        return link.replace("drive.google.com/file/d/", "drive.google.com/uc?id=")
    else:
        raise ValueError("El enlace no es compatible.")
