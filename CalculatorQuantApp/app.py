from CalculatorQuantApp.controllers import CalculatorQuant

calculator = CalculatorQuant()

def lambda_handler_quant_add(event : {} = None):
    resp = calculator.quant_add(**event)
    return resp

def lambda_handler_quant_subtract(event : {} = None):
    resp = calculator.quant_subtract(**event)
    return resp

def lambda_handler_quant_multiply(event : {} = None):
    resp = calculator.quant_multiply(**event)
    return resp

def lambda_handler_quant_divide(event : {} = None):
    resp = calculator.quant_divide(**event)
    return resp


def lambda_handler_quant_divide_abs(event : {} = None):
    resp = calculator.quant_divide_abs(**event)
    return resp

def lambda_handler_quant_add_abs(event : {} = None):
    resp = calculator.quant_add_abs(**event)
    return resp


def lambda_handler_quant_subtract_abs(event : {} = None):
    resp = calculator.quant_subtract_abs(**event)
    return resp
