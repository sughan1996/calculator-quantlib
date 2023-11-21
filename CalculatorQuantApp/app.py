from CalculatorQuantApp.controllers import CalculatorQuant

calculator = CalculatorQuant()

def lambda_handler_add(event : {} = None):
    resp = calculator.quant_add(**event)
    return resp

def lambda_handler_subtract(event : {} = None):
    resp = calculator.quant_subtract(**event)
    return resp

def lambda_handler_multiply(event : {} = None):
    resp = calculator.quant_multiply(**event)
    return resp
