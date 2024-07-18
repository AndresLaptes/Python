# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    # TU CÓDIGO AQUÍ
    partes: str = smb_path.strip('//')
    host = partes[0]
    path = partes[1].rsplit('/')
    

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')