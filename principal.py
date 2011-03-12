
# -*- coding: cp860 -*-
from os import system
from datetime import date
from bd import *

option = 0


system("clear") 

while option != 7:
    print " ---- PROJETO-SUS ---- "
    print 
    print "Escolha o que deseja fazer: "
    print "1 - Cadastrar Paciente"
    print "2 - Cadastrar Medico(a)"
    print "3 - Cadastrar Enfermeiro(a)"
    print "4 - Cadastrar Hospital"
    print "5 - Internação de Paciente"
    print "6 - Liberação de Paciente"
    print "7 - Sair"
    option = input()

    if option == 1:
        print "CADASTRO DE PACIENTE"
        print "Digite o nome: "
        name = raw_input()
        print "Digite o codigo de seguro social: "
        css = raw_input()
        print "Digite a idade: "
        age = raw_input()
        Paciente(name, css, age)
        print "Cadastrado com sucesso!"
	print
        
    if option == 2:
        print "CADASTRO DE MEDICO(A)"
        print "Digite o nome: "
        name = raw_input()
        print "Digite o CRM: "
        crm = raw_input()
        print "Digite a matricula: "
        registry = raw_input()
        print "Digite a especialidade: "
        spec = raw_input()
        Medico(name, crm, registry, spec)
	print "Cadastrado com sucesso!"
	print
    
    if option == 3:
        print "CADASTRO DE ENFERMEIRO(A)"
        print "Digite o nome: "
        name = raw_input()
        print "Digite a matricula: "
        registry = raw_input()
        print "Digite o cargo: "
        job = raw_input()
        Enfermeira(name, registry, job)
	print "Cadastrado com sucesso!"
	print

    if option == 4:
        print "CADASTRO DE HOSPITAL"
        print "Digite o nome: "
        name = raw_input()
        print "Digite o codigo: "
        code = raw_input()
        print "Digite o endereco: "
        address = raw_input()
        Hospital(name, code, address)
	print "Cadastrado com sucesso!"
    	print
    if option == 5:
        print "INTERNAÇÃO DE PACIENTE"
        print "Selecione um Paciente para internacao: "
        patient = raw_input()
        print "Digite a data de entrada: "
        date = raw_input()
        Internacao.open(patient, date)
            
    if option == 6:
        print "LIBERACAO DE PACIENTE INTERNADO"
        print "Selecione um paciente internado: "
        patient = raw_input()
        print "Digite a data de saida: "
        date = raw_input()
        Internacao.close(patient, date)
    
    if option == 7:
	system("clear")         
	print "Obrigado por utilizar nosso sistema"
        
