class Usuario:
  def __init__(self, nome):
    self.__nome = nome
    self.__livros_emprestados = []
  
  def emprestar(self, livro):
    self.__livros_emprestados.append(livro)
    print(f"O livro {livro.__titulo} foi emprestado com sucesso!")

