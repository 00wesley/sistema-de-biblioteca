import Livro as modulo_livro
classe_livro = modulo_livro.Livro

import Usuario as modulo_usuario
classe_usuario = modulo_usuario.Usuario

class Biblioteca:
  def __init__(self):
    self.__livros = []
    self.__usuarios = []
  
  @property
  def livros(self):
    return self.__livros
  
  @property
  def usuarios(self):
    return self.__usuarios

  def cadastrar_livro(self, livro: classe_livro):
    self.__livros.append(livro)
  
  def cadastrar_usuario(self, usuario: classe_usuario):
    self.__usuarios.append(usuario)

  def listar_livros_disponiveis(self):
    livro = classe_livro
    print("Livros disponíveis: ")
    indicie = 0
    for livro in self.livros:
      indicie += 1
      print(f"{indicie}. {livro.titulo}, autor: {livro.autor}")

  
  def emprestar_livro(self, livro: classe_livro, usuario: classe_usuario):
    if livro in self.livros and livro.disponivel == True and usuario in self.usuarios:
      usuario.emprestar_livro(livro)
      self.__livros.remove(livro)
    else:
      print("Algo deu errado verifique a disponibilidade do livro ou se o usuário está cadastrado")
  
  def devolver_livro (self, livro: classe_livro, usuario: classe_usuario):
    if livro in usuario.livros_emprestados:
      usuario.devolver_livro(livro)
      self.__livros.append(livro)
    else:
      print(f"{usuario.nome}, você não emprestou o livro {livro.titulo}")


