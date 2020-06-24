import os


class LevboPaths:
    """
    Rutas predeterminadas para el módulo de videojuegos.
    """
    def __init__(self):
        """[summary]
        """
        self.__LEVBOGAMES_ENV = 'LEVBOGAMES'
        self.__RESOURCES_DIRECTORY = 'resources'
        self.__SPRITES_DIRECTORY = 'sprites'


    @property
    def RESOURCES_PATH(self):
        """
        Path donde se encuentran los recursos de levbogames.
        
        Se utiliza la variable de entorno LEVBOGAMES para ubicarse en el directorio principal de levbogames, si esta 
        variable no se ecuentra definida se asume el directorio de ejecución (.).
        """
        try:
            levbogames_path = os.environ[self.__LEVBOGAMES_ENV ]
        except KeyError as keyE:
            levbogames_path = '.'
        finally:
            return f'{levbogames_path}/{self.__RESOURCES_DIRECTORY}'


    @property
    def SPRITES_RESOURCE(self):
        """
        Path donde se ecueuntran los sprites de levbogames. 
        
        Este debe localizarse en resources/sprites
        """        
        return f'{self.RESOURCES_PATH}/{self.__SPRITES_DIRECTORY}'


levbopaths = LevboPaths()
    