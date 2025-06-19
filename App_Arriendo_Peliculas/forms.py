from django import forms
 
# class CursoFormulario(forms.Form):
#     curso = forms.CharField()
#     camada = forms.IntegerField()

# class ProfesorFormulario(forms.Form):
#     nombre = forms.CharField(max_length=30)
#     apellido = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     profesion = forms.CharField(max_length=30)

class GeneroFormulario2(forms.Form):
        nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'size': 55})  # Cambia el número según el tamaño deseado
        )

class PeliculaFormulario2(forms.Form):
        titulo = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'size': 55})  # Cambia el número según el tamaño deseado
        )
        anio = forms.IntegerField(label="Año")
        disponible = forms.BooleanField()


class ClienteFormulario2(forms.Form):
        nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'size': 55})  # Cambia el número según el tamaño deseado
        )
        email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'size': 55})  # Cambia el número según el tamaño deseado
        )
