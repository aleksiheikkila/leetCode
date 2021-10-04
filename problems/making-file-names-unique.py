# https://leetcode.com/problems/making-file-names-unique

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        suffixes = {}  # key: filename, val is the previous suffix int
        rst = []
        
        for name in names:
            if name not in suffixes:
                suffixes[name] = 0
                rst.append(name)
            else:
                suffixes[name] += 1
                while f"{name}({suffixes[name]})" in suffixes:
                    suffixes[name] += 1
                
                # now the correct name is f"{name}({suffixes[name]})"
                # add to suffixes, so that there will be collision if this name was tried
                suffixes[f"{name}({suffixes[name]})"] = 0
                rst.append(f"{name}({suffixes[name]})")
                
        return rst
        