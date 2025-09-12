class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip4 = queryIP.split('.')
        ip6 = queryIP.split(':')
        if len(ip4) == 4:
            for i in ip4:
                if not i.isdigit():
                    return "Neither"
                if len(i) > 3 or (len(i) != 1 and i[0] == "0"):
                    return "Neither"
                if not (0 <= int(i) <= 255):
                    return "Neither"
            return "IPv4"

        ch = set('abcdefABCDEF')
        if len(ip6) == 8:
            for k in ip6:
                if len(k) > 4 or len(k) == 0:
                    return "Neither"
                for l in k:
                    if not (l.isdigit() or l in ch):
                        return "Neither"
            return "IPv6"
        
        return "Neither"