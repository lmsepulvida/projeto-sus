from should_dsl import should, should_not
import unittest
import specloud
from datetime import date

#INICIANDO TESTES USANDO SHOULD_DSL

from bd import Paciente, Medico, Hospital

class Test_Paciente(unittest.TestCase):

	def test_adicionar_novo_paciente(self):
		self.paciente = Paciente(1,'Guilherme',2,3)
		self.paciente.id |should| equal_to (1)
		self.paciente.nome |should| equal_to("Guilherme")
		self.paciente.seguro |should| equal_to(2)
		self.paciente.idade |should| equal_to(3)	
		#self.paciente.seguro |should| equal_to(1)

class Test_Medico(unittest.TestCase):

	def test_adicionar_novo_medico(self):
		self.medico = Medico(1,'Roberto',2222,'clinico')
		self.medico.id |should| equal_to (1)
		self.medico.nome |should| equal_to("Roberto")
		self.medico.matricula |should| equal_to(2222)
		self.medico.especialidade |should| equal_to("clinico")	
	
class Test_Hospital(unittest.TestCase):

	def test_adicionar_novo_hospital(self):
		self.hospital = Hospital(1,'Hospital Santa Luzia', "Rua das flores 30")
		self.hospital.id |should| equal_to (1)
		self.hospital.nome |should| equal_to("Hospital Santa Luzia")
		self.hospital.endereco |should| equal_to("Rua das flores 30")
		

if __name__ == "__main__":
	unittest.main()
