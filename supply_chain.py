import random

def supply_chain_analysis(data):
    material_demand = data['material_demand']
    suppliers = ["Supplier A", "Supplier B", "Supplier C"]
    best_supplier = random.choice(suppliers)
    return {"best_supplier": best_supplier, "expected_delay": "2 days"}
