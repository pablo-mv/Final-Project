class Incidents:
    def __init__(self, packetId, memberId, reason):
        self.__packetId = packetId
        self.__memberId = memberId
        self.__reason = reason
    def __str__(self):
        s = 'Packet id: '+ str(self.__packetId) + '\nMember id: '+ str(self.__memberId) + '\n It could not been delivered because of: ' + reason
        return s