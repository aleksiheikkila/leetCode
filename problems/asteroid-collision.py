# https://leetcode.com/problems/asteroid-collision


class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # maintain a stable list of asteroids A
        A = []
        
        for ast in asteroids:
            # if A is empty, we can add the next asteroid freely
            if len(A) == 0:
                A.append(ast)
                continue
            
            # CASE: collision
            if ast < 0 and A[-1] > 0:
                abs_ast = abs(ast)
                if A[-1] == abs_ast:
                    # both destroyed, then A will again be stable
                    A.pop()
                    continue
                    
                #if A[-1] > abs_ast:
                #    # new ast destroyed, A still stable
                #    continue
                
                 
                if A[-1] < abs_ast:
                    # A[-1] gets destroyed, A might not be stable anymore
                    # keep checking for cascading effects
                    for i in reversed(range(len(A))):
                        # no more collisions:
                        if A[i] < 0:
                            # moving away
                            A = A[:i+1] + [ast]
                            break
                        # collision, with new asteroid being bigger
                        if A[i] < abs_ast:
                            if i == 0:
                                A = [ast]
                                break
                            continue
                            
                        # collision, same size
                        if A[i] == abs_ast:
                            A = A[:max(0, i)]
                            break
                        
                        # collision, prev asteroid being bigger
                        else:
                            A = A[:i+1]
                            break
            
            # CASE: no collision, add the next asteroid and continue                          
            else:
                A.append(ast)
        
        return A
 