import tkinter as tk
from tkinter import messagebox

class ContaBancaria:
    def __init__(self, numero_conta, titular, senha, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "O valor do depósito deve ser positivo."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        elif valor > self.saldo:
            return "Saldo insuficiente para realizar o saque."
        else:
            return "O valor do saque deve ser positivo."

    def verificar_saldo(self):
        return f"Saldo atual de R${self.saldo:.2f}"

class SimBank:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, titular, senha):
        if numero_conta not in self.contas:
            nova_conta = ContaBancaria(numero_conta, titular, senha)
            self.contas[numero_conta] = nova_conta
            return f"Conta {numero_conta} criada com sucesso para {titular}."
        else:
            return "Número de conta já existe."

    def acessar_conta(self, numero_conta, senha):
        conta = self.contas.get(numero_conta, None)
        if conta and conta.senha == senha:
            return conta
        return None

class SimBankApp:
    def __init__(self, root):
        self.banco = SimBank()
        self.root = root
        self.root.title("SimBank")

        # Layout da janela principal
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f2f5")

        # Frames para as diferentes telas
        self.frame_criar_conta = tk.Frame(root, bg="#f0f2f5")
        self.frame_acessar_conta = tk.Frame(root, bg="#f0f2f5")
        self.frame_operacoes_conta = tk.Frame(root, bg="#f0f2f5")

        # Configurações dos frames para ocupar toda a tela
        for frame in (self.frame_criar_conta, self.frame_acessar_conta, self.frame_operacoes_conta):
            frame.grid(row=0, column=0, sticky="nsew")

        self.tela_criar_conta()
        self.tela_acessar_conta()
        self.tela_operacoes_conta()

        # Exibir a tela de criar conta inicialmente
        self.frame_criar_conta.tkraise()

    def tela_criar_conta(self):
        # Tela de criação de conta
        container = tk.Frame(self.frame_criar_conta, bg="#f0f2f5")
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        tk.Label(container, text="Criar Conta", font=("Helvetica", 18, "bold"), bg="#f0f2f5").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        tk.Label(container, text="Número da Conta:", bg="#f0f2f5").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_numero_conta = tk.Entry(container, font=("Helvetica", 12))
        self.entry_numero_conta.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(container, text="Titular:", bg="#f0f2f5").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_titular = tk.Entry(container, font=("Helvetica", 12))
        self.entry_titular.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(container, text="Senha:", bg="#f0f2f5").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_senha = tk.Entry(container, show="*", font=("Helvetica", 12))
        self.entry_senha.grid(row=3, column=1, pady=5, padx=5)

        tk.Button(container, text="Criar Conta", command=self.criar_conta, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=2, pady=15)
        tk.Button(container, text="Ir para Acessar Conta", command=lambda: self.frame_acessar_conta.tkraise(), font=("Helvetica", 12), bg="#333333", fg="white").grid(row=5, column=0, columnspan=2)

        self.label_mensagem_criar = tk.Label(container, text="", fg="#4CAF50", bg="#f0f2f5")
        self.label_mensagem_criar.grid(row=6, column=0, columnspan=2)

    def tela_acessar_conta(self):
        # Tela de acesso à conta
        container = tk.Frame(self.frame_acessar_conta, bg="#f0f2f5")
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        tk.Label(container, text="Acessar Conta", font=("Helvetica", 18, "bold"), bg="#f0f2f5").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        tk.Label(container, text="Número da Conta:", bg="#f0f2f5").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_numero_acesso = tk.Entry(container, font=("Helvetica", 12))
        self.entry_numero_acesso.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(container, text="Senha:", bg="#f0f2f5").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_senha_acesso = tk.Entry(container, show="*", font=("Helvetica", 12))
        self.entry_senha_acesso.grid(row=2, column=1, pady=5, padx=5)

        tk.Button(container, text="Acessar Conta", command=self.acessar_conta, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=2, pady=15)
        tk.Button(container, text="Voltar para Criar Conta", command=lambda: self.frame_criar_conta.tkraise(), font=("Helvetica", 12), bg="#333333", fg="white").grid(row=4, column=0, columnspan=2)

        self.label_mensagem_acesso = tk.Label(container, text="", fg="#4CAF50", bg="#f0f2f5")
        self.label_mensagem_acesso.grid(row=5, column=0, columnspan=2)

    def tela_operacoes_conta(self):
        # Tela de operações da conta
        container = tk.Frame(self.frame_operacoes_conta, bg="#f0f2f5")
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        tk.Label(container, text="Operações da Conta", font=("Helvetica", 18, "bold"), bg="#f0f2f5").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        tk.Label(container, text="Valor:", bg="#f0f2f5").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_valor = tk.Entry(container, font=("Helvetica", 12))
        self.entry_valor.grid(row=1, column=1, pady=5, padx=5)

        tk.Button(container, text="Depositar", command=self.depositar, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(container, text="Sacar", command=self.sacar, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(container, text="Verificar Saldo", command=self.verificar_saldo, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(container, text="Voltar", command=lambda: self.frame_acessar_conta.tkraise(), font=("Helvetica", 12), bg="#333333", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        self.label_mensagem_operacoes = tk.Label(container, text="", fg="#4CAF50", bg="#f0f2f5")
        self.label_mensagem_operacoes.grid(row=6, column=0, columnspan=2)

    # Métodos de funcionalidade
    def criar_conta(self):
        numero_conta = self.entry_numero_conta.get()
        titular = self.entry_titular.get()
        senha = self.entry_senha.get()
        mensagem = self.banco.criar_conta(numero_conta, titular, senha)
        self.label_mensagem_criar.config(text=mensagem)
        self.entry_numero_conta.delete(0, tk.END)
        self.entry_titular.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)

    def acessar_conta(self):
        numero_conta = self.entry_numero_acesso.get()
        senha = self.entry_senha_acesso.get()
        self.conta_atual = self.banco.acessar_conta(numero_conta, senha)
        if self.conta_atual:
            self.label_mensagem_acesso.config(text=f"Conta {numero_conta} acessada com sucesso.")
            self.frame_operacoes_conta.tkraise()
        else:
            self.label_mensagem_acesso.config(text="Número da conta ou senha incorretos.")

    def depositar(self):
        try:
            valor = float(self.entry_valor.get())
            mensagem = self.conta_atual.depositar(valor)
            self.label_mensagem_operacoes.config(text=mensagem)
            self.entry_valor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido para depósito.")

    def sacar(self):
        try:
            valor = float(self.entry_valor.get())
            mensagem = self.conta_atual.sacar(valor)
            self.label_mensagem_operacoes.config(text=mensagem)
            self.entry_valor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido para saque.")

    def verificar_saldo(self):
        mensagem = self.conta_atual.verificar_saldo()
        self.label_mensagem_operacoes.config(text=mensagem)

# Inicializar o aplicativo
root = tk.Tk()
app = SimBankApp(root)
root.mainloop()
