from stevedore import named
from designate.openstack.common import log as logging

LOG = logging.getLogger(__name__)


class ExtensionController:

    def __init__(self, namespace, names):
        LOG.debug('EXTENSIONCONTROLLER')
        self._mgr = named.NamedExtensionManager(
            namespace=namespace,
            names=names,
            invoke_on_load=True,
        )
        LOG.debug(self._mgr.__dict__)
        LOG.debug(self._mgr._names)
        for e in self._mgr:
            LOG.debug('EXTENSIONCONTROLLER name = ' + e.name)
            setattr(self, e.name, e.obj)

# class ExtensionController:

#     def __init__(self, namespace):
#         LOG.debug('EXTENSIONCONTROLLER')
#         self._mgr = stevedore.ExtensionManager(
#             namespace=namespace,
#             invoke_on_load=True,
#         )
#         for e in self._mgr:
#             LOG.debug('EXTENSIONCONTROLLER name = ' + e.name)
#             setattr(self, e.name, e.obj)
