from rest_framework import serializers
from .models import Empleado, Sucursal
from .models import Movimientos


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields='__all__'

class MovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movimientos
        fields='__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sucursal
        fields='__all__'


#content = EmpleadoSerializer(empleado).data
#y= JSONRenderer().render(content)

# A from io import BytesIO
#stream = BytesIO(y)
#parseado = JSONParser().parse(stream)