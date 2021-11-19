from django.db import models
import uuid 
# Criaçao de modelos de class
#definicao as propiedades metodo de uma instancia
class noticia(models.Model):
    
    def _init_(self, id_UUID, conteudo, autor, publicado, data_criação):
        self.id_UUID = id_UUID
        self.conteudo = conteudo
        self.autor = autor
        self.publicado = publicado
        self.data_criação = data_criação
        
    
   
    def get_id_UUID(self):  
        return self._id_UUID
    
 
    
    def conteudo(self):
        return self.conteudo
    
    
    def autor(self):
        return self.autor
    
    
    def publicado(self):
        return self.publicado
    
    
    def data_criação(self):
        return self.data_criação

    
    def detele(self, request, noticia):
        return self.id_UUID
     
