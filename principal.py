
# -*- coding: cp860 -*-
from os import system
from datetime import date
from bd import *

option = 0


system("clear") 

while option != 9:
    print " ---- PROJETO-SUS ---- "
    print 
    print "Escolha o que deseja fazer: "
    print "1 - Cadastrar Paciente"
    print "2 - Cadastrar Medico(a)"
    print "3 - Cadastrar Enfermeiro(a)"
    print "4 - Cadastrar Hospital"
    print "5 - Internação de Paciente"
    print "6 - Liberação de Paciente"
    print "7 - Ver pacientes cadastrados"
    print "8 - Alterar Internacoes"
    print
    print "9 - Sair"
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
	for i in range(len(Paciente.pacientes)):
		print "[",i,"]",Paciente.pacientes[i].nome
        print "Selecione um Paciente para internacao: "
        patient_tmp = raw_input()
	opaciente = int(patient_tmp)	
	patient = Paciente.pacientes[opaciente].nome
        print "Digite a data de entrada: "
        date = raw_input()
	print "Selecione um hospital:"
	for i in range(len(Hospital.hospitais)):
		print "[",i,"]",Hospital.hospitais[i].nome  
	hospital_tmp = raw_input()
	ohospital = int(hospital_tmp)
	hospital = Hospital.hospitais[ohospital].nome
        print "Selecione um medico:"
	for i in range(len(Medico.medicos)):
		print "[",i,"]",Medico.medicos[i].nome
	        
	medic = int(raw_input())
	print "Selecione um enfermeiro:"
	for i in range(len(Enfermeira.enfermeiras)):
		print "[",i,"]",Enfermeira.enfermeiras[i].nome
        nurse = int(raw_input())

	Internacao(patient, date, hospital, Medico.medicos[medic].nome, Enfermeira.enfermeiras[nurse].nome,0)
	#Internacao.addMedico(Medico.medicos[medic].nome)    

    if option == 6:
        print "LIBERACAO DE PACIENTE INTERNADO"
        system("clear")         
	print "Pacientes internados:"	
	for i in range(len(Internacao.internacoes)):
		print "[",i,"]",Internacao.internacoes[i].paciente
	print "Selecione um paciente internado: "
        patient = raw_input()
        print "Digite a data de saida: "
        date = raw_input()
        Internacao.internacoes[i].data_saida = date
        
    if option == 7:
	system("clear")         
	for i in range(len(Paciente.pacientes)):
		print Paciente.pacientes[i].nome

    if option == 8:	
	system("clear")         
	print "INTERNACOES:"	
	for i in range(len(Internacao.internacoes)):
		print "[",i,"]",Internacao.internacoes[i].paciente
	print "Selecione uma internacao:"
        internation = int(raw_input())
      	print "Paciente: ",Internacao.internacoes[internation].paciente
	print "Data de entrada: ",Internacao.internacoes[internation].data_entrada
	print "Hospital: ",Internacao.internacoes[internation].hospital
	print "Medico: ",Internacao.internacoes[internation].medico
	print "Enfermeiro: ",Internacao.internacoes[internation].enfermeiro
	print "Data de alta: ",Internacao.internacoes[internation].data_saida	
#	for j in range(len(Internacao.internacoes[internation].medicos[j])):		
#		print "Medico ",j,": ",Internacao.internacoes[i].medicos[j]
	

    if option == 9:
	system("clear")         
	print "Obrigado por utilizar nosso sistema"

