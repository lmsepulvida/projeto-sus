from should_dsl import should, should_not
import unittest
import specloud
from datetime import date

#INICIANDO TESTES USANDO SHOULD_DSL

from bd import *

class Test_Paciente(unittest.TestCase):

	def test_adicionar_novo_paciente(self):
		self.paciente = Paciente('Guilherme',2,3)
		#self.paciente.id |should| equal_to (1)
		self.paciente.nome |should| equal_to("Guilherme")
		self.paciente.seguro |should| equal_to(2)
		self.paciente.idade |should| equal_to(3)	
		#self.paciente.seguro |should| equal_to(1)

class Test_Medico(unittest.TestCase):

	def test_adicionar_novo_medico(self):
		self.medico = Medico('Roberto',3333, 2222,'clinico')
		#self.medico.id |should| equal_to (1)
		self.medico.nome |should| equal_to("Roberto")
		self.medico.crm |should| equal_to(3333)
		self.medico.matricula |should| equal_to(2222)
		self.medico.especialidade |should| equal_to("clinico")
		#self.adicionar_hospital("santa casa")
		#self.adicionar_hospital("santa casa")		
		len(self.medico.hospitais) |should| be_less_than_or_equal_to (3)
		#self.medico.adicionar_hospital("santa casa") |should_not| include_all_of(["santa casa"])
	
class Test_Enfermeira(unittest.TestCase):

	def test_adicionar_nova_enfermeira(self):
		self.enfermeira = Enfermeira('Maria',2222,'Chefe enfermagem')
		#self.enfermeira.id |should| equal_to (1)
		self.enfermeira.nome |should| equal_to("Maria")
		self.enfermeira.matricula |should| equal_to(2222)
		self.enfermeira.cargo |should| equal_to("Chefe enfermagem")
		len(self.enfermeira.hospitais) |should| be_less_than_or_equal_to (3)

class Test_Hospital(unittest.TestCase):

	def test_adicionar_novo_hospital(self):
		self.hospital = Hospital('Hospital Santa Luzia',2,"Rua das flores 30")
		#self.hospital.id |should| equal_to (1)
		self.hospital.nome |should| equal_to("Hospital Santa Luzia")
		self.hospital.codigo |should| equal_to (2)
		self.hospital.endereco |should| equal_to("Rua das flores 30")
		
class Test_Internacao(unittest.TestCase):

	def test_realizar_internacao(self):
		self.internacao = Internacao(1,22/03/2010,"hgg","house","nurse",0)
		self.internacao.paciente |should| equal_to (1)		
		self.internacao.data_entrada |should| equal_to (22/03/2010)
		self.internacao.hospital |should| equal_to ("hgg")
		self.internacao.medico |should| equal_to ("house")
		self.internacao.enfermeiro |should| equal_to ("nurse")
		#COMO ESPECIFICAR UMA INTERNACAO SEM DATA DE SAIDA?
		#CRIAR CLASSE/TEST REALIZAR_AUTA?
		self.internacao.data_saida |should| equal_to (0)
			
if __name__ == "__main__":
	unittest.main()
