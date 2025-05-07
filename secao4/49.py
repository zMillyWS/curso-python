"""
Exercício 49: Calcule o horário de término de
uma experiência dado o horário inicial e a duração em segundos.
"""
ihora, imin, iseg = input(
    "Digite o horário de início da "
    "experiencia em Horas, minutos e segundos: ").split()
d = int(input("Digite o tempo de duracao da experiencia, em segundos: "))
s_final = (int(iseg) + d) % 60
m_final = (int(imin) + (int(iseg) + d) / 60) % 60
h_final = (int(ihora) + (int(imin) + (int(iseg) + d) / 60) / 60) % 24
print(f"A experiencia terminou em: {h_final:.0f}:{m_final:.0f}:{s_final:.0f}")
