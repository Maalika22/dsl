import rpyc

class StringService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_concatenate(self, str1, str2):
        return str1 + str2

if _name_ == "_main_":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(StringService, port=18861)
    print("Server is running on port 18861...")
    server.start()
