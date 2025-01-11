from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    categoria = db.Column(db.String(50), nullable=False)
    tempo_min = db.Column(db.Integer, nullable=False)

    # Relacionamento com requerimentos
    requerimentos = db.relationship('Requerimento', back_populates='fornecedor', lazy='dynamic')
    
    # Relacionamento com produtos
    produtos = db.relationship('Produto', back_populates='fornecedor', lazy='dynamic')

    def __repr__(self):
        return f"<Fornecedor {self.nome}>"


class Produto(db.Model):
    __tablename__ = 'produtos'
    id_produto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id_fornecedor'), nullable=False)

    # Relacionamento com fornecedor
    fornecedor = db.relationship('Fornecedor', back_populates='produtos')

    def __repr__(self):
        return f"<Produto {self.nome}, Quantidade: {self.quantidade}>"


from sqlalchemy.sql import expression

class Requerimento(db.Model):
    __tablename__ = 'requerimentos'
    id_requerimento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id_fornecedor'), nullable=False)
    estado = db.Column(
        db.String(50),
        nullable=False,
        default='EM ESPERA',
        server_default='EM ESPERA'
    )
    data = db.Column(db.DateTime, server_default=db.func.now())
    alocado = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
        server_default=expression.false()
    )
    fornecedor = db.relationship('Fornecedor', back_populates='requerimentos')

    __table_args__ = (
        CheckConstraint(
            "estado IN ('EM ESPERA', 'EM PREPARAÇÃO', 'ENVIADO', 'FINALIZADO')",
            name='check_estado_valido'
        ),
    )

    def __repr__(self):
        return f"<Requerimento ID: {self.id_requerimento}, Estado: {self.estado}, Alocado: {self.alocado}>"



class Pedido(db.Model):
    __tablename__ = 'pedidos'
    requerimento_id = db.Column(db.Integer, db.ForeignKey('requerimentos.id_requerimento'), primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), primary_key=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id_fornecedor'), primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)

    # Relacionamentos
    requerimento = db.relationship('Requerimento', backref='pedidos', lazy=True)
    produto = db.relationship('Produto', backref='pedidos', lazy=True)
    fornecedor = db.relationship('Fornecedor', backref='pedidos', lazy=True)

    def __repr__(self):
        return f"<Pedido Requerimento ID: {self.requerimento_id}, Produto ID: {self.produto_id}, Quantidade: {self.quantidade}>"

