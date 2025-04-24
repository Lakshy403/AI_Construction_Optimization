import random

def optimize_schedule(data):
    workforce = data['workforce']
    optimized = sorted(workforce, key=lambda x: x['efficiency'], reverse=True)
    return optimized[:10]  # Return top 10 optimized workers
