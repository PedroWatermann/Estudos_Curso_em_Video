ini = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
for i in range(ini, fim + 1):
    if len(str(i)) == 2:  # Agora verificamos corretamente se tem 2 dígitos
        filename = f"d0{i}.py"
    else:
        filename = f"d{i}.py"

    with open(filename, "w") as f:
        f.write("##")

print("Arquivos criados com sucesso!")
