class Expense:
    def __init__(self,name,category,amount) -> None:
        self.name=name
        self.category=category
        self.amount=amount
        pass
    def __repr__(self) -> str:
        return f"<Expense : {self.name},{self . category},${self.amount:.2f}>"

__all__=["Expense"]
