# # Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# # сторона_а (довжина сторони a).
# # кут_а (кут між сторонами a і b).
# # кут_б (суміжний з кутом кут_а).
# # Необхідно реалізувати наступні вимоги:

# # Значення сторони сторона_а повинно бути більше 0.
# # Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# # Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.

# Для встановлення значень атрибутів використовуйте метод __setattr__.

# a, alpha, beta
# a > 0
# alpha+beta = 180


from math import sin, radians



class Romb:
    def __init__(self, a, alpha):
        if a > 0 and alpha>0 and alpha < 180:
            self.a = a
            self.alpha = alpha
        else:
            raise ValueError("Некоретне значення!")
            
    def __str__(self):
        return f"Romb with a = {self.a}, alpha = {self.alpha}, beta = {self.beta}."
        
    def periment(self):
        return 4 * self.a
        
    def __add__(self, other):
        return ((self.a)**2)*sin(radians(self.alpha)) + ((other.a)**2)*sin(radians(other.alpha))
        
romb = Romb(10, 60) + Romb(20, 80)

print(romb)
            

            
              
            
    














    




















