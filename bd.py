from datetime import date

class Paciente():
	pacientes = []	

	def __init__(self, meu_nome, meu_seguro, minha_idade):
		#self.id = id        
		self.nome = meu_nome
	        self.seguro = meu_seguro
	        self.idade = minha_idade
		self.salvaPacientes(self)

	@staticmethod        
	def salvaPacientes(self):
        	self.pacientes.append(self)

class Medico():
	medicos = []	

	def __init__(self, meu_nome, meu_crm, minha_matricula, minha_especialidade):	
		#self.id = id
		self.nome = meu_nome
		self.crm = meu_crm
		self.matricula = minha_matricula
		self.especialidade = minha_especialidade
		self.salvaMedicos(self)

	@staticmethod        
	def salvaMedicos(self):
        	self.medicos.append(self)


class Enfermeira():
	enfermeiras = []	
	
	def __init__(self, meu_nome, minha_matricula, meu_cargo):	
		#self.id = id
		self.nome = meu_nome
		self.matricula = minha_matricula
		self.cargo = meu_cargo
		self.salvaEnfermeiras(self)

	@staticmethod        
	def salvaEnfermeiras(self):
        	self.enfermeiras.append(self)



class Hospital():
	hospitais = []
	def __init__(self, meu_nome, meu_codigo, meu_endereco):	
		#self.id = id		
		self.nome = meu_nome
		self.codigo = meu_codigo				
		self.endereco = meu_endereco
		self.salvaHospitais(self)

	@staticmethod        
	def salvaHospitais(self):
        	self.hospitais.append(self)



class Internacao():
	internacoes = []
	def __init__(self, intern_paciente, intern_data_entrada, intern_data_saida, intern_hospital, intern_medico, intern_enfermeiro):	
		#self.id = id		
		self.paciente = intern_paciente
		self.data_entrada = intern_data_entrada				
		self.hospital = intern_hospital
		self.int_medicos = []
		self.int_medicos.append(intern_medico)		
		self.int_enfermeiros = []
		self.int_enfermeiros.append(intern_enfermeiro)
		self.data_saida	= intern_data_saida
		self.salvaInternacoes(self)

	@staticmethod        
	def salvaInternacoes(self):
        	self.internacoes.append(self)

	def darAlta(self, intern_data_saida):	
		self.data_saida = intern_data_saida

