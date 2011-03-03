from datetime import date
from bd import *

option = 0

while option != 7:
    print " ---- PROJETO-SUS ---- "
    print "Escolha o que deseja fazer: "
    print "1 - Cadastrar Paciente"
    print "2 - Cadastrar Medico(a)"
    print "3 - Cadastrar Enfermeiro(a)"
    print "4 - Cadastrar Hospital"
    print "5 - Internacao de Paciente"
    print "6 - Liberacao de Paciente"
    print "7 - Sair"
    option = input()

    if option == 1:
        print "CADASTRO DE PACIENTE"
        print "Digite o nome: "
        name = input()
        print "Digite o codigo de seguro social: "
        css = raw_input()
        print "Digite a idade: "
        age = raw_input()
        Paciente(name, css, age)
        
    if option == 2:
        print "CADASTRO DE MEDICO(A)"
        print "Digite o nome: "
        name = input()
        print "Digite o CRM: "
        crm = raw_input()
        print "Digite a matricula: "
        registry = raw_input()
        print "Digite a especialidade: "
        spec = raw_input()
        Medico(name, crm, registry, spec)
    
    if option == 3:
        print "CADASTRO DE ENFERMEIRO(A)"
        print "Digite o nome: "
        name = input()
        print "Digite a matricula: "
        registry = raw_input()
        print "Digite o cargo: "
        job = raw_input()
        Enfermeiro(name, registry, job)

    if option == 4:
        print "CADASTRO DE HOSPITAL"
        print "Digite o nome: "
        name = input()
        print "Digite o codigo: "
        code = raw_input()
        print "Digite o endereco: "
        address = raw_input()
        Hospital(name, code, address)
    
    if option == 5:
        print "INTERNAÇÃO DE PACIENTE"
        print "Selecione um Paciente para internacao: "
        patient = input()
        print "Digite a data de entrada: "
        date = input()
        Intern.open(patient, date)
            
    if option == 6:
        print "LIBERACAO DE PACIENTE INTERNADO"
        print "Selecione um paciente internado: "
        patient = input()
        print "Digite a data de saida: "
        date = input()
        Intern.close(patient, date)
    
    if option == 7:
        print "Obrigado por utilizar nosso sistema"
        