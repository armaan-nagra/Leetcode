class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        queryIPv4 = queryIP.split('.')
        if len(queryIPv4) == 4:
            for query in queryIPv4:
                if not query:
                    return "Neither"
                if query and query[0] == '0' and len(query) > 1:
                    return "Neither"
                if not query.isdigit():
                    return "Neither"
                if int(query) > 255 or int(query) < 0:
                    return "Neither"
            return "IPv4"
        else:
            #check if IPv6 by splitting by :
            queryIPv6 = queryIP.split(':')
            if len(queryIPv6) != 8:
                return "Neither"
            else:
                for query in queryIPv6:
                    if not query:
                        return "Neither"
                    if len(query) > 4:
                        return "Neither"
                    for q in query:
                        if q not in ("0123456789abcdefABCDEF"):
                            return "Neither"
            return "IPv6"
        return "Neither"
