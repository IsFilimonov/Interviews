def cakes(recipe, available):
    total = {}
    
    for k, v in recipe.items():
        if k in available:
            total.update({k: available[k] // recipe[k]})
        else: 
            total.update({k: 0})
    
    return min(total.values())

