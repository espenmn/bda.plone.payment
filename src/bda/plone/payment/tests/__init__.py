from zope.interface import alsoProvides
from plone.app.testing import (
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from bda.plone.payment.interfaces import IPaymentExtensionLayer


def set_browserlayer(request):
    """Set the BrowserLayer for the request.

    We have to set the browserlayer manually, since importing the profile alone
    doesn't do it in tests.
    """
    alsoProvides(request, IPaymentExtensionLayer)


class PaymentLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import bda.plone.payment
        self.loadZCML(package=bda.plone.payment,
                      context=configurationContext)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'bda.plone.payment:default')

    def tearDownZope(self, app):
        pass


Payment_FIXTURE = PaymentLayer()
Payment_INTEGRATION_TESTING = IntegrationTesting(
    bases=(Payment_FIXTURE,),
    name="Payment:Integration")
