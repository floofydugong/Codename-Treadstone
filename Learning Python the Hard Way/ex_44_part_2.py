#Composition Example
class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER override()"

    def altered(self):
        print "OTHER altered()"

class Child(object):
    #Child has a "other"
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD AFTER OTHER altered()"

#son is an instance of Child
son = Child()

son.implicit()
son.override()
son.altered()

