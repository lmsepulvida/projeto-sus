from datetime import date

class Paciente():
	def __init__(self, id, meu_nome, meu_seguro, minha_idade):
		self.id = id        
		self.nome = meu_nome
	        self.seguro = meu_seguro
	        self.idade = minha_idade
	        #self.StoragePacientes(self)

class Medico():
	def __init__(self, id, meu_nome, minha_matricula, minha_especialidade):	
		self.id = id
		self.nome = meu_nome
		self.matricula = minha_matricula
		self.especialidade = minha_especialidade

class Hospital():
	def __init__(self, id, meu_nome, meu_endereco):	
		self.id = id
		self.nome = meu_nome
		self.endereco = meu_endereco
		

