from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'



#content = EmpleadoSerializer(empleado).data
#y= JSONRenderer().render(content)

# A from io import BytesIO
#stream = BytesIO(y)
#parseado = JSONParser().parse(stream)