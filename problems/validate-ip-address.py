# https://leetcode.com/problems/validate-ip-address

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        DIGITS = set("0123456789")
        HEXDIGITS = set("0123456789abcdefABCDEF")
        
        
        def valid_ip4_block(num_block):
            if not num_block: return False  # missing/empty
            if not set(num_block).issubset(DIGITS): return False  # not only digits
            if num_block[0] == "0" and len(num_block) > 1: return False  # leading zero
            return 0 <= int(num_block) <= 255
        
        def valid_ip6_block(num_block):
            if not num_block: return False  # missing/empty
            if not set(num_block).issubset(HEXDIGITS): return False  # unallowed chars
            return len(num_block) < 5
        
        
        def validate_ipv4(queryIP):
            for num_block in queryIP.split("."):
                if not valid_ip4_block(num_block):
                    return "Neither" 
            return "IPv4"
        
        
        def validate_ipv6(queryIP):
            for num_block in queryIP.split(":"):
                if not valid_ip6_block(num_block):
                    return "Neither" 
            return "IPv6"
        
        
        if queryIP.count(".") == 3:
            return validate_ipv4(queryIP)
        elif queryIP.count(":") == 7:
            return validate_ipv6(queryIP)
        else:
            return "Neither"
        