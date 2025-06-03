from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        have_key = set()
        visited = set()
        queue = deque()
        closed_boxes = set()
    
        # Add initial boxes to the queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                closed_boxes.add(box)
    
        total_candies = 0
    
        while queue:
            box = queue.popleft()
            if box in visited:
                continue
            visited.add(box)

            # Collect candies
            total_candies += candies[box]
        
            # Collect keys
            for key in keys[box]:
                if key not in have_key:
                    have_key.add(key)
                    if key in closed_boxes:
                        queue.append(key)
                        closed_boxes.remove(key)
        
            # Process contained boxes
            for contained in containedBoxes[box]:
                if status[contained] == 1 or contained in have_key:
                    queue.append(contained)
                else:
                    closed_boxes.add(contained)

        return total_candies