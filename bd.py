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

	def __init__(self, meu_nome, meu_crm, minha_matricula, minha_especialidade, meu_hospital):	
		#self.id = id
		self.nome = meu_nome
		self.crm = meu_crm
		self.matricula = minha_matricula
		self.especialidade = minha_especialidade
		self.hospitais = []
		self.addHospital(meu_hospital)
		self.salvaMedicos(self)
	
	def addHospital(self,hospital):
		if (len(self.hospitais) == 3):
	            raise RuntimeError("Maximo de 3 hospitais atingido")
	        elif (hospital in self.hospitais):
	           raise RuntimeError("Medico ja cadastrado neste hospital")
	        else:
	            self.hospitais.append(hospital)
		    
	@staticmethod        
	def salvaMedicos(self):
        	self.medicos.append(self)

	#def addHospital(self, hospital):
        #	self.hospitais.append(hospital)
	#	print "metodo de baixo"
	

class Enfermeira():
	enfermeiras = []	
	
	def __init__(self, meu_nome, minha_matricula, meu_cargo, meu_hospital):	
		#self.id = id
		self.nome = meu_nome
		self.matricula = minha_matricula
		self.cargo = meu_cargo
		self.hospitais = []
		self.addHospital(meu_hospital)
		self.salvaEnfermeiras(self)

	def addHospital(self,hospital):
		if (len(self.hospitais) == 3):
	            raise RuntimeError("Maximo de 3 hospitais atingido")
	        elif (hospital in self.hospitais):
	           raise RuntimeError("Enfermeiro ja cadastrado neste hospital")
	        else:
	            self.hospitais.append(hospital)

	@staticmethod        
	def salvaEnfermeiras(self):
        	self.enfermeiras.append(self)
	
	#def addHospital(self, hospital):
        #	self.hospitais.append(hospital)

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
	def __init__(self, intern_paciente, intern_data_entrada, intern_hospital, intern_medicos, intern_enfermeiros, intern_data_saida):	
		#self.id = id		
		self.paciente = intern_paciente
		self.data_entrada = intern_data_entrada				
		self.hospital = intern_hospital
		#self.medico = intern_medico
		#self.enfermeiro = intern_enfermeiro		
		self.int_medicos = []
		self.addMedico(intern_medicos)
		self.int_enfermeiros = []
		self.addEnfermeiro(intern_enfermeiros)
		self.data_saida	= intern_data_saida
		self.salvaInternacoes(self)
		

	@staticmethod        
	def salvaInternacoes(self):
        	self.internacoes.append(self)

	def addMedico(self, medico):
        	self.int_medicos.append(medico)

	def addEnfermeiro(self, enfermeiro):
        	self.int_enfermeiros.append(enfermeiro)

