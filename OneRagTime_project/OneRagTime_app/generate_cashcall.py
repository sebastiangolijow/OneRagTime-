from models import Investor

def generate():
    print(Investor.objects.all())

print(generate())