from datetime import date

class Paciente():
	def __init__(self, id, meu_nome, meu_seguro, minha_idade):
		self.id = id        
		self.nome = meu_nome
	        self.seguro = meu_seguro
	        self.idade = minha_idade
	        #self.StoragePacientes(self)

class Medico():
	def __init__(self, id, meu_nome, meu_crm, minha_matricula, minha_especialidade):	
		self.id = id
		self.nome = meu_nome
		self.crm = meu_crm
		self.matricula = minha_matricula
		self.especialidade = minha_especialidade

class Enfermeira():
	def __init__(self, id, meu_nome, minha_matricula, meu_cargo):	
		self.id = id
		self.nome = meu_nome
		self.matricula = minha_matricula
		self.cargo = meu_cargo


class Hospital():
	def __init__(self, id, meu_nome, meu_codigo, meu_endereco):	
		self.id = id		
		self.nome = meu_nome
		self.codigo = meu_codigo				
		self.endereco = meu_endereco
		

