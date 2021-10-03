class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Check for empty list
        if len(nums) == 0:
            return -1
        
        # Check for list with one value 
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        def counter():
            lo, hi = 0, len(nums) - 1
            while lo <= hi: 
                mid = (lo + hi) // 2
                mid_number = nums[mid]

                if mid >= lo and mid_number < nums[mid-1]:
                    # The middle position is the answer 
                        return mid
                elif mid_number > nums[hi]:
                    # Answer lies in the right half
                    lo = mid + 1

                else:
                    # Answer lies in the left half
                    hi = mid - 1

            return 0
        
        result = counter()
        print(result)
        
        # If list sorted
        if result == 0:
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_number = nums[mid]

                if mid_number == target:
                    return mid
                elif mid_number < target: 
                    lo = mid + 1
                elif mid_number > target:
                    hi = mid - 1
            return -1
        
        #left
        if target >= nums[0] and target <= nums[result-1]:
            lo, hi = 0, result
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_number = nums[mid]

                if mid_number == target:
                    return mid
                elif mid_number < target:
                    lo = mid + 1  
                elif mid_number > target:
                    hi = mid - 1 
            return -1
        
        # right
        if target <= nums[len(nums) - 1] and target >= nums[result]:
            lo, hi = result, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_number = nums[mid]

                if mid_number == target:
                    return mid
                elif mid_number < target:
                    lo = mid + 1  
                elif mid_number > target:
                    hi = mid - 1
            return -1
        
        return -1
