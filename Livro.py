class Livro:
  def __init__(self, titulo, autor):
    self.__titulo = titulo
    self.__autor = autor
    self.__disponivel = True

  @property
  def titulo(self):
    return self.__titulo
  
  @property
  def autor(self):
    return self.__autor
  
  @property
  def disponivel(self):
    return self.__disponivel

  def emprestar (self):
    if self.__disponivel == True:
      self.__disponivel = False
      print(f"O livro {self.__titulo} foi emprestado com sucesso!")
    elif self.__disponivel == False:
      print(f"O livro {self.__titulo}não está disponível para empréstimo no momento.")
  
  def devolver (self):
    if self.__disponivel == False:
      self.__disponivel = True
      print(f"O livro {self.__titulo} foi devolvido com sucesso!")
    elif self.__disponivel == True:
      print(f"O livro {self.__titulo} não foi emprestado.")