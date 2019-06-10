from .initializer_model import InitializerModel

class Tag(InitializerModel):

    def _init_properties_custom(self, value, prop, arr):

        if prop == 'id':
            self.identifier = value
        
        standart_properties = [
            'media_count',
            'name',
        ]

        if prop in standart_properties:
            self.__setattr__(prop, value)
