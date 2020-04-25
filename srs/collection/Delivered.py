class Delivered():
    def __init__(self, packetId, memberId):
        self.__packetId = packetId
        self.__memberId = memberId
    def __str__(self):
        s = 'Packet id: '+ str(self.__packetId) + '\nMember id: '+ str(self.__memberId)
        return s
    