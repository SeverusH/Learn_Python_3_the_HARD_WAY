class Parent(object):
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("Child, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("Child, AFTER PARENT altered()")


dad = Parent()
son = Child()

print(">>>> Parent.implicit()")
dad.implicit()
print(">>>> Child.implicit()")
son.implicit()

print(">>>> Parent.override()")
dad.override()
print(">>>> Child.override()")
son.override()

print(">>>> Parent.altered()")
dad.altered()
print(">>>> Child.altered()")
son.altered()
