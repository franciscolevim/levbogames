from levbogames.environment.paths import levbopaths
from pyglet.resource import Loader


class Resources:
    """
    Administra los paths de los recursos que serán necesarios para un videojuego.
    """
    def __init__(self):
        self.__loader = Loader()


    def __str__(self):
        return f'Resources: {self.__loader.path}'


    def append_path(self, path:str, directory = ''):
        """
        Agrega un nuevo path a los recursos registrados.

        Args:
            path (str): Path donde se ecunetran los recursos, este campo puede ser la ruta absoluta a los recursos.
            directory (str, optional): Es el nombre del directorio que contiene a los recursos. Defaults to ''.
        """
        if path and path.strip() != '':
            self.__loader.path.append(f'{path}/{directory}' if directory and directory.strip() != '' else path)
            self.__loader.reindex()


    def append_sprites_path(self, path = '', directory = ''):
        """
        Agrega un nuevo path que debe contener sprites para un videojuego. El path default estará dado por el 
        directorio home del proyecto.

        Args:
            path (str, optional): Path donde se encuentran los sprites. Defaults to ''.
            directory (str, optional): directorio donde se encuentran los sprites. Defaults to ''.
        """
        self.append_path(path if path and path.strip() != '' else levbopaths.SPRITES_RESOURCE, directory)
