class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def obter_titulo(self):
        return self.titulo

    def obter_autor(self):
        return self.autor

    def obter_ano_publicacao(self):
        return self.ano_publicacao

    def esta_disponivel(self):
        return self.disponivel

    def definir_disponibilidade(self, status):
        self.disponivel = status


class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def obter_nome(self):
        return self.nome

    def obter_email(self):
        return self.email

    def emprestar_livro(self, livro):
        if livro.esta_disponivel():
            self.livros_emprestados.append(livro)
            livro.definir_disponibilidade(False)
            print(f"Livro '{livro.obter_titulo()}' emprestado para {self.nome}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.definir_disponibilidade(True)
            print(f"Livro '{livro.obter_titulo()}' devolvido por {self.nome}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não foi emprestado por {self.nome}.")


class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro.esta_disponivel():
            self.livros.append(livro)
            print(f"Livro '{livro.obter_titulo()}' adicionado à livraria.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' removido da livraria.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está na livraria.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None


class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        if usuario.obter_nome() != "":
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca.")
        else:
            print("Nome de usuário inválido.")

    def remover_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.obter_nome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.obter_nome() == nome:
                return usuario
        return None


# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

# Criação da livraria e gestor de usuários
livraria = Livraria()
gestor_usuarios = GestorUsuarios()

# Adicionar livros à livraria
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

# Adicionar usuários ao gestor de usuários
gestor_usuarios.adicionar_usuario(usuario1)
gestor_usuarios.adicionar_usuario(usuario2)

# Empréstimo de livro
usuario1.emprestar_livro(livro1)

# Tentativa de empréstimo de livro indisponível
usuario2.emprestar_livro(livro1)

# Devolução de livro
usuario1.devolver_livro(livro1)

# Remoção de livro
livraria.remover_livro(livro2)

# Remoção de usuário
gestor_usuarios.remover_usuario(usuario2)

# Busca de livro e usuário
livro_encontrado = livraria.buscar_livro("Python para Iniciantes")
usuario_encontrado = gestor_usuarios.buscar_usuario("Alice")

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.obter_titulo())

if usuario_encontrado:
    print(usuario_encontrado.obter_nome())