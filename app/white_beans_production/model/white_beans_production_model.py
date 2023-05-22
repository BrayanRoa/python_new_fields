

class WhiteBeansProductionModel():
    
    def __init__(self, id, variety, ontario_acres, intake_ont, pending, intake, dumped,estimate_planted, percentage_of_sales) -> None:
        self.id=id
        self.variety=variety
        self.ontario_acres=ontario_acres
        self.intake_ont=intake_ont
        self.pending=pending
        self.intake=intake
        self.dumped=dumped
        self.estimate_planted=estimate_planted
        self.percentage_of_sales=percentage_of_sales
        
    def __str__(self):
        return {
            "id": self.id,
            "variety": self.variety,
            "ontario_acres": self.ontario_acres,
            "intake_ont": self.intake_ont,
            "pending":self.pending,
            "intake":self.intake,
            "dumped":self.dumped,
            "estimate_planted":self.estimate_planted,
            "percentage_of_sales":self.percentage_of_sales
        }