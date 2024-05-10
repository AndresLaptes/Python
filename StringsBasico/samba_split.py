# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    # TU CÓDIGO AQUÍ
    host = smb_path.partition('/')
    path = smb_path

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')