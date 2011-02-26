from should_dsl import should, should_not
import unittest
import specloud
from datetime import date

#INICIANDO TESTES USANDO SHOULD_DSL

from bd import Paciente


class Test_Paciente(unittest.TestCase):

	def test_adicionar_novo_paciente(self):
		self.paciente = Paciente(1,'Guilherme',2,3)
		self.paciente.id |should| equal_to (1)
		self.paciente.nome |should| equal_to("Guilherme")
		self.paciente.seguro |should| equal_to(2)
		self.paciente.idade |should| equal_to(3)	
		#self.paciente.seguro |should| equal_to(1)
	
	
if __name__ == "__main__":
	unittest.main()
