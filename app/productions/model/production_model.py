

class ProductionModel():
    
    def __init__(self, id=None, variedad=None, acres=None, intake_ont=None, pending=None, intake=None) -> None:
        self.id = id
        self.variety = variedad
        self.ontario_acres = acres
        self.intake_ont = intake_ont
        self.pending = pending
        self.intake = intake
        
    def __str__(self):
        return {
            "id": self.id,
            "variety": self.variety,
            "ontario_acres": self.ontario_acres,
            "intake_ont": self.intake_ont,
            "pending":self.pending,
            "intake":self.intake
        }