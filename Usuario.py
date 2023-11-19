import Livro as modulo_livro
classe_livro = modulo_livro.Livro

class Usuario:
  def __init__(self, nome):
    self.__nome = nome
    self.__livros_emprestados = []
  
  @property
  def nome(self):
    return self.__nome
  
  @property
  def livros_emprestados(self):
    return self.__livros_emprestados
  
  def emprestar_livro(self, livro: classe_livro):
    if livro.disponivel == True:
      self.__livros_emprestados.append(livro)
      print(f"{self.nome}, o livro {livro.titulo} foi emprestado com sucesso!")
    elif livro.disponivel == False:
      print(f"{self.nome}, o livro {livro.titulo} não está disponível no momento!")
    
    
  def devolver_livro(self, livro: classe_livro):
    if livro in self.livros_emprestados:
      self.__livros_emprestados.remove(livro)
      print(f"{self.nome}, o livro {livro.titulo} foi devolvido.")
    else:
      print(f"{self.nome}, você não emprestou o livro {livro.titulo}")
 

