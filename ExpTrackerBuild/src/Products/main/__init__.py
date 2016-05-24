from Products.main.app import MyTracker,manage_addMyTracker, addMyTracker


def initialize(registrar):
    registrar.registerClass(MyTracker,
                            constructors=(manage_addMyTracker, addMyTracker))