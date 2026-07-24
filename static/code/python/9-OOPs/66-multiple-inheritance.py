class Base:
    label = "A: Base Class"


class Cd:
    label = "B: Masala Blend"


# we can inherit from multiple class
class Another(Cd, Base):
    pass


#
# ------------ MRO - Method Resolution Order ------------------


class A:
    label = "A: Base Class"


class B(A):
    label = "B: Masala Blend"


class C(A):
    label = "C: Herbal Blend"


class D(B, C):
    pass


cup = D()

# so which label will be used?
print(cup.label)  # B: Masala Blend

# Python resolves using Method Resolution Order (MRO):
# D → B → C → A → object
# It does NOT simply check parents level-by-level,
# but uses C3 linearization to determine order.
# we can use this dunder to see
print(D.__mro__)
